import numpy as np

# Définir la matrice de Leslie
L = np.array([[0, 0, 1.5, 4.2, 3, 2.5, 1.5, 0, 0, 0],
              [65, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 68, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 75, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 7, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 55, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 35, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 2, 0]])

# Population initiale en 1900
initial_population = np.array([100, 0, 0, 0, 0, 0, 0, 0, 0, 0]).reshape(-1, 1)


####### PART ONE #######


# Définir le nombre d'années à simuler
years = [1910,1920, 1930, 1950,1995, 2000]

# Effectuer des calculs itératifs pour chaque année
for year in years:
    k = year - 1900
    original_population = np.linalg.matrix_power(L, k) @(initial_population)
    print(f"Population in {year}: {original_population}")

# Calculer les valeurs propres pour vérifier la stabilité a long terme
valeurs_propres =np.linalg.eigvals(L)
print(f"\nles valeurs propres: {valeurs_propres}")

if all(abs(eig) < 1 for eig in valeurs_propres):
    print("The population is stable.")
else:
    print("The population is unstable.")

"""Si toutes les valeurs propres d'une matrice sont strictement
 inférieures à 1 en valeur absolue, cela indique que le système 
 est stable. Cette condition est basée sur le fait que si toutes 
 les valeurs propres sont inférieures à 1 en valeur absolue, alors
  les composantes du vecteur propre correspondant diminuent 
  exponentiellement au fil du temps, 
 ce qui conduit à une stabilité à long terme du système."""


# Calculer des ratios entre années consécutives
ratios = []

# Effectuer des calculs itératifs pour chaque année
for i in range(1, len(years)):
    k_prev = years[i-1] - 1900
    k_curr = years[i] - 1900

    population_prev = np.linalg.matrix_power(L, k_prev) @ initial_population
    population_curr = np.linalg.matrix_power(L, k_curr) @ initial_population

    # Vérification pour éviter la division par zéro
    if np.all(population_prev != 0):
        ratio = population_curr / population_prev
        ratios.append(ratio)
        print(f"Ratio between {years[i - 1]} and {years[i]}: {np.round(ratio, 2)}")
    else:
        print(f"Ratio between {years[i - 1]} and {years[i]}: N/A (population_prev contains zeros)")

# afficher les ratios
print("Ratios:", np.round(ratios, 2))

# Ratio entre 1920 et 1930
ratio_1920_1930 = ratios[1]
print(f"Ratio between 1920 and 1930: {ratio_1920_1930}")
"""Dans notre cas, les ratios les plus constants semblent
 être ceux entre les années 1920 et 1930."""

# Calculer la moyenne des ratios
average_ratio_1920_1930 = np.mean(ratio_1920_1930)
print(f"Average ratio between 1920 and 1930: {average_ratio_1920_1930}")

"""L'average_ratio_1920_1930 est la constante associée à ces ratios.
Ce ratio constant peut nous fournir des informations sur le comportement 
à long terme du système(comme les valeurs propres). En particulier, 
si ce ratio est proche de 1,cela pourrait indiquer une stabilité à long terme du système.
Si le ratio est nettement différent de 1, cela pourrait indiquer
une croissance ou une decroissance à long terme de la population."""

"""dasn notre cas, avec les resultats du deux methode, la population 
a long terme est unstable"""


######## PART TWO ######

# Définir les facteurs de réduction de la pollution
birth_rate_reduction = 0.10
survival_reduction = 0.15

# Créer une matrice de Leslie modifiée avec des effets de pollution
modified_L = L.copy()
modified_L[0, 2:6] *= (1 - birth_rate_reduction)
modified_L[1:6, 2:6] *= (1 - survival_reduction)


# Définir le nombre d'années à simuler
years1 = [1990]

# Effectuer des calculs itératifs pour chaque année de years1 avec la matrice de Leslie original
for year in years:
    k = year - 1900
    original_population_1990 = np.linalg.matrix_power(L, k)@(initial_population)

# Effectuer des calculs itératifs pour chaque année de years1 avec la matrice de Leslie modifiée
for year in years1:
    k =  year - 1900
    modified_population_1990 = np.linalg.matrix_power(modified_L, k)@(initial_population)

# afficher les  populations
print(f"Population in 1990 (Original): {original_population_1990}")
print(f"Population in 1990 (Modified with Pollution Effects): {modified_population_1990}")

"""En comparant ces deux résultats, on observe que la population 
modélisée avec les effets de la pollution est beaucoup plus faible 
que la population modélisée sans les effets de la pollution.
Le (birth_rate_reduction) et (survival_reduction) ont entrainé  une 
diminution du nombre de naissances et une diminution du taux de 
survie, ce qui, combiné, conduit à une population plus faible."""


###### PART THREE #######
# a)

# définir l'âge de début de la pêche
harvesting_start_age =3

# Définir le harvesting rate
harvesting_rate =0.25

# Créer une matrice pour représenter le processus de pêche
F = np.zeros_like(L)
F[harvesting_start_age-1:, :-1] = harvesting_rate

# Calculate the new Leslie matrix
L_prime_harvest = L * (1 - F)

print("Modified Leslie matrix for the harvesting_rate=0.25:")
print(L_prime_harvest)

"""Dans la modification fournie, j'ai supposé que la pêche 
des poissons intervient après le processus de naissance annuel  
car le processus de pêche affecte les poissons âgés de 3 ans et 
plus, il doit etre appliquer après le processus de naissance, qui implique 
la production de nouveaux individus."""


# Définir le harvesting rate
harvesting_rate1 = 0.20

F = np.zeros_like(L)
F[harvesting_start_age-1:, :-1] = harvesting_rate1

L_prime_harvest1 = L * (1 - F)

print("Modified Leslie matrix for harvesting_rate=0.2:")
print(L_prime_harvest1)

#b)

# Définir le nombre d'années à simuler
years2= [1930, 1950, 1995, 2000]

# Effectuer des calculs itératifs pour chaque année avec la matrice de Leslie modifiée
for year in years2:
    k = year - 1900
    harvest_population = np.linalg.matrix_power(L_prime_harvest1, k) @ initial_population
    # afficher la population
    print(f"Population in {year} (Original): {original_population}")
    print(f"Population in {year} (With Harvesting): {harvest_population}")
    print(f"Harvesting rate: {harvesting_rate1}")
"""si on prend l'années 1930 comme example, on remarque  les 
populations avec la pêche sont significativement plus
basses que les populations sans pêche. Cela suggère que la 
stratégie de pêche a entraîné une diminution de la population 
par rapport au scénario sans pêche."""


# c)

# Définir une variable de harvesting rate(h) à expérimenter
harvesting_rates = np.arange(0.01, 1.01, 0.01)

# Définir le nombre d'années à simuler
years4 = 30
"""pour 1930"""

# afficher les resultats
print("c)Harvesting Rate\tPopulation in 2000")

# Effectuer des calculs itératifs pour chaque taux de récolte
for harvesting_rate in harvesting_rates:
    F = np.zeros_like(L)
    F[harvesting_start_age - 1:, :-1] = harvesting_rate

    L_prime_harvest = L * (1 - F)

    final_population = np.linalg.matrix_power(L_prime_harvest, years4)@(initial_population)

    print(f"pour h= {harvesting_rate:.2f}\n{final_population}")
    print(f"Population in {1930} (Original): {original_population}")

"""pour h=0.45"""

###### PART FOUR

"""la peche pour les (1-3 years old) entraîne une augmentation de la 
mortalité parmi les groupes d'âge de 1 à 3 ans,donc une diminution des taux 
de survie pour ces groupes d'âge donc diminution des recoltes"""

# Définir les tranches d'âge
harvesting_age_groups = [1, 2, 3]

F = np.zeros_like(L)

# Appliquer le harvesting_rate aux tranches d'âge spécifiées
for age_group in harvesting_age_groups:
    F[age_group-1:, :-1] = harvesting_rate1

L_prime_harvest2 = L * (1 - F)

print("Modified Leslie matrix for harvesting_rate=0.2 with extended age groups:")
print(L_prime_harvest2)

years3 = [1930, 1950, 1995, 2000]

for year in years3:
    k = year - 1900
    harvest_population2 = np.linalg.matrix_power(L_prime_harvest2, k) @ initial_population

    # Afficher les populations
    print(f"Population in {year} (Original): {original_population}")
    print(f"Population in {year} (With Harvesting - Extended Age Groups): {harvest_population2}")
    print(f"Harvesting rate: {harvesting_rate1}")


####### PART FIVE ###########
#a)

age_groups_fine = [3, 4, 5]
age_groups_coarse = [5, 6, 7, 8]

F_fine = np.zeros_like(L)
F_coarse = np.zeros_like(L)

# Appliquer le harvesting_rate aux groupes d'âge spécifiés pour chaque nets
for age_group in age_groups_fine:
    F_fine[age_group-1:, :-1] = harvesting_rate1

for age_group in age_groups_coarse:
    F_coarse[age_group-1:, :-1] = harvesting_rate1

# Calculer la nouvelle matrice de Leslie avec l'effet combiné des deux réseaux
L_effect_dual_nets = L * (1 - F_fine - F_coarse)

print("Modified Leslie matrix for using two nets with different mesh fineness:")
print(L_effect_dual_nets)

#b)

"""En ciblant des groupes d'âge spécifiques, la stratégie de pêche 
peut contribuer à maintenir une distribution d'âge plus équilibrée 
au sein de la population. L'objectif est d'éviter une surpêche de 
certains groupes d'âge, ce qui pourrait perturber la structure globale 
de la population. Cela pourrait contribuer à la stabilité à long terme 
de la population.
aussi, elle permet un meilleur contrôle de la capacité reproductive de 
la population. Par exemple, en ciblant des groupes d'âge avec un potentiel 
reproductif plus élevé, on peut optimiser le rendement global. La 
combinaison de mailles fines et grossières offre une flexibilité pour 
adapter la stratégie de pêche aux taux de reproduction et de survie 
variables des différents groupes d'âge."""