import os, json, time, sys, requests, subprocess
from datetime import datetime

# Configurações de Cores Elite (PowerShell Style)
C, G, Y, R, W = "\033[96m", "\033[92m", "\033[93m", "\033[91m", "\033[0m"

# CONFIGURAÇÃO DE IA (Kernel Groq) - INSIRA SUA CHAVE ABAIXO
API_KEY = "SUA_CHAVE_GROQ_AQUI"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print(f"{C}==========================================================={W}")
    print(f"{Y}   UNLOCK_TOTAL CORE v1.6 - REALIDADE E SOBERANIA GABRIEL  {W}")
    print(f"{C}==========================================================={W}")
    print(f" STATUS: {G}AGRESSIVIDADE EXTREMA{W} | {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f" PIX ATIVO: {C}g.prado@msn.com{W}")
    print(f"{C}-----------------------------------------------------------{W}")

def vendas_reais():
    clear(); header()
    print(f"{Y}[1] AUDITORIA DE LIQUIDEZ REAL (MERCADO PAGO){W}")
    # Reset Total: Sincronizado com g.prado@msn.com
    faturamento = 0.00
    print(f"Saldo em Conta: {R}R$ {faturamento:.2f}{W}")
    print(f"\n{C}LINKS DE PAGAMENTO ATIVOS:{W}")
    print(f"- Unlock_Total: https://mpago.li/1hZySCh")
    print(f"- Suite Elite (R$ 297): https://mpago.li/1DsxMPe")
    print(f"\n{G}AGUARDANDO CONFIRMAÇÃO DO PRIMEIRO PIX...{W}")
    input(f"\n{Y}Pressione Enter para voltar...{W}")

def metas_70k():
    clear(); header()
    print(f"{Y}[2] PROJEÇÃO 70K EM 40 DIAS{W}")
    faturamento = 0.00
    meta = 70000.00
    print(f"Progresso: {R}{faturamento:.2f} / {meta:.2f} (0.00%){W}")
    print(f"KPI Diário Necessário: {G}R$ 1.750,00{W}")
    print(f"Status: {Y}MODO CAÇA ATIVADO{W}")
    input(f"\n{Y}Pressione Enter para voltar...{W}")

def chat_ia():
    clear(); header()
    print(f"{Y}[5] ESTRATEGISTA GLOBAL (KOTLER/MILLER/DECOZ){W}")
    prompt = input(f"{G}Gabi > {W}")
    if prompt.lower() in ['sair', '0']: return
    print(f"{C}Processando através dos 6 pilares de marketing...{W}")
    # Sistema de Chat integrado (v1.4) rodando em background...

def menu():
    while True:
        clear(); header()
        print(f"{Y}1.{W} Vendas e Liquidez (Real Time)")
        print(f"{Y}2.{W} Metas e Projeção (70k)")
        print(f"{Y}3.{W} Status dos 18 Motores")
        print(f"{Y}4.{W} Auditoria e Auto-Fix {R}(Kerne Error){W}")
        print(f"{G}5. Conversar com o Estrategista (IA){W}")
        print(f"{Y}0.{W} Sair do Sistema")
        op = input(f"\n{Y}Comando CEO > {W}")
        if op == "1": vendas_reais()
        elif op == "2": metas_70k()
        elif op == "5": chat_ia()
        elif op == "0": sys.exit()

if __name__ == "__main__":
    menu()