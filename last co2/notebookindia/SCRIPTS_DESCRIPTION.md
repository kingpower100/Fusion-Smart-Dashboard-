# 📚 Description des Scripts et Notebooks - Fusion Smart Dashboard

## 🎯 **Scripts Principaux**

### **1. `app.py` - Application Principale** 🚀
**Description** : Le cœur de votre dashboard énergétique intelligent
**Fonctionnalités** :
- Interface utilisateur Streamlit complète
- Navigation entre toutes les pages
- Intégration de l'Assistant IA
- Gestion des sessions et cache
- Thème sombre personnalisé

**Pages incluses** :
- 🏠 Accueil avec météo en temps réel
- 🗺️ Carte CO₂ interactive
- 📊 Recommandations IA
- 🧠 Simulateur bayésien
- 🤖 Simulateur multi-agents
- 💬 Assistant IA spécialisé

**Utilisation** : `streamlit run app.py`

---

### **2. `energy_assistant_wrapper.py` - Wrapper Assistant IA** 🤖
**Description** : Interface d'intégration pour l'Assistant IA spécialisé énergie
**Fonctionnalités** :
- Gestion des chemins Python dynamiques
- Chargement automatique des modèles FAISS
- Configuration des variables d'environnement
- Gestion d'erreurs robuste
- Cache intelligent des ressources

**Utilisation** : Importé automatiquement par `app.py`

---

### **3. `preload_models.py` - Préchargement des Modèles** ⚡
**Description** : Script d'optimisation pour charger les modèles IA en avance
**Fonctionnalités** :
- Chargement des index FAISS
- Initialisation du modèle SentenceTransformer
- Chargement des chunks et métadonnées
- Mesure des temps de chargement
- Préparation du cache

**Utilisation** : `python preload_models.py`

---

### **4. `run_optimized.py` - Démarrage Optimisé** 🚀
**Description** : Script de démarrage avec optimisations de performance
**Fonctionnalités** :
- Préchargement automatique des modèles
- Configuration des variables d'environnement
- Démarrage Streamlit optimisé
- Gestion des erreurs
- Port configuré (8511)

**Utilisation** : `python run_optimized.py`

---

## 📁 **Pages du Dashboard**

### **5. `pages/map_co2.py` - Carte CO₂ Interactive** 🗺️
**Description** : Visualisation géographique des émissions de CO₂
**Fonctionnalités** :
- Cartes interactives avec Folium
- Données géospatiales
- Visualisation des émissions par zone
- Interface utilisateur intuitive
- Export des données

**Technologies** : Folium, GeoPandas, Streamlit

---

### **6. `pages/campus_energy_network_graph.py` - Réseau Énergétique** 🌐
**Description** : Visualisation du réseau énergétique du campus
**Fonctionnalités** :
- Graphiques de réseau interactifs
- Analyse des connexions énergétiques
- Visualisation des flux
- Interface de navigation
- Métriques de performance

**Technologies** : NetworkX, Plotly, Streamlit

---

### **7. `pages/recommandations.py` - Recommandations IA** 💡
**Description** : Système de recommandations basé sur l'IA
**Fonctionnalités** :
- Analyse des données énergétiques
- Génération de recommandations
- Interface utilisateur intuitive
- Historique des suggestions
- Métriques d'efficacité

**Technologies** : Pandas, NumPy, Streamlit

---

### **8. `pages/simulateur_bayesien.py` - Simulateur Bayésien** 🧠
**Description** : Modélisation probabiliste des systèmes énergétiques
**Fonctionnalités** :
- Modèles bayésiens
- Prédictions probabilistes
- Interface de paramétrage
- Visualisation des résultats
- Export des analyses

**Technologies** : PyMC, NumPy, Plotly

---

### **9. `pages/simulateur_multi_agents.py` - Simulateur Multi-Agents** 🤖
**Description** : Simulation de systèmes complexes avec agents multiples
**Fonctionnalités** :
- Modélisation multi-agents
- Simulation comportementale
- Interface de configuration
- Visualisation des interactions
- Analyse des résultats

**Technologies** : Mesa, NumPy, Plotly

---

## 🔧 **Scripts d'Installation**

### **10. `install_windows.bat` - Installation Windows** 🪟
**Description** : Script d'installation automatique pour Windows
**Fonctionnalités** :
- Vérification de Python
- Création d'environnement virtuel
- Installation des dépendances
- Vérification de l'installation
- Messages d'erreur clairs

**Utilisation** : Double-clic pour exécuter

---

### **11. `install_unix.sh` - Installation Unix/Linux/macOS** 🐧
**Description** : Script d'installation automatique pour systèmes Unix
**Fonctionnalités** :
- Vérification de Python3
- Création d'environnement virtuel
- Installation des dépendances
- Gestion des erreurs
- Instructions post-installation

**Utilisation** : `chmod +x install_unix.sh && ./install_unix.sh`

---

## 📋 **Fichiers de Configuration**

### **12. `.streamlit/config.toml` - Configuration Streamlit** ⚙️
**Description** : Configuration de l'application Streamlit
**Contenu** :
- Thème sombre avec couleurs bleues
- Optimisations de performance
- Paramètres serveur
- Configuration de sécurité

---

### **13. `requirements.txt` - Dépendances Python** 📦
**Description** : Liste complète des packages Python requis
**Catégories** :
- Streamlit et interface
- Data Science et Analytics
- Machine Learning et IA
- Géospatial et cartographie
- Utilitaires

**Installation** : `pip install -r requirements.txt`

---

### **14. `.gitignore` - Exclusion Git** 🚫
**Description** : Fichiers et dossiers exclus du versioning
**Exclusions** :
- Environnements virtuels
- Fichiers de cache
- Données sensibles
- Fichiers temporaires
- Modèles IA volumineux

---

### **15. `.gitattributes` - Attributs Git** 📝
**Description** : Configuration des types de fichiers Git
**Gestion** :
- Fichiers texte (Python, config)
- Fichiers binaires (modèles, images)
- Scripts shell
- Documents

---

## 📖 **Documentation**

### **16. `README.md` - Guide Principal** 📚
**Description** : Documentation complète du projet
**Contenu** :
- Description du projet
- Guide d'installation
- Structure du projet
- Fonctionnalités
- Dépannage

---

### **17. `PERFORMANCE_GUIDE.md` - Guide de Performance** ⚡
**Description** : Optimisations et bonnes pratiques
**Contenu** :
- Solutions de latence
- Cache et optimisation
- Scripts de préchargement
- Configuration des performances

---

### **18. `TRANSFER_GUIDE.md` - Guide de Transfert** 🔄
**Description** : Instructions pour déplacer le projet
**Contenu** :
- Méthodes de transfert
- Installation sur nouvelle machine
- Vérifications rapides
- Dépannage

---

## 🎯 **Utilisation Recommandée**

### **Première Installation**
```bash
# Windows
install_windows.bat

# macOS/Linux
chmod +x install_unix.sh
./install_unix.sh
```

### **Démarrage Optimisé**
```bash
python run_optimized.py
```

### **Démarrage Standard**
```bash
streamlit run app.py
```

### **Préchargement des Modèles**
```bash
python preload_models.py
```

---

## 🔍 **Structure des Dépendances**

### **Core Dependencies**
- **Streamlit** : Interface utilisateur
- **Pandas/NumPy** : Manipulation des données
- **FAISS** : Recherche vectorielle
- **SentenceTransformers** : Modèles d'embedding

### **Visualisation**
- **Plotly** : Graphiques interactifs
- **Folium** : Cartes géographiques
- **Matplotlib** : Graphiques statiques

### **IA et ML**
- **Transformers** : Modèles de langage
- **PyTorch** : Framework de deep learning
- **tf-keras** : Compatibilité Keras

---

## 🚀 **Workflow de Développement**

1. **Installation** : Scripts automatiques
2. **Configuration** : Fichiers `.toml` et `.env`
3. **Démarrage** : Scripts optimisés
4. **Développement** : Modification des pages
5. **Test** : Interface Streamlit
6. **Déploiement** : Transfert via Git

---

**🎉 Chaque script a un rôle spécifique et contribue à l'écosystème complet de votre dashboard énergétique intelligent !**
