import requests
import json
import os

def test_groq():
    with open("master_data.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    
    key = config["APIs_Elite_IA_Orquestracao"]["GROQ_API_KEY"]
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": "Sinalize: Sistema Operante."}],
        "max_tokens": 10
    }
    
    try:
        r = requests.post(url, headers=headers, json=payload, timeout=10)
        if r.status_code == 200:
            print(f"[+] GROQ API: {r.json()['choices'][0]['message']['content']}")
            return True
        else:
            print(f"[-] FALHA NA IA: Status {r.status_code} - {r.text}")
            return False
    except Exception as e:
        print(f"[-] ERRO DE CONEXÃO: {e}")
        return False

if __name__ == "__main__":
    test_groq()
