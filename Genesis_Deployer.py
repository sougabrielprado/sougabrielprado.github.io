import os
import requests
import json
import time

ROOT_DIR = r"E:\4 . Engenharia\Unlock_Total"
GROQ_API_KEY = "config.get("APIs_Elite_IA_Orquestracao", {}).get("GROQ_API_KEY")xpjB"
HEADERS = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}

STRUCTURE = {
    "0_Kernel_Bypass": ["Unlock_Total.bat", "Unlock_Total.cs", "Unlock_Total.py"],
    "1_AI_Orchestrator": ["nexus_core.py", "groq_manager.py"],
    "2_OSINT_Scraper": ["reddit_hunter.py", "github_scraper.py"],
    "3_Financial_Nexus": ["mercadopago_gateway.py"],
    "4_Interface_CLevel": ["dashboard.html"],
    "Logs": ["system_events.log"],
    "Reports": ["AI_Audit_Report.md"]
}

def ask_ai_to_code(filename, module_name):
    prompt = f"Escreva um script inicial pragmático e avançado em Python/HTML para o arquivo '{filename}' que atua no módulo '{module_name}'. Retorne APENAS o código puro, sem formatação markdown."
    payload = {"model": "llama3-8b-8192", "messages": [{"role": "system", "content": "Você é um Engenheiro de Elite C-Level focado em automação extrema."}, {"role": "user", "content": prompt}]}
    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=HEADERS, json=payload)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"# Falha na injeção da IA. Motivo: {e}\n"

def genesis_deploy():
    print("[+] KERNEL INJECT: Inicializando Consciência Coletiva via Groq...")
    for folder, files in STRUCTURE.items():
        folder_path = os.path.join(ROOT_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                print(f"[*] Sintetizando código via IA para: {file}...")
                content = ask_ai_to_code(file, folder) if file.endswith('.py') or file.endswith('.html') else f":: Arquivo {file} - Ecossistema Unlock_Total Nível 0\n"
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                time.sleep(1)
    print("\n[+] Ecossistema autônomo materializado no disco local.")

if __name__ == "__main__":
    genesis_deploy()
