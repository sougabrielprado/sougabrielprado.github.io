import hashlib
import json
import os
import time
import requests

# ==========================================
# MÓDULO 13: META CONVERSIONS API (CAPI)
# ==========================================
ROOT_DIR = r"E:\4 . Engenharia\Unlock_Total"
MASTER_DATA = os.path.join(ROOT_DIR, "master_data.json")
DB_PAGAMENTOS = os.path.join(ROOT_DIR, "Logs", "pagamentos_processados.json")

def hash_data(data):
    return hashlib.sha256(data.lower().strip().encode('utf-8')).hexdigest()

def enviar_evento_meta(valor, email_cliente, order_id):
    with open(MASTER_DATA, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Chaves necessárias (Adicionar ao master_data.json)
    pixel_id = config.get("Engenharia_Financeira", {}).get("FB_PIXEL_ID")
    access_token = config.get("Engenharia_Financeira", {}).get("FB_ACCESS_TOKEN")
    
    if not pixel_id or not access_token:
        print("[-] ERRO: FB_PIXEL_ID ou FB_ACCESS_TOKEN não encontrados no Master Data.")
        return

    url = f"https://graph.facebook.com/v18.0/{pixel_id}/events"
    
    payload = {
        "data": [{
            "event_name": "Purchase",
            "event_time": int(time.time()),
            "action_source": "system_generated",
            "user_data": {
                "em": [hash_data(email_cliente)],
                "client_ip_address": "127.0.0.1", # Kernel Local
                "client_user_agent": "Unlock_Total_CAPI_v1"
            },
            "custom_data": {
                "currency": "BRL",
                "value": valor,
                "order_id": order_id
            }
        }],
        "access_token": access_token
    }

    try:
        r = requests.post(url, json=payload)
        if r.status_code == 200:
            print(f"[+] CAPI: Compra de R$ {valor} reportada ao algoritmo do Meta.")
        else:
            print(f"[-] CAPI FAIL: {r.text}")
    except Exception as e:
        print(f"[-] Erro de conexão CAPI: {e}")

def capi_loop():
    print("--- META CONVERSIONS API MONITOR ONLINE ---")
    enviados_capi = []
    
    while True:
        if os.path.exists(DB_PAGAMENTOS):
            try:
                with open(DB_PAGAMENTOS, 'r') as f:
                    pagamentos = json.load(f)
                
                for pay_id in pagamentos:
                    if pay_id not in enviados_capi:
                        # Aqui extraímos o e-mail do cliente do DB ou usamos o seu como fallback
                        enviar_evento_meta(197.00, "cliente_exemplo@gmail.com", pay_id)
                        enviados_capi.append(pay_id)
            except: pass
            
        time.sleep(300) # Checa a cada 5 minutos

if __name__ == "__main__":
    capi_loop()
