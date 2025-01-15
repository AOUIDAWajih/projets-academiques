# Rendu M1 MIASHS AOUIDA WAJIH INE(203351642DB)



rm(list = ls())

# Installer les packages nécessaires 
if (!require("tm")) install.packages("tm", dependencies=TRUE)
if (!require("wordcloud")) install.packages("wordcloud", dependencies=TRUE)
if (!require("lsa")) install.packages("lsa", dependencies=TRUE)
if (!require("tidyverse")) install.packages("tidyverse", dependencies=TRUE)
if (!require("tidytext")) install.packages("tidytext", dependencies=TRUE)



# Charger les bibliothèques nécessaires
library(tm)
library(wordcloud)
library(lsa)
library(tidyverse)
library(tidytext)



####### 1)

# Étape 1: Charger les données depuis le fichier CSV
data <- read.csv("C:\\Users\\pc\\Downloads\\data.csv", header = FALSE, stringsAsFactors = FALSE)
colnames(data) <- c("number","Segment", "Parti")

####### 2)
#  Séparer les données par parti (LFI et RN)
lfi_data <- data[data$Parti == "LFI", ]
rn_data <- data[data$Parti == "RN", ]

# Créer une matrice pour le parti LFI
lfi_matrix <- table(unlist(strsplit(tolower(lfi_data$Segment), " ")))

# Créer une matrice pour le parti RN
rn_matrix <- table(unlist(strsplit(tolower(rn_data$Segment), " ")))

# Afficher les matrices
print("Matrice pour LFI:")
print(lfi_matrix)

print("Matrice pour RN:")
print(rn_matrix)


###### 3)

# Fonction pour générer la wordcloud
generate_wordcloud <- function(data, title) {
  # Prétraitement du texte
  corpus <- Corpus(VectorSource(tolower(data$Segment)))
  
  # Créer un tableau de termes
  dtm <- DocumentTermMatrix(corpus)
  
  # Extraire les termes les plus fréquents
  freq_terms <- colSums(as.matrix(dtm))
  top_terms <- head(sort(freq_terms, decreasing = TRUE), 50)
  
  # Générer la wordcloud
  wordcloud(names(top_terms), freq = top_terms, scale=c(4,0.5),  main = title)
}

# Générer la wordcloud pour le parti LFI
generate_wordcloud(lfi_data, "Wordcloud - LFI")

# Générer la wordcloud pour le parti RN
generate_wordcloud(rn_data, "Wordcloud - RN")


###### 4)


# Fonction pour appliquer LSA à une matrice
apply_lsa <- function(matrix, dimensions) {
  # Prétraitement du texte
  corpus <- Corpus(VectorSource(tolower(matrix$Segment)))
  
  # Créer une matrice de termes
  dtm <- DocumentTermMatrix(corpus)
  
  
  # Appliquer l'algorithme LSA
  lsa_space <- lsa(dtm, dims = dimensions)
  
  # Retourner l'espace LSA
  return(lsa_space)
}

# Appliquer LSA à la matrice du parti LFI en dimension 5
lfi_lsa <- apply_lsa(lfi_data, 5)

# Appliquer LSA à la matrice du parti RN en dimension 5
rn_lsa <- apply_lsa(rn_data, 5)

# Afficher les résultats
print("LSA pour LFI:")
print(lfi_lsa)

print("LSA pour RN:")
print(rn_lsa)


###### 5 )


# Fonction pour obtenir les termes les plus similaires après LSA
get_similar_terms_after_lsa <- function(lsa_space, word, k = 5) {
  # Trouver l'indice du mot dans la matrice tk
  word_index <- which(rownames(lsa_space$tk) == word)
  
  if (length(word_index) == 0) {
    stop(paste0("Le terme '", word, "' n'est pas présent dans l'espace LSA"))
  }
  
  # Extraire la colonne correspondant au mot
  word_vector <- lsa_space$tk[, word_index, drop = FALSE]
  
  # Calculer la similarité cosinus avec tous les termes
  similarities <- sim2(word_vector, lsa_space$tk, method = "cosine")
  
  # Trier les termes par similarité 
  top_k_indexes <- order(similarities, decreasing = TRUE)[1:k]
  top_k_terms <- rownames(lsa_space$tk)[top_k_indexes]
  
  return(top_k_terms)
}

# Appliquer la fonction pour obtenir les termes les plus similaires après LSA pour le parti LFI
lfi_similar_terms_after_lsa <- get_similar_terms_after_lsa(lfi_lsa, "français", 5)
print(paste("Termes les plus similaires à 'français' après LSA pour le parti LFI :", paste(lfi_similar_terms_after_lsa, collapse = ", ")))

# Appliquer la fonction pour obtenir les termes les plus similaires après LSA pour le parti RN
rn_similar_terms_after_lsa <- get_similar_terms_after_lsa(rn_lsa, "français", 5)
print(paste("Termes les plus similaires à 'français' après LSA pour le parti RN :", paste(rn_similar_terms_after_lsa, collapse = ", ")))



####### 6)



# Charger le contenu du fichier texte
chemin_fichier <- "C:\\Users\\pc\\Downloads\\extrait.txt"
texte <- readLines(chemin_fichier, warn = FALSE)

# Convertir le texte en une seule chaîne de caractères
texte_complet <- paste(texte, collapse = " ")

# Diviser la chaîne en phrases d'environ 10 mots chacune
mots <- strsplit(texte_complet, "\\s+")[[1]]
mots_par_groupe <- split(mots, ceiling(seq_along(mots)/10))

# Afficher les groupes de mots
for (groupe in mots_par_groupe) {
  print(paste(groupe, collapse = " "))
}

# Calculer le nombre de lignes nécessaires pour la matrice
nb_lignes <- length(mots_par_groupe)

# Créer une matrice avec les segments de mots
matrice_segments <- matrix("", nrow = nb_lignes, ncol = 10, byrow = TRUE)

# Remplir la matrice avec les segments de mots
for (i in seq_len(nb_lignes)) {
  matrice_segments[i, ] <- head(mots_par_groupe[[i]], 10)
}

# Afficher la matrice
print(matrice_segments)

# Compter la fréquence des mots
table_mots <- table(mots)

# Sélectionner les 50 mots les plus fréquents
mots_freq <- names(sort(table_mots, decreasing = TRUE)[1:50])

wordcloud(words = mots_freq, freq = table_mots[mots_freq], scale=c(3,0.5), colors=brewer.pal(8, "Dark2"))

# Créer la matrice termes-documents
dtm1 <- TermDocumentMatrix(Corpus(VectorSource(texte)), control = list(wordLengths=c(1, Inf)))

# Appliquer l'algorithme LSA
lsa_resultat <- lsa:::LSA(dtm1)

