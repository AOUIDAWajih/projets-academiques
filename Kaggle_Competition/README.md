# 🧬 Résumé Automatique d’Articles Scientifiques Médicaux avec LLM

Ce projet a pour objectif de développer un **système de résumé automatique** basé sur un **grand modèle de langue (LLM)** afin de synthétiser des publications scientifiques en médecine. Le système est optimisé pour deux types spécifiques de publications :

- 🧪 **Les essais contrôlés randomisés (ECR)**
- 🔬 **Les études observationnelles**

> 🥇 **Dans ce projet j'ai obtenu la 1ère place dans la compétition Kaggle** [M2 - Résumé d'articles scientifiques](https://www.kaggle.com/competitions/m-2-maliash-resume-darticles-scientifiques).

---

## 🎯 Objectifs du projet

- Créer un modèle robuste capable de produire des résumés fiables à partir de textes scientifiques longs et complexes.
- Comparer les performances à l’aide de la métrique **ROUGE**, utilisée pour évaluer la qualité d’un résumé automatique par rapport à un résumé de référence.

---

## 🧠 Approche

- Utilisation de modèles de type **Large Language Models (LLMs)**, comme ceux basés sur la famille **T5 / BART / GPT**.
- Prétraitement soigné du texte scientifique (normalisation, nettoyage des sections).
- Entraînement supervisé sur des résumés de référence rédigés par des experts.
- Évaluation via les scores **ROUGE-1, ROUGE-2 et ROUGE-L**.

---

## 📂 Contenu du dépôt

- `notebooks/` : Contient le notebook de préparation de données, fine-tuning et évaluation.


---

## 📊 Données

Les données sont fournies par la compétition Kaggle :
- Texte complet d’articles scientifiques
- Résumés de référence rédigés manuellement
- Méta-informations sur le type d’étude

Lien vers la compétition : [https://www.kaggle.com/competitions/m-2-maliash-resume-darticles-scientifiques](https://www.kaggle.com/competitions/m-2-maliash-resume-darticles-scientifiques)

---

## 🧪 Évaluation

L’évaluation est basée sur la **métrique ROUGE** :
- **ROUGE-1** : n-grammes unigrams
- **ROUGE-2** : bigrams
- **ROUGE-L** : plus longue sous-séquence commune

Le modèle proposé a atteint des performances exceptionnelles, se classant **1er dans le leaderboard final** de la compétition.

---

## 🚀 Reproduire les résultats

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/ton-utilisateur/nom-du-repo.git
   cd nom-du-repo
