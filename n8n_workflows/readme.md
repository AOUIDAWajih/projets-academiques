# n8n Workflows

Ce dossier contient trois workflows n8n prêts à l'emploi pour automatiser différentes tâches à l'aide de l'intelligence artificielle et d'intégrations cloud.

---

## 1. Get a summary of each podcast in your YouTube playlist

**Objectif :**  
Transcrire automatiquement vos podcasts ou vidéos préférées dans une playlist YouTube et générer un résumé détaillé grâce à l'IA.

**Utilisateurs cibles :**  
- Fans de podcasts souhaitant gagner du temps  
- Professionnels occupés suivant des vidéos éducatives ou industrielles  
- Créateurs de contenu ou chercheurs qui analysent beaucoup de vidéos  

**Fonctionnalités :**  
- Récupère toutes les vidéos d'une playlist YouTube  
- Extrait les titres, URLs et IDs  
- Transcrit et combine les textes  
- Génère un résumé AI structuré de chaque épisode  
- Enregistre tout dans Google Sheets (titres, transcription, résumé, numéro de ligne)  

**Configuration :**  
- OAuth2 YouTube et Google Sheets  
- API de transcription et IA  
- ID de la playlist à configurer  

---

## 2. Automate Email Filtering & AI Summarization

**Objectif :**  
Automatiser le traitement des emails entrants et générer des résumés concis avec l’IA, pour ensuite les enregistrer dans Google Sheets.

**Utilisateurs cibles :**  
- Professionnels recevant de nombreux emails  
- Équipes de support client  
- Chefs de projets suivant la correspondance  

**Fonctionnalités :**  
- Surveille la boîte Gmail pour de nouveaux emails  
- Filtre les emails selon des critères spécifiques  
- Extrait les informations clés (expéditeur, date, sujet, contenu)  
- Résume le contenu avec l’IA  
- Enregistre tout dans Google Sheets  

**Configuration :**  
- OAuth2 Gmail et Google Sheets  
- API Groq pour l’IA  
- Personnalisation des filtres et critères de validation  

---

## 3. Free AI Image Generator

**Objectif :**  
Créer automatiquement des images personnalisées à partir de prompts, avec génération IA.

**Utilisateurs cibles :**  
- Créateurs de contenu marketing  
- Designers et illustrateurs  
- Toute personne souhaitant générer des images rapidement  

**Fonctionnalités :**  
- Déclenchement via message chat N8N ou Telegram  
- Prompt structuré et propre pour la génération  
- Utilisation de Google Gemini ou autres modèles IA  
- Prévisualisation et sauvegarde locale ou via Telegram  

**Configuration :**  
- Compte Google Gemini pour la génération d’images  
- Bot Telegram (optionnel)  
- Paramètres par défaut : taille 1080x1920, modèle "flux"  
- Possibilité de personnaliser le modèle, la taille, et le prompt  

---

## Instructions générales pour tous les workflows

1. Importer le fichier JSON du workflow dans votre instance n8n.  
2. Configurer les credentials nécessaires (YouTube, Gmail, Google Sheets, IA, Telegram, etc.).  
3. Ajuster les paramètres selon vos besoins (playlist ID, filtre email, taille d’image, modèle IA…).  
4. Activer le workflow et tester son fonctionnement.  
5. Pour Google Sheets, créer un document et renseigner l’ID correspondant dans le workflow.  

---

## Licence et attribution

Les modèles et services IA utilisés (Google Gemini, Groq, etc.) sont sous leurs propres licences respectives.  

