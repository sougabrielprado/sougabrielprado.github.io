import time
import json
import os
import requests

# ==========================================
# MÓDULO 8: RELATÓRIOS WHATSAPP (ELITE)
# ==========================================
ROOT_DIR = r"E:\4 . Engenharia\Unlock_Total"
DB_PAGAMENTOS = os.path.join(ROOT_DIR, "Logs", "pagamentos_processados.json")

# Utilizaremos o CallMeBot (API Free) para notificação instantânea
# Gabi, acesse https://www.callmebot.com/blog/free-api-whatsapp-messages/ para pegar seu apikey
WHATSAPP_PHONE = "5551984252212" # Seu número formatado
WHATSAPP_APIKEY = "123456"       # Substitua pela sua chave no master_data.json

def enviar_notificacao_lucro(pay_id):
    mensagem = f"💰 *LUCRO CONFIRMADO, GABI!*\n\n🚀 Venda: Unlock_Total\n💎 Valor: R$ 197,00\n🆔 ID: {pay_id}\n\nO milhão de Junho está chegando."
    url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_PHONE}&text={requests.utils.quote(mensagem)}&apikey={WHATSAPP_APIKEY}"
    
    try:
        requests.get(url)
        print(f"[+] WHATSAPP: Alerta de lucro enviado para o Gabi.")
    except Exception as e:
        print(f"[-] Erro ao enviar WhatsApp: {e}")

def monitor_whatsapp_loop():
    print("--- WHATSAPP PROFIT REPORTS ONLINE ---")
    enviados_whatsapp = []
    
    while True:
        if os.path.exists(DB_PAGAMENTOS):
            with open(DB_PAGAMENTOS, 'r') as f:
                pagamentos = json.load(f)
            
            for pay_id in pagamentos:
                if pay_id not in enviados_whatsapp:
                    enviar_notificacao_lucro(pay_id)
                    enviados_whatsapp.append(pay_id)
        
        time.sleep(60) # Checa a cada minuto

if __name__ == "__main__":
    monitor_whatsapp_loop()