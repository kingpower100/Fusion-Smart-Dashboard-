# 🚀 `app.py` - Application Principale - Fusion Smart Dashboard

## 📋 **Vue d'Ensemble**

**`app.py`** est le cœur de votre dashboard énergétique intelligent. Ce fichier central orchestre toutes les fonctionnalités et gère l'interface utilisateur Streamlit.

## 🎯 **Fonctionnalités Principales**

### **Interface Utilisateur**
- ✅ **Navigation intuitive** avec sidebar personnalisée
- ✅ **Thème sombre** avec couleurs bleues
- ✅ **Responsive design** pour tous les écrans
- ✅ **Navigation automatique** masquée

### **Pages Intégrées**
1. **🏠 Accueil** - Vue d'ensemble avec météo en temps réel
2. **🗺️ Carte CO₂** - Visualisation géographique interactive
3. **📊 Recommandations** - Conseils IA basés sur les données
4. **🧠 Simulateur Bayésien** - Modélisation probabiliste
5. **🤖 Simulateur Multi-Agents** - Simulation comportementale
6. **💬 Assistant IA** - Chat intelligent spécialisé énergie

## 🔧 **Architecture Technique**

### **Structure du Code**
```python
# 1. Configuration et Imports
import streamlit as st
# ... autres imports

# 2. Configuration de la Page
st.set_page_config(...)

# 3. Styles CSS Personnalisés
hide_pages_style = """..."""

# 4. Navigation Sidebar
st.sidebar.radio(...)

# 5. Gestion des Pages
if page == "🏠 Accueil":
    # Logique de la page Accueil
elif page == "🗺️ Carte CO₂":
    # Logique de la page Carte
# ... etc
```

### **Gestion des Sessions**
- **`st.session_state`** pour la persistance des données
- **Cache intelligent** pour les modèles IA
- **Gestion des erreurs** robuste

## 🌐 **Intégration des Composants**

### **Pages Importées**
```python
from pages.map_co2 import show_map_co2
from pages.campus_energy_network_graph import show_energy_network_graph
from pages.recommandations import show_energy_recommendations
from pages.simulateur_bayesien import simulateur_bayesien
from pages.simulateur_multi_agents import simulateur_multi_agents
```

### **Assistant IA Intégré**
```python
elif page == "💬 Assistant IA":
    from energy_assistant_wrapper import run_energy_assistant_wrapper
    run_energy_assistant_wrapper()
```

## 🎨 **Personnalisation de l'Interface**

### **Thème Sombre**
- **Couleurs principales** : Bleus (#1f77b4, #205f86, #181745)
- **Texte** : Blanc (#ffffffff)
- **Police** : Sans-serif

### **CSS Personnalisé**
```css
/* Masquer la navigation automatique de Streamlit */
section[data-testid="stSidebarNav"] {display: none;}

/* Masquer la barre de recherche et suggestions */
.stSearchBox {display: none;}

/* Masquer le header et footer automatiques */
header[data-testid="stHeader"] {display: none;}
footer {visibility: hidden;}
```

## 📊 **Gestion des Données**

### **Météo en Temps Réel**
- **API** : Open-Meteo
- **Localisation** : IIT Delhi (28.5450, 77.2732)
- **Données** : Température, humidité, radiation, vent
- **Mise à jour** : Automatique

### **Intégration des Données**
- **CSV** : Données énergétiques
- **PDF** : Rapports et documents
- **FAISS** : Index vectoriels pour la recherche

## 🚀 **Optimisations de Performance**

### **Cache Streamlit**
- **`@st.cache_resource`** pour les ressources lourdes
- **TTL** : 1 heure pour les modèles
- **Gestion intelligente** des sessions

### **Chargement Conditionnel**
- **Modèles IA** : Chargés à la demande
- **Pages** : Importées dynamiquement
- **Ressources** : Mises en cache automatiquement

## 🔍 **Dépannage et Maintenance**

### **Erreurs Courantes**
1. **`st.set_page_config()` must be first**
   - Solution : Vérifier l'ordre des commandes Streamlit

2. **Module not found**
   - Solution : Vérifier les chemins d'import

3. **Port déjà utilisé**
   - Solution : Changer le port avec `--server.port`

### **Logs et Debug**
```bash
# Mode debug
streamlit run app.py --logger.level debug

# Port personnalisé
streamlit run app.py --server.port 8080

# Headless mode
streamlit run app.py --server.headless true
```

## 📱 **Compatibilité**

### **Navigateurs Supportés**
- ✅ **Chrome** 90+
- ✅ **Firefox** 88+
- ✅ **Edge** 90+
- ✅ **Safari** 14+

### **Systèmes d'Exploitation**
- ✅ **Windows** 10/11
- ✅ **macOS** 10.15+
- ✅ **Linux** Ubuntu 18.04+

## 🎯 **Utilisation**

### **Démarrage Standard**
```bash
streamlit run app.py
```

### **Démarrage avec Port Personnalisé**
```bash
streamlit run app.py --server.port 8080
```

### **Démarrage Optimisé**
```bash
python run_optimized.py
```

## 🔧 **Configuration Avancée**

### **Variables d'Environnement**
```bash
# Créer un fichier .env
STREAMLIT_SERVER_PORT=8510
STREAMLIT_SERVER_HEADLESS=false
STREAMLIT_THEME_BASE=dark
```

### **Fichier de Configuration**
```toml
# .streamlit/config.toml
[server]
maxUploadSize = 200
enableXsrfProtection = false

[theme]
base = "dark"
primaryColor = "#1f77b4"
```

## 📈 **Métriques de Performance**

### **Temps de Chargement**
- **Premier démarrage** : ~6.8s (modèles IA)
- **Démarrages suivants** : ~0.1s (cache)
- **Navigation entre pages** : <0.1s

### **Utilisation des Ressources**
- **Mémoire** : Optimisée avec cache
- **CPU** : Utilisation minimale
- **Stockage** : Cache intelligent

## 🚀 **Développement et Extension**

### **Ajouter une Nouvelle Page**
1. **Créer** le fichier dans `pages/`
2. **Importer** dans `app.py`
3. **Ajouter** dans la navigation sidebar
4. **Tester** l'intégration

### **Modifier le Thème**
1. **Éditer** `.streamlit/config.toml`
2. **Modifier** le CSS dans `hide_pages_style`
3. **Redémarrer** l'application

## 🎉 **Résumé**

**`app.py`** est votre **hub central** qui :
- 🎯 **Orchestre** toutes les fonctionnalités
- 🎨 **Gère** l'interface utilisateur
- 🔧 **Intègre** tous les composants
- ⚡ **Optimise** les performances
- 🚀 **Facilite** le développement

**C'est le point d'entrée principal de votre dashboard énergétique intelligent !** 🚀✨
