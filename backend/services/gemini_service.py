import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def generar_rutina(estado, objetivo):
    prompt = f"Genera una rutina para un usuario que se siente {estado} y cuyo objetivo es {objetivo}. Devuelve un JSON con ejercicios, duración y consejos emocionales."
    res = requests.post(
        f"{API_ENDPOINT}?key={GEMINI_API_KEY}",
        json={"contents": [{"parts": [{"text": prompt}]}]}
    )
    data = res.json()
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    return text
