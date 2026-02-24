import os
import time
import psutil
import json
import sys

# ==========================================
# SENTINEL GUARDIAN: PROTEÇÃO DE KERNEL E CHAVES
# ==========================================
ROOT_DIR = r"E:\4 . Engenharia\Unlock_Total"
MASTER_DATA = os.path.join(ROOT_DIR, "master_data.json")
LOG_PATH = os.path.join(ROOT_DIR, "Logs", "security_events.log")

# Assinaturas de Ferramentas Forenses e de Auditoria
BLACK-LIST_PROCESSOS = [
    "wireshark.exe", "procmon.exe", "procexp.exe", "x64dbg.exe", 
    "idag.exe", "wireshark.exe", "processhacker.exe", "vboxservice.exe"
]

def registrar_evento(mensagem):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] ALERT: {mensagem}\n")

def protocolo_de_emergencia():
    """Obliteração imediata de rastros e chaves"""
    registrar_evento("CONTRA-INTELIGÊNCIA ATIVADA: Detetada ferramenta de análise.")
    
    # 1. Shutdown de todos os módulos de IA e Financeiro
    os.system("taskkill /F /IM python.exe")
    os.system("taskkill /F /IM pythonw.exe")
    
    # 2. Ofuscação do Master Data (Renomeação e Ocultação)
    if os.path.exists(MASTER_DATA):
        temp_path = MASTER_DATA + ".tmp"
        os.rename(MASTER_DATA, temp_path)
        os.system(f"attrib +h +s {temp_path}")
    
    print("[!] SISTEMA EM MODO DE SEGURANÇA. Chaves protegidas.")
    sys.exit()

def scan_kernel():
    print("--- SENTINEL GUARDIAN ATIVO | MONITORIZAÇÃO DE AMEAÇAS ---")
    while True:
        for proc in psutil.process_iter(['name']):
            try:
                nome_proc = proc.info['name'].lower()
                if nome_proc in BLACK-LIST_PROCESSOS:
                    protocolo_de_emergencia()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Monitorização de integridade do diretório E:\
        if not os.path.exists(ROOT_DIR):
            registrar_evento("Falha de montagem do volume E:\. Possível extração física.")
            
        time.sleep(5) # Varredura de alta frequência

if __name__ == "__main__":
    scan_kernel()
