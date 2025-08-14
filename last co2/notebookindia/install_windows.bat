@echo off
echo ========================================
echo 🚀 Fusion Smart Dashboard - Installation
echo ========================================
echo.

echo 📋 Vérification de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installé ou pas dans le PATH
    echo 💡 Installez Python depuis https://python.org
    pause
    exit /b 1
)

echo ✅ Python détecté
python --version

echo.
echo 🔧 Création de l'environnement virtuel...
python -m venv venv
if errorlevel 1 (
    echo ❌ Erreur lors de la création de l'environnement virtuel
    pause
    exit /b 1
)

echo ✅ Environnement virtuel créé

echo.
echo 🚀 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

echo.
echo 📦 Mise à jour de pip...
python -m pip install --upgrade pip

echo.
echo 📚 Installation des dépendances...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Erreur lors de l'installation des dépendances
    echo 💡 Vérifiez votre connexion internet et réessayez
    pause
    exit /b 1
)

echo.
echo 🎯 Vérification de l'installation...
python -c "import streamlit, pandas, numpy, faiss; print('✅ Tous les packages sont installés!')"

if errorlevel 1 (
    echo ❌ Erreur lors de la vérification
    pause
    exit /b 1
)

echo.
echo 🎉 Installation terminée avec succès !
echo.
echo 🚀 Pour démarrer l'application :
echo    1. python run_optimized.py    (recommandé)
echo    2. streamlit run app.py       (standard)
echo.
echo 🌐 L'application sera accessible sur :
echo    http://localhost:8511 (optimisé)
echo    http://localhost:8510 (standard)
echo.
pause
