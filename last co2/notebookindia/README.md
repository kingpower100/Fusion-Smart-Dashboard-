# 🚀 Fusion Smart Dashboard - Guide d'Installation

## 📋 **Description du Projet**

**Fusion Smart** est un tableau de bord énergétique intelligent qui combine :
- 📊 **Visualisations énergétiques** avancées
- 🗺️ **Cartographie CO₂** interactive
- 🧠 **Simulateurs bayésiens** et multi-agents
- 🤖 **Assistant IA spécialisé** en énergie (RAG + Mistral)
- 📈 **Recommandations** basées sur l'IA

## 🖥️ **Prérequis Système**

### **Système d'Exploitation**
- ✅ **Windows 10/11** (testé)
- ✅ **macOS 10.15+** (compatible)
- ✅ **Ubuntu 18.04+** (compatible)

### **Python**
- **Version** : Python 3.8 - 3.12 (recommandé : 3.11)
- **Pip** : Version 20.0+

### **Mémoire RAM**
- **Minimum** : 8 GB
- **Recommandé** : 16 GB+

### **Espace Disque**
- **Minimum** : 5 GB
- **Recommandé** : 10 GB+

## 📦 **Installation**

### **1. Cloner le Projet**
```bash
# Cloner le repository
git clone [URL_DU_REPO]
cd "last co2/notebookindia"

# OU copier manuellement le dossier
# Copier le dossier "last co2" vers la nouvelle machine
```

### **2. Créer l'Environnement Virtuel**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3. Installer les Dépendances**
```bash
# Mettre à jour pip
pip install --upgrade pip

# Installer les packages requis
pip install -r requirements.txt

# Si requirements.txt n'existe pas, installer manuellement :
pip install streamlit pandas numpy matplotlib plotly pillow
pip install faiss-cpu sentence-transformers python-dotenv
pip install streamlit-folium geopandas folium
pip install pytz requests
pip install tf-keras  # Pour la compatibilité Keras
```

### **4. Vérifier l'Installation**
```bash
# Tester Streamlit
streamlit --version

# Tester les imports Python
python -c "import streamlit, pandas, numpy, faiss; print('✅ Tous les packages sont installés!')"
```

## 🗂️ **Structure du Projet**

```
last co2/
├── notebookindia/
│   ├── app.py                    # Application principale
│   ├── energy_assistant_wrapper.py # Wrapper pour l'Assistant IA
│   ├── preload_models.py         # Script de préchargement
│   ├── run_optimized.py          # Démarrage optimisé
│   ├── requirements.txt           # Dépendances Python
│   ├── README.md                 # Ce fichier
│   ├── .streamlit/
│   │   └── config.toml          # Configuration Streamlit
│   ├── pages/                    # Pages du dashboard
│   │   ├── map_co2.py           # Carte CO₂
│   │   ├── campus_energy_network_graph.py
│   │   ├── recommandations.py   # Recommandations IA
│   │   ├── simulateur_bayesien.py
│   │   └── simulateur_multi_agents.py
│   ├── assets/                   # Ressources (CSS, images)
│   └── data/                     # Données du projet
└── energy-assistant/             # Module Assistant IA
    ├── app/
    │   ├── main.py               # Assistant IA principal
    │   ├── mistral_client.py     # Client Mistral
    │   └── prompt_builder.py     # Construction des prompts
    └── rag/
        └── faiss_index/          # Index FAISS pour la recherche

## 📚 **Notebooks Target - Analyse Énergétique**

### **🎯 TARGET 3 : Classification des Usages Énergétiques**
**Objectif** : Classifier les usages énergétiques selon les profils utilisateurs

**Description** : Dans le cadre de l'optimisation énergétique du campus de l'IIIT Delhi, l'objectif est de **classifier les usages énergétiques** des bâtiments en fonction des différents profils d'occupation :
- **Étudiants** : Consommation pendant les heures de cours
- **Personnel administratif et technique** : Usage pendant les heures de bureau
- **Week-ends et périodes de faible activité** : Consommation minimale
- **Événements spéciaux** : Pic de consommation exceptionnel

Cette classification permettra d'identifier les comportements de consommation propres à chaque profil et de mettre en place des stratégies ciblées de réduction et d'optimisation énergétique.

---

### **🎯 TARGET 2 : Détection de Surconsommation Énergétique**
**Objectif** : Détecter des situations de **surconsommation énergétique cachée**

**Description** : Exploitation de modèles d'apprentissage non supervisé pour identifier des anomalies :
- ✅ **Isolation Forest** : Pour identifier des anomalies isolées dans les données de consommation
- ✅ **DBSCAN** : Pour repérer des regroupements inhabituels indiquant des comportements anormaux
- **Analyse des patterns** : Détection de dérives énergétiques
- **Alertes automatiques** : Notification des surconsommations détectées

---

### **🎯 TARGET 1 : Évaluation Intelligente de l'Empreinte Carbone**
**Objectif** : Modéliser et prévoir l'évolution de l'empreinte carbone

**Description** : Développement d'un système capable de **modéliser et prévoir l'évolution de l'empreinte carbone** d'un bâtiment d'entreprise à partir de :
- **Usages énergétiques** : Consommation d'électricité, chauffage, refroidissement, etc.
- **Conditions climatiques** : Température, humidité, ensoleillement, précipitations, etc.
- **Données contextuelles** : Taux d'occupation, calendrier, événements spéciaux

**Technologies utilisées** :
- **Machine Learning** : Modèles prédictifs avancés
- **Analyse temporelle** : Séquences temporelles et saisonnalité
- **Intégration multi-sources** : Fusion de données hétérogènes
- **Prédictions en temps réel** : Mise à jour continue des modèles

## 🚀 **Démarrage de l'Application**

### **Option 1 : Démarrage Optimisé (Recommandé)**
```bash
# Précharger les modèles IA et démarrer avec optimisations
python run_optimized.py
```
- **Port** : 8511
- **URL** : http://localhost:8511
- **Avantages** : Performance maximale, modèles préchargés

### **Option 2 : Démarrage Standard**
```bash
# Démarrage normal
streamlit run app.py --server.port 8510
```
- **Port** : 8510
- **URL** : http://localhost:8510
- **Avantages** : Simple, modèles chargés à la demande

### **Option 3 : Démarrage avec Port Personnalisé**
```bash
# Choisir un port spécifique
streamlit run app.py --server.port 8080
```

## 🔧 **Configuration**

### **Fichier de Configuration Streamlit**
Le fichier `.streamlit/config.toml` contient :
- **Thème sombre** avec couleurs bleues
- **Optimisations de performance**
- **Paramètres serveur**

### **Variables d'Environnement (Optionnel)**
```bash
# Créer un fichier .env
EMB_MODEL=sentence-transformers/all-MiniLM-L6-v2
FAISS_INDEX=rag/faiss_index/index_all.faiss
CHUNKS_PATH=rag/faiss_index/chunks_all.txt
META_PATH=rag/faiss_index/metadata_all.json
```

## 🌐 **Accès à l'Application**

### **Local**
- **URL** : http://localhost:8511 (optimisé) ou http://localhost:8510 (standard)
- **Navigateur** : Chrome, Firefox, Edge, Safari

### **Réseau Local**
- **URL** : http://[VOTRE_IP]:8511
- **Trouver votre IP** :
  - **Windows** : `ipconfig`
  - **macOS/Linux** : `ifconfig` ou `ip addr`

## 🎯 **Fonctionnalités Principales**

### **🏠 Accueil**
- Météo en temps réel (IIT Delhi)
- Vue d'ensemble du dashboard

### **🗺️ Carte CO₂**
- Visualisation géographique des émissions
- Données interactives

### **📊 Recommandations**
- Conseils énergétiques basés sur l'IA
- Analyse des données

### **🧠 Simulateur Bayésien**
- Modélisation probabiliste
- Prédictions énergétiques

### **🤖 Simulateur Multi-Agents**
- Simulation de systèmes complexes
- Analyse comportementale

### **💬 Assistant IA**
- Chat intelligent spécialisé énergie
- RAG (Retrieval-Augmented Generation)
- Modèle Mistral intégré

## 🚨 **Dépannage**

### **Erreur : "No module named 'faiss'"**
```bash
pip install faiss-cpu
```

### **Erreur : "Keras 3 not supported"**
```bash
pip install tf-keras
```

### **Erreur : "set_page_config() must be first"**
- Vérifiez que `st.set_page_config()` est la première commande Streamlit
- Redémarrez l'application

### **Performance Lente**
```bash
# Précharger les modèles
python preload_models.py

# Puis démarrer optimisé
python run_optimized.py
```

### **Port Déjà Utilisé**
```bash
# Changer le port
streamlit run app.py --server.port 8080
```

## 📱 **Compatibilité Navigateur**

- ✅ **Chrome** 90+
- ✅ **Firefox** 88+
- ✅ **Edge** 90+
- ✅ **Safari** 14+

## 🔒 **Sécurité**

- **Ports** : 8510, 8511 (modifiables)
- **Accès** : Local uniquement par défaut
- **Données** : Stockées localement

## 📞 **Support**

### **Logs d'Erreur**
```bash
# Voir les logs en temps réel
streamlit run app.py --logger.level debug
```

### **Vérification des Dépendances**
```bash
# Liste des packages installés
pip list

# Vérifier les versions
python -c "import streamlit; print(streamlit.__version__)"
```

## 🎉 **Félicitations !**

Votre **Fusion Smart Dashboard** est maintenant prêt ! 

**Prochaines étapes :**
1. 🌐 Ouvrir http://localhost:8511 dans votre navigateur
2. 🎨 Personnaliser le thème si nécessaire
3. 📊 Explorer toutes les fonctionnalités
4. 🤖 Tester l'Assistant IA

**Bonne exploration !** 🚀✨
#   F u s i o n - S m a r t - D a s h b o a r d - 
 
 