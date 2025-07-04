# Fine-tuning de BERT pour l'Analyse de Sentiment de Commentaires Clients 📝💬

Ce projet démontre comment **affiner un modèle BERT** pour l’analyse de sentiment à partir des commentaires clients, en utilisant le dataset **Yelp**.  
Le notebook `FineTuning_Transformer_BERT_Customer_Review.ipynb` fournit un workflow complet incluant :

- le chargement et le prétraitement des données,  
- l'entraînement du modèle BERT,  
- l'évaluation de ses performances,  
- et la prédiction sur de nouveaux commentaires.

---

## 📚 Table des Matières

- [Aperçu](#aperçu)
- [Jeu de Données](#jeu-de-données)
- [Pré-requis](#pré-requis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités Clés](#fonctionnalités-clés)
- [Évaluation du Modèle](#évaluation-du-modèle)
- [Exemples de Prédiction](#exemples-de-prédiction)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## 🔍 Aperçu

Ce projet affine un modèle **BERT** pour classifier les avis clients selon des catégories de sentiment, en se basant sur les **évaluations par étoiles** (1 à 5 étoiles, remappées sur 0 à 4 pour des raisons de compatibilité modèle).

Le pipeline inclut :
- le prétraitement des données,
- l'entraînement du modèle,
- l’évaluation à l’aide d’une **matrice de confusion** et d’un **rapport de classification**.

---

## 🧾 Jeu de Données

Le dataset utilisé est **`yelp.csv`**, contenant des avis clients avec leur **note étoilée** et d’autres métadonnées.

Les évaluations par étoiles sont mappées comme suit :

| Étoiles | Label utilisé |
|---------|----------------|
| 1       | 0              |
| 2       | 1              |
| 3       | 2              |
| 4       | 3              |
| 5       | 4              |

---

## 🛠️ Pré-requis

- **Python 3.7+**
- Bibliothèques Python :
  - `transformers`
  - `tokenizers`
  - `torch`
  - `pandas`
  - `numpy`
  - `seaborn`
  - `matplotlib`
  - `scikit-learn`

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

