import os, json, time, sys, requests, subprocess
from datetime import datetime

# Configurações de Cores Elite
C, G, Y, R, W = "\033[96m", "\033[92m", "\033[93m", "\033[91m", "\033[0m"

# CONFIGURAÇÃO DE IA (Insira sua chave Groq)
API_KEY = "SUA_CHAVE_GROQ_AQUI"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print(f"{C}==========================================================={W}")
    print(f"{Y}   UNLOCK_TOTAL CORE v1.3 - PROTOCOLO DE AUTOCURA (S.H.)   {W}")
    print(f"{C}==========================================================={W}")
    print(f" STATUS: {G}SISTEMA INTELIGENTE{W} | {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"{C}-----------------------------------------------------------{W}")

def auditoria_logs_com_fix():
    clear(); header()
    print(f"{Y}[4] AUDITORIA DE LOGS E AUTO-FIX{W}\n")
    log_path = "Logs/Sovereignty_Report.log"
    
    # Simulação de leitura de log real (ou leitura do arquivo se existir)
    try:
        with open(log_path, "r") as f: logs = f.readlines()[-5:]
    except:
        logs = ["[ERRO] Módulo 12: Falha na sincronia de lances de tráfego.\n", 
                "[ERRO] Módulo 18: Conexão recusada pela API de Vendas.\n"]
    
    for log in logs: print(f"{R}{log.strip()}{W}")
    
    print(f"\n{Y}[F] Solicitar AUTO-FIX da IA para estes erros{W}")
    print(f"{C}[ENTER] Voltar ao Menu{W}")
    
    choice = input("\nComando > ").lower()
    if choice == 'f':
        executar_autofix(logs)

def executar_autofix(logs_error):
    print(f"\n{Y}IA Analisando logs e gerando script de reparo...{W}")
    
    prompt_fix = (
        f"Analise estes logs de erro do sistema Unlock_Total: {logs_error}. "
        "Gere APENAS o código (PowerShell ou Python) necessário para corrigir esses problemas. "
        "Não dê explicações. Retorne o código limpo."
    )
    
    try:
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        data = {
            "model": "llama3-70b-8192",
            "messages": [{"role": "system", "content": "Você é um Engenheiro Sênior de Elite. Retorne apenas código funcional."},
                         {"role": "user", "content": prompt_fix}]
        }
        response = requests.post(API_URL, json=data, headers=headers)
        fix_code = response.json()['choices'][0]['message']['content'].strip('`').replace('powershell', '').strip()
        
        print(f"\n{G}SOLUÇÃO PROPOSTA PELA IA:{W}\n")
        print(f"{C}{fix_code}{W}\n")
        
        confirm = input(f"{Y}Deseja executar este comando de reparo agora? (S/N): {W}").lower()
        if confirm == 's':
            print(f"{G}Executando reparo...{W}")
            # Detecta se é PowerShell ou Python simples
            if "Get-" in fix_code or "Set-" in fix_code or "$" in fix_code:
                subprocess.run(["powershell", "-Command", fix_code], shell=True)
            else:
                exec(fix_code)
            print(f"\n{G}[OK] Reparo aplicado com sucesso.{W}")
            time.sleep(2)
    except:
        print(f"{R}Erro ao conectar com o Kernel de Autocura.{W}")
        time.sleep(2)

# ... (Mantenha as funções vendas_detalhadas, metas_expansao e chat_estrategista da v1.2)

def menu():
    while True:
        clear(); header()
        print(f"{Y}1.{W} Vendas e Liquidez")
        print(f"{Y}2.{W} Metas e Projeção")
        print(f"{Y}3.{W} Status dos Motores")
        print(f"{Y}4.{W} Auditoria de Logs {R}(AUTO-FIX){W}")
        print(f"{G}5. Conversar com o Estrategista (IA){W}")
        print(f"{Y}0.{W} Sair")
        op = input(f"\n{Y}Comando CEO > {W}")
        if op == "4": auditoria_logs_com_fix()
        elif op == "0": sys.exit()
        # Adicionar as outras chamadas aqui...

if __name__ == "__main__":
    menu()