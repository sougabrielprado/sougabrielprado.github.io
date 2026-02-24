import requests, time, json, os
MP_TOKEN = "APP_USR-2422865585047382-022323-75e3c45da6ab12e058d32c22969101bc-69041119"
def check_liquidez():
    url = "https://api.mercadopago.com/v1/payments/search"
    headers = {"Authorization": f"Bearer {MP_TOKEN}"}
    try:
        # Usando HTTPS Direto (Bypass de ICMP/Ping)
        r = requests.get(url, headers=headers, params={"status": "approved"}, timeout=30)
        return r.json().get('results', [])
    except: return []

while True:
    try:
        vendas = check_liquidez()
        if vendas: print(f"[+] Vendas detectadas: {len(vendas)}")
    except: pass
    time.sleep(300)
