# 🚀 Guide de Transfert Rapide - Fusion Smart Dashboard

## 📦 **Transfert du Projet**

### **Option 1 : Copie Manuelle (Recommandée)**
1. **Copier le dossier complet** `"last co2"` vers la nouvelle machine
2. **Conserver la structure** exacte des dossiers
3. **Vérifier que tous les fichiers** sont présents

### **Option 2 : Archive ZIP**
1. **Créer une archive** du dossier `"last co2"`
2. **Transférer l'archive** (USB, Cloud, Réseau)
3. **Extraire sur la nouvelle machine**

### **Option 3 : Git (Si configuré)**
```bash
git clone [URL_DU_REPO]
cd "last co2/notebookindia"
```

## 🖥️ **Installation sur Nouvelle Machine**

### **Windows**
```bash
# Double-cliquer sur
install_windows.bat

# OU manuellement
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### **macOS/Linux**
```bash
# Rendre exécutable et lancer
chmod +x install_unix.sh
./install_unix.sh

# OU manuellement
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🚀 **Démarrage Rapide**

### **Première Utilisation**
```bash
# Précharger les modèles (recommandé)
python preload_models.py

# Démarrer optimisé
python run_optimized.py
```

### **Utilisations Suivantes**
```bash
# Démarrer directement
python run_optimized.py
```

## 🔧 **Vérifications Rapides**

### **Dépendances Installées**
```bash
python -c "import streamlit, faiss, pandas; print('✅ OK')"
```

### **Structure des Fichiers**
```
✅ app.py
✅ energy_assistant_wrapper.py
✅ requirements.txt
✅ .streamlit/config.toml
✅ pages/ (dossier)
✅ energy-assistant/ (dossier)
```

## 🚨 **Problèmes Courants**

### **"No module named 'faiss'"**
```bash
pip install faiss-cpu
```

### **"Keras 3 not supported"**
```bash
pip install tf-keras
```

### **Port déjà utilisé**
```bash
streamlit run app.py --server.port 8080
```

## 🌐 **Accès**
- **URL** : http://localhost:8511
- **Navigateur** : Chrome, Firefox, Edge, Safari

## 📞 **Support**
- **README.md** : Guide complet
- **PERFORMANCE_GUIDE.md** : Optimisations
- **Logs** : Voir la console pour les erreurs

---

**🎯 Objectif : Installation en moins de 10 minutes !**

**Bonne installation !** 🚀✨
