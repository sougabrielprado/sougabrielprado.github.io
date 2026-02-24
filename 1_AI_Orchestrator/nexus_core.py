import os
import time
import requests
import json

# CHAVES DO MASTER_DATA.JSON
GROQ_API_KEY = "config.get("APIs_Elite_IA_Orquestracao", {}).get("GROQ_API_KEY")xpjB"
SERPER_DEV_KEY = "d96ec99d8aa1e03988be3db2cc16e81c73ec4a15"
MP_ACCESS_TOKEN = "APP_USR-8809800455203335-022323-78d3bc40d053fb1df6fe4fe139c2245c-3224354336"

HEADERS_GROQ = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
HEADERS_MP = {"Authorization": f"Bearer {MP_ACCESS_TOKEN}", "Content-Type": "application/json"}

def osint_prospect_clients():
    print("[+] OSINT: Buscando alvos vulneráveis (Reddit/Fóruns) via Serper.dev...")
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": 'site:reddit.com "bypass UAC" OR "disable smartscreen" OR "execution policy restricted"'})
    headers = {'X-API-KEY': SERPER_DEV_KEY, 'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=payload)
        return response.json().get('organic', [])
    except Exception as e:
        print(f"[-] Erro OSINT: {e}")
        return []

def dynamic_pricing_and_pitch(lead_snippet):
    prompt = f"Crie um pitch de vendas direto e pragmático de 2 linhas para um usuário com este problema: '{lead_snippet}'. O produto é o 'Unlock_Total', um protocolo de automação que remove restrições do Windows. Defina um preço em BRL entre 97 e 297 dependendo da urgência da dor."
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "system", "content": "Você é um estrategista de vendas cibernéticas implacável."}, {"role": "user", "content": prompt}]
    }
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=HEADERS_GROQ, json=payload)
        return response.json()['choices'][0]['message']['content']
    except:
        return "Acesse o protocolo Unlock_Total por R$ 197 e resolva seu bloqueio imediatamente."

def generate_payment_link(amount=197.00):
    print("[+] FINANCEIRO: Gerando checkout invisível no MercadoPago...")
    url = "https://api.mercadopago.com/checkout/preferences"
    payload = {
        "items": [{"title": "Unlock_Total Protocol", "quantity": 1, "currency_id": "BRL", "unit_price": float(amount)}],
        "back_urls": {"success": "https://sougabrielprado.github.io/Unlock_Total/success"},
        "auto_return": "approved"
    }
    try:
        response = requests.post(url, headers=HEADERS_MP, json=payload)
        return response.json().get('init_point', 'Falha ao gerar Link')
    except:
        return "Erro de Gateway MP"

def nexus_loop():
    print("--- NEXUS AGENT ONLINE | KERNEL ACTIVE ---")
    while True:
        leads = osint_prospect_clients()
        if not leads:
            print("[-] Nenhum alvo imediato encontrado. Aguardando radar...")
        
        for lead in leads[:3]:
            print(f"\n[LEAD DETECTADO]: {lead.get('title', 'N/A')}")
            pitch = dynamic_pricing_and_pitch(lead.get('snippet', ''))
            link = generate_payment_link()
            print(f"[COPY]: {pitch}")
            print(f"[PAY_LINK]: {link}")
            time.sleep(3)
        
        print("\n[ZzZ] Ciclo OSINT completo. Limpando memória e recarregando em 30 segundos...")
        time.sleep(30)

if __name__ == "__main__":
    nexus_loop()
