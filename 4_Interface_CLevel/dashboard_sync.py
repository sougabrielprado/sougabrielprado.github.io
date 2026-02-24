import os
import json
import time
import subprocess
import re

# ==========================================
# TELEMETRIA DE ELITE & SINCRONIZAÇÃO CLOUD
# ==========================================
ROOT_DIR = r"E:\4 . Engenharia\Unlock_Total"
DB_PAGAMENTOS = os.path.join(ROOT_DIR, "Logs", "pagamentos_processados.json")
DASHBOARD_PATH = os.path.join(ROOT_DIR, "4_Interface_CLevel", "dashboard.html")
PRECO_TICKET = 197.00

def obter_metricas():
    """Lê o banco de dados local e calcula a alavancagem assimétrica."""
    try:
        if os.path.exists(DB_PAGAMENTOS):
            with open(DB_PAGAMENTOS, 'r') as f:
                pagamentos = json.load(f)
            vendas = len(pagamentos)
        else:
            vendas = 0
            
        receita_total = vendas * PRECO_TICKET
        return vendas, receita_total
    except Exception as e:
        print(f"[-] Falha na leitura de dados financeiros: {e}")
        return 0, 0.0

def injetar_dados_no_dashboard(vendas, receita):
    """Reescreve o HTML do dashboard com os dados em tempo real."""
    if not os.path.exists(DASHBOARD_PATH):
        print("[-] ERRO: dashboard.html não encontrado no Kernel.")
        return

    with open(DASHBOARD_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    # Formatação de BRL (ex: 1.182,00)
    receita_str = f"R$ {receita:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    # Engenharia reversa no HTML para injeção via Regex
    html = re.sub(
        r'<h3>Receita \(24h\)</h3>\s*<div class="value">.*?</div>', 
        f'<h3>Receita (24h)</h3>\n            <div class="value">{receita_str}</div>', 
        html
    )
    
    html = re.sub(
        r'<h3>Conversão PIX</h3>\s*<div class="value">.*?</div>', 
        f'<h3>Vendas Liquidadas</h3>\n            <div class="value">{vendas}</div>', 
        html
    )

    with open(DASHBOARD_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"[+] KERNEL INJECT: HTML atualizado. Receita Mapeada: {receita_str}")

def sincronizar_entidade_cloud():
    """Força a subida do arquivo HTML atualizado para o repositório GitHub."""
    print("[+] Orquestrando Deploy para GitHub Pages...")
    os.chdir(ROOT_DIR)
    
    # Subprocessos silenciosos para interagir com o Git via Kernel
    subprocess.run(["git", "add", "4_Interface_CLevel/dashboard.html"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "commit", "-m", "chore(telemetry): Atualizacao autonoma de liquidez C-Level"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    resultado = subprocess.run(["git", "push", "origin", "main"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if resultado.returncode == 0:
        print("[+] Sincronia de Entidade Cloud concluída. iPhone atualizado.")
    else:
        print("[-] Falha na sincronia Cloud. O repositório pode estar bloqueado.")

def telemetry_loop():
    print("--- C-LEVEL TELEMETRY AGENT ONLINE | TRACKING METRICS ---")
    while True:
        vendas, receita = obter_metricas()
        injetar_dados_no_dashboard(vendas, receita)
        sincronizar_entidade_cloud()
        
        # O ciclo de atualização roda a cada 15 minutos para poupar recursos
        print("[ZzZ] Telemetria em repouso. Próxima varredura em 15m...\n")
        time.sleep(900)

if __name__ == "__main__":
    telemetry_loop()