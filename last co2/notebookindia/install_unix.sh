#!/bin/bash

echo "========================================"
echo "🚀 Fusion Smart Dashboard - Installation"
echo "========================================"
echo

echo "📋 Vérification de Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 n'est pas installé"
    echo "💡 Installez Python3 avec votre gestionnaire de paquets"
    exit 1
fi

echo "✅ Python3 détecté"
python3 --version

echo
echo "🔧 Création de l'environnement virtuel..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de la création de l'environnement virtuel"
    exit 1
fi

echo "✅ Environnement virtuel créé"

echo
echo "🚀 Activation de l'environnement virtuel..."
source venv/bin/activate

echo
echo "📦 Mise à jour de pip..."
python -m pip install --upgrade pip

echo
echo "📚 Installation des dépendances..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de l'installation des dépendances"
    echo "💡 Vérifiez votre connexion internet et réessayez"
    exit 1
fi

echo
echo "🎯 Vérification de l'installation..."
python -c "import streamlit, pandas, numpy, faiss; print('✅ Tous les packages sont installés!')"

if [ $? -ne 0 ]; then
    echo "❌ Erreur lors de la vérification"
    exit 1
fi

echo
echo "🎉 Installation terminée avec succès !"
echo
echo "🚀 Pour démarrer l'application :"
echo "   1. python run_optimized.py    (recommandé)"
echo "   2. streamlit run app.py       (standard)"
echo
echo "🌐 L'application sera accessible sur :"
echo "   http://localhost:8511 (optimisé)"
echo "   http://localhost:8510 (standard)"
echo
echo "💡 N'oubliez pas d'activer l'environnement virtuel :"
echo "   source venv/bin/activate"
echo
