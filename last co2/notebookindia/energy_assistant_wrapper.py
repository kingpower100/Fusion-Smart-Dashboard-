"""
Energy Assistant Wrapper
This file handles the import and execution of the energy assistant
"""
import os
import sys
import importlib.util
import streamlit as st

def run_energy_assistant_wrapper():
    """Wrapper function to run the energy assistant with proper dependency handling"""
    
    try:
        # Get the path to the energy-assistant project
        current_dir = os.path.dirname(__file__)
        energy_assistant_path = os.path.abspath(os.path.join(current_dir, "..", "..", "energy-assistant"))
        energy_assistant_app_path = os.path.join(energy_assistant_path, "app")
        
        # Add both paths to Python path
        if energy_assistant_path not in sys.path:
            sys.path.insert(0, energy_assistant_path)
        if energy_assistant_app_path not in sys.path:
            sys.path.insert(0, energy_assistant_app_path)
        
        # Check if the main file exists
        main_file_path = os.path.join(energy_assistant_app_path, "main.py")
        if not os.path.exists(main_file_path):
            st.error(f"❌ Fichier energy-assistant introuvable : {main_file_path}")
            st.info("💡 Vérifiez que le projet energy-assistant existe et contient le fichier app/main.py")
            return
        
        # Set environment variables for correct file paths
        os.environ["FAISS_INDEX"] = os.path.join(energy_assistant_path, "rag", "faiss_index", "index_all.faiss")
        os.environ["CHUNKS_PATH"] = os.path.join(energy_assistant_path, "rag", "faiss_index", "chunks_all.txt")
        os.environ["META_PATH"] = os.path.join(energy_assistant_path, "rag", "faiss_index", "metadata_all.json")
        os.environ["FAISS_INDEX_PDF"] = os.path.join(energy_assistant_path, "rag", "faiss_index", "index_pdf.faiss")
        os.environ["FAISS_INDEX_PDF_PATH"] = os.path.join(energy_assistant_path, "rag", "faiss_index", "chunks_pdf.txt")
        
        # Import the module
        spec = importlib.util.spec_from_file_location("energy_assistant_main", main_file_path)
        energy_assistant_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(energy_assistant_module)
        
        # Run the energy assistant
        energy_assistant_module.run_energy_assistant()
        
    except ImportError as e:
        st.error(f"❌ Erreur d'importation de l'assistant IA: {str(e)}")
        st.info("💡 Assurez-vous que le projet energy-assistant est accessible depuis ce répertoire.")
        st.info(f"💡 Erreur détaillée : {str(e)}")
    except Exception as e:
        st.error(f"❌ Erreur lors de l'exécution de l'assistant IA: {str(e)}")
        st.exception(e)
