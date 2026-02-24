import json
import requests

def validar_ia():
    try:
        with open('master_data.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        key = config['APIs_Elite_IA_Orquestracao']['GROQ_API_KEY']
        
        # UPGRADE: Migrando para Llama-3.3-70b-versatile (O padrão de 2026)
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama-3.3-70b-versatile", 
            "messages": [{"role": "user", "content": "Sinalize: Sistema Operante e modelo atualizado."}],
            "temperature": 0.5,
            "max_tokens": 30
        }

        r = requests.post(url, headers=headers, json=data, timeout=15)
        
        if r.status_code == 200:
            resposta = r.json()['choices'][0]['message']['content']
            print(f"\033[92m[+] SUCESSO: {resposta}\033[0m")
        else:
            print(f"\033[91m[-] ERRO {r.status_code}: {r.text}\033[0m")
            
    except Exception as e:
        print(f"\033[91m[-] ERRO NO KERNEL: {e}\033[0m")

if __name__ == "__main__":
    validar_ia()