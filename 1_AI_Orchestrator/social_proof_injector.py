import os
import json
import time
import requests
from PIL import Image, ImageDraw, ImageFont

# ==========================================
# INJEÇÃO DE PROVA SOCIAL: AUTOMAÇÃO ELITE
# ==========================================
ROOT_DIR = r"E:\4 . Engenharia\Unlock_Total"
DB_PAGAMENTOS = os.path.join(ROOT_DIR, "Logs", "pagamentos_processados.json")
MASTER_DATA = os.path.join(ROOT_DIR, "master_data.json")

# Cores de Poder
NAVY = (10, 25, 47)
GOLD = (212, 175, 55)
WHITE = (230, 241, 255)

with open(MASTER_DATA, 'r', encoding='utf-8') as f:
    config = json.load(f)

# Nota: Adicione 'IG_ACCESS_TOKEN' e 'IG_USER_ID' ao seu master_data.json no painel Meta for Developers
ACCESS_TOKEN = config.get("Engenharia_Financeira", {}).get("IG_ACCESS_TOKEN", "SUBSTITUIR_NO_JSON")
IG_USER_ID = config.get("Engenharia_Financeira", {}).get("IG_USER_ID", "SUBSTITUIR_NO_JSON")

def criar_card_venda(valor, id_transacao):
    """Gera imagem premium de prova social via Pillow (Open-Source)"""
    img = Image.new('RGB', (1080, 1080), color=NAVY)
    draw = ImageDraw.Draw(img)
    
    # Borda Dourada de Elite
    draw.rectangle([20, 20, 1060, 1060], outline=GOLD, width=15)
    
    # Texto Tático
    try:
        font_title = ImageFont.truetype("arial.ttf", 80)
        font_value = ImageFont.truetype("arial.ttf", 150)
    except:
        font_title = ImageFont.load_default()
        font_value = ImageFont.load_default()

    draw.text((540, 300), "VENDA CONFIRMADA", fill=GOLD, font=font_title, anchor="mm")
    draw.text((540, 500), f"R$ {valor}", fill=WHITE, font=font_value, anchor="mm")
    draw.text((540, 700), "Protocolo Unlock_Total", fill=GOLD, font=font_title, anchor="mm")
    draw.text((540, 900), f"ID: {id_transacao}", fill=WHITE, font=ImageFont.truetype("arial.ttf", 40), anchor="mm")

    path_img = os.path.join(ROOT_DIR, "Logs", f"venda_{id_transacao}.png")
    img.save(path_img)
    return path_img

def postar_instagram(image_path, caption):
    """Publica a prova social via Instagram Graph API"""
    if ACCESS_TOKEN == "SUBSTITUIR_NO_JSON": return
    
    # 1. Upload da imagem (requer URL pública - use o link do seu GitHub Pages)
    image_url = f"https://sougabrielprado.github.io/Unlock_Total/Logs/{os.path.basename(image_path)}"
    post_url = f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media"
    payload = {'image_url': image_url, 'caption': caption, 'access_token': ACCESS_TOKEN}
    
    r = requests.post(post_url, data=payload)
    if r.status_code == 200:
        creation_id = r.json().get('id')
        publish_url = f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media_publish"
        requests.post(publish_url, data={'creation_id': creation_id, 'access_token': ACCESS_TOKEN})
        print("[+] PROVA SOCIAL: Publicado no Instagram com sucesso.")

def social_proof_loop():
    print("--- SOCIAL PROOF AGENT ONLINE | ESCALANDO AUTORIDADE ---")
    processados_social = []
    
    while True:
        if os.path.exists(DB_PAGAMENTOS):
            with open(DB_PAGAMENTOS, 'r') as f:
                pagamentos = json.load(f)
            
            for pay_id in pagamentos:
                if pay_id not in processados_social:
                    print(f"[!] Identificada nova venda para Prova Social: {pay_id}")
                    path = criar_card_venda("197,00", pay_id)
                    postar_instagram(path, f"Mais um acesso liberado ao Protocolo Unlock_Total. Tecnologia de elite e liberdade de Kernel. #IA #Growth #GabrielPrado")
                    processados_social.append(pay_id)
        
        time.sleep(3600) # Verifica a cada hora

if __name__ == "__main__":
    social_proof_loop()
