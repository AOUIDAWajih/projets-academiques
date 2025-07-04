# Prévision de la Demande en Série Temporelle avec XGBoost 🔋📈

Ce dépôt contient un notebook Jupyter (`XGBoost_for_Time_Series_Dataset_DemandForecasting.ipynb`) qui démontre l'utilisation de l'algorithme **XGBoost** pour la **prévision de la demande énergétique** en série temporelle, en utilisant le jeu de données **PJME_hourly**.

Le notebook couvre les étapes de **prétraitement des données**, **entraînement du modèle**, **prédiction**, **évaluation**, et **visualisation** (valeurs réelles vs prédites, analyse des erreurs, etc.).

---

## 📊 Jeu de Données

Le jeu de données utilisé est **`PJME_hourly.csv`**, contenant la **consommation horaire d'énergie (en MW)** pour la région PJME.  
- Le fichier est indexé par une colonne **datetime**.
- La variable cible est **`PJME_MW`**.

---

## 🛠️ Pré-requis

Pour exécuter le notebook, assurez-vous d’avoir les bibliothèques Python suivantes installées :

```bash
pip install pandas numpy matplotlib seaborn xgboost scikit-learn
