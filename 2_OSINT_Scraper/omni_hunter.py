import os
import json
import time
import requests

# ==========================================
# OMNI HUNTER: SEQUESTRO DE AUDIÊNCIA OSINT
# ==========================================
ROOT_DIR = r"E:\4 . Engenharia\Unlock_Total"
JSON_PATH = os.path.join(ROOT_DIR, "master_data.json")
TARGETS_DB = os.path.join(ROOT_DIR, "Logs", "high_value_targets.json")

# Carrega chaves do Kernel
with open(JSON_PATH, 'r', encoding='utf-8') as f:
    config = json.load(f)

SERPER_KEY = config.get("APIs_Elite_Growth_e_Automacao", {}).get("SERPER_DEV_KEY")
GROQ_KEY = config.get("APIs_Elite_IA_Orquestracao", {}).get("GROQ_API_KEY")

HEADERS_GROQ = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"}
HEADERS_SERPER = {'X-API-KEY': SERPER_KEY, 'Content-Type': 'application/json'}

DOMINIOS_ALVO = ["reddit.com", "linkedin.com", "twitter.com", "stackoverflow.com"]
KEYWORDS = '"bypass UAC" OR "admin rights windows 11" OR "disable smartscreen"'

def carregar_db():
    if not os.path.exists(TARGETS_DB):
        return []
    with open(TARGETS_DB, 'r') as f:
        return json.load(f)

def salvar_alvo(alvo):
    db = carregar_db()
    db.append(alvo)
    with open(TARGETS_DB, 'w') as f:
        json.dump(db, f, indent=4)

def varredura_omnichannel():
    print("[+] OSINT: Iniciando varredura global em redes de alto tráfego...")
    leads_encontrados = []
    
    for dominio in DOMINIOS_ALVO:
        query = f"site:{dominio} {KEYWORDS}"
        payload = json.dumps({"q": query, "tbs": "qdr:w"}) # Filtra apenas posts da última semana
        try:
            res = requests.post("https://google.serper.dev/search", headers=HEADERS_SERPER, data=payload)
            resultados = res.json().get('organic', [])
            leads_encontrados.extend(resultados)
        except Exception as e:
            print(f"[-] Erro ao raspar {dominio}: {e}")
            
    return leads_encontrados

def processamento_tatico_ia(lead):
    prompt = f"""Analise este lead: '{lead.get('title')} - {lead.get('snippet')}'.
1. Dê um Score de 0 a 100 baseado na urgência da dor (ex: servidor parado = 100, curiosidade = 20).
2. Escreva uma copy de DM de 2 linhas, fria e pragmática, oferecendo o protocolo 'Unlock_Total' por R$ 197.
Responda no formato: SCORE: [numero] | COPY: [texto]"""
    
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "system", "content": "Você é um especialista em Growth Hacking e Engenharia Social."},
                     {"role": "user", "content": prompt}]
    }
    try:
        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=HEADERS_GROQ, json=payload)
        return res.json()['choices'][0]['message']['content']
    except:
        return "SCORE: 50 | COPY: Acesse a infraestrutura Unlock_Total para resolver este bloqueio instantaneamente."

def hunter_loop():
    print("--- OMNI HUNTER V1.0 | RASTREIO E INTERCEPÇÃO ---")
    while True:
        alvos_brutos = varredura_omnichannel()
        db_atual = [t['link'] for t in carregar_db()]
        
        for alvo in alvos_brutos:
            link = alvo.get('link')
            if link not in db_atual:
                print(f"\n[ALVO IDENTIFICADO] {alvo.get('title')}")
                analise = processamento_tatico_ia(alvo)
                print(f"[IA TÁTICA] {analise}")
                
                if "SCORE: 8" in analise or "SCORE: 9" in analise or "SCORE: 100" in analise:
                    print("[!] ALVO HIGH-TICKET. Salvando no banco de dados de intercepção...")
                    salvar_alvo({"titulo": alvo.get('title'), "link": link, "analise": analise})
                
                time.sleep(4) # Rate limit do Groq
                
        print("\n[ZzZ] Varredura finalizada. Ocultando rastros e aguardando 2 horas...")
        time.sleep(7200)

if __name__ == "__main__":
    hunter_loop()
