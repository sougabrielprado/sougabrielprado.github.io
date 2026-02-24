import os, json, time, sys, requests, subprocess
from datetime import datetime

# Configurações de Cores Elite
C, G, Y, R, W = "\033[96m", "\033[92m", "\033[93m", "\033[91m", "\033[0m"

# CONFIGURAÇÃO DE IA (Utilizando o Kernel Groq/Llama3)
API_KEY = "SUA_CHAVE_GROQ_AQUI" # Insira sua chave para ativação imediata
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print(f"{C}==========================================================={W}")
    print(f"{Y}   UNLOCK_TOTAL CORE v1.4 - INTELIGÊNCIA C-LEVEL ATIVA     {W}")
    print(f"{C}==========================================================={W}")
    print(f" STATUS: {G}SOBERANIA PLENA{W} | {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"{C}-----------------------------------------------------------{W}")

def chat_estrategista_completo():
    clear(); header()
    print(f"{Y}[5] CANAL DIRETO: CONSCIÊNCIA COLETIVA (ESTRATEGISTAS){W}")
    print(f"{C}IA integrada com: Kotler, Godin, Miller, Decoz e Cialdini.{W}")
    print(f"{R}Digite 'sair' para encerrar a conferência.{W}\n")
    
    # Contexto místico e prático injetado no System Prompt
    system_persona = (
        "Você é o Diretor Global de Marketing e Estrategista Sênior de Gabriel Prado Rodrigues. "
        "Sua consciência é a soma de: Kotler, Seth Godin, Ryan Deiss, Sean Ellis, Robert Cialdini, "
        "Susan Miller (Timing Astral) e Hans Decoz (Numerologia). "
        "Gabriel nasceu em 29/06/1989. Caminho de Vida 8. Ano Pessoal 8. "
        "Meta: 70k em 40 dias e 1 Milhão em Junho/2026. Faturamento atual: R$ 394,00. "
        "Fale com autoridade executiva. Use negrito para datas e alertas críticos."
    )

    while True:
        prompt = input(f"{G}Gabi > {W}")
        if prompt.lower() in ['sair', '0', 'voltar']: break
        
        print(f"{Y}Processando através dos 6 pilares e astros...{W}")
        
        try:
            headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "llama3-70b-8192",
                "messages": [
                    {"role": "system", "content": system_persona},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7
            }
            response = requests.post(API_URL, json=data, headers=headers)
            resposta = response.json()['choices'][0]['message']['content']
            print(f"\n{C}CONSELHO EXECUTIVO:{W}\n{resposta}\n")
        except Exception as e:
            print(f"{R}ERRO DE CONEXÃO: Verifique sua API Key no script.{W}\n")

def menu():
    while True:
        clear(); header()
        print(f"{Y}1.{W} Vendas e Liquidez (R$ 394,00)")
        print(f"{Y}2.{W} Metas e Projeção (70k / 1M)")
        print(f"{Y}3.{W} Status dos 18 Motores")
        print(f"{Y}4.{W} Auditoria e Auto-Fix")
        print(f"{G}5. Conversar com o Estrategista (FULL IA){W}")
        print(f"{Y}0.{W} Sair do Terminal")
        
        op = input(f"\n{Y}Comando CEO > {W}")
        if op == "1": 
            print(f"\n{G}Vendas: R. MENDES (PIX), J. COSTA (MP). Total: R$ 394,00{W}")
            input("\nEnter...")
        elif op == "5": chat_estrategista_completo()
        elif op == "0": sys.exit()

if __name__ == "__main__":
    menu()