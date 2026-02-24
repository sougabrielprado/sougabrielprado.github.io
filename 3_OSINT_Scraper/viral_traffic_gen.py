import os
import json
import time
import requests

# ==========================================
# MÓDULO 9: GERADOR DE TRÁFEGO VIRAL (IA)
# ==========================================
ROOT_DIR = r"E:\4 . Engenharia\Unlock_Total"
MASTER_DATA = os.path.join(ROOT_DIR, "master_data.json")

with open(MASTER_DATA, 'r', encoding='utf-8') as f:
    config = json.load(f)

GROQ_KEY = config.get("APIs_Elite_IA_Orquestracao", {}).get("GROQ_API_KEY")

def gerar_roteiro_viral(tema="Bypass de UAC no Windows"):
    """Usa Llama-3 para criar um roteiro de 15 segundos altamente persuasivo."""
    prompt = f"Crie um roteiro de 15 segundos para um Reels do Instagram. Tema: {tema}. O objetivo é vender o protocolo Unlock_Total. Use gatilhos de autoridade e escassez. Comece com um HOOK de dor (ex: 'Cansado de ser bloqueado pelo seu próprio PC?')."
    
    headers = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "system", "content": "Você é um mestre de roteiros virais e persuasão."},
                     {"role": "user", "content": prompt}]
    }
    
    try:
        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        return res.json()['choices'][0]['message']['content']
    except:
        return "Erro ao gerar roteiro. Use: Hook de Dor + Solução Unlock_Total + CTA Bio."

def traffic_engine_loop():
    print("--- VIRAL TRAFFIC ENGINE ONLINE | ESCALANDO O FUNIL ---")
    while True:
        roteiro = gerar_roteiro_viral()
        print(f"\n[+] NOVO ROTEIRO GERADO:\n{roteiro}")
        # Aqui integraríamos com APIs de Video Gen (ex: HeyGen/D-ID) no futuro
        print("[!] Aguardando Janela Astral de Postagem (Pico de Engajamento)...")
        time.sleep(21600) # Gera 1 roteiro estratégico a cada 6 horas

if __name__ == "__main__":
    traffic_engine_loop()
