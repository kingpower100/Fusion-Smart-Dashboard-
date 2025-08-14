"""
Script de démarrage optimisé pour réduire la latence
"""
import os
import sys
import subprocess
import time

def run_optimized_app():
    """Démarre l'application avec des optimisations de performance"""
    
    print("🚀 Démarrage optimisé de l'application...")
    
    # Vérifier si les modèles sont préchargés
    if not os.path.exists("preload_models.py"):
        print("❌ Script de préchargement non trouvé")
        return
    
    # Précharger les modèles
    print("📚 Préchargement des modèles...")
    try:
        result = subprocess.run([sys.executable, "preload_models.py"], 
                              capture_output=True, text=True, check=True)
        print("✅ Modèles préchargés avec succès")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Erreur lors du préchargement: {e}")
        print("L'application continuera mais sera plus lente au premier démarrage")
    
    # Démarrer l'application avec des optimisations
    print("🌐 Démarrage de l'application Streamlit...")
    print("💡 Utilisez Ctrl+C pour arrêter l'application")
    
    # Variables d'environnement pour optimiser les performances
    env = os.environ.copy()
    env["STREAMLIT_SERVER_HEADLESS"] = "true"
    env["STREAMLIT_SERVER_ENABLE_STATIC_SERVING"] = "true"
    env["STREAMLIT_SERVER_ENABLE_CORS"] = "false"
    env["STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION"] = "false"
    
    try:
        # Démarrer l'application
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8511",
            "--server.headless", "true",
            "--server.enableStaticServing", "true"
        ], env=env)
    except KeyboardInterrupt:
        print("\n🛑 Application arrêtée par l'utilisateur")
    except Exception as e:
        print(f"❌ Erreur lors du démarrage: {e}")

if __name__ == "__main__":
    run_optimized_app()
