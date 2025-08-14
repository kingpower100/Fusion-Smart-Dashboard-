# mistral_client.py
import os, requests
from dotenv import load_dotenv
load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")

# Normaliser l'URL pour éviter des résolutions lentes de 'localhost' sous Windows
if "localhost" in OLLAMA_URL:
    OLLAMA_URL = OLLAMA_URL.replace("localhost", "127.0.0.1")

def query_mistral(prompt: str, stream: bool = False):
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": stream,
            "keep_alive": -1,
            "options": {
                "num_predict": 256,
                "num_ctx": 2048,
                "temperature": 0.2,
                "top_k": 30,
                "top_p": 0.9,
                "repeat_penalty": 1.1,
                "num_thread": max(4, os.cpu_count() // 2 or 4),
                "num_gpu": 1,
            },
        }

        # Timeout augmenté (300s) pour laisser le temps de charger/répondre
        r = requests.post(OLLAMA_URL, json=payload, stream=stream, timeout=300)
        r.raise_for_status()

        if stream:
            response_text = ""
            for line in r.iter_lines(decode_unicode=True):
                if not line:
                    continue
                try:
                    data = requests.utils.json.loads(line)
                    if "response" in data:
                        response_text += data["response"]
                except Exception:
                    continue
            return response_text
        else:
            response_data = r.json()
            if "response" in response_data:
                return response_data["response"]
            return "Erreur: Réponse invalide du modèle"

    except requests.exceptions.RequestException as e:
        return f"Erreur de connexion: {str(e)}"
    except Exception as e:
        return f"Erreur: {str(e)}"

