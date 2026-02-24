import os, json, ast, sys

# Identifica a raiz independente se está no Windows ou no Ubuntu do GitHub
ROOT = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(ROOT, "master_data.json")

print(">>> INICIANDO VARREDURA CI/CD DE ELITE (AST & JSON) <<<")

critical_files = [
    os.path.join("1_AI_Orchestrator", "nexus_core.py"),
    os.path.join("3_Financial_Nexus", "mercadopago_gateway.py"),
    os.path.join("4_Interface_CLevel", "dashboard_sync.py")
]

erros = 0

# Verificação de Sintaxe (Prevenção de Tela Azul/Crash)
for f in critical_files:
    path = os.path.join(ROOT, f)
    if not os.path.exists(path):
        print(f"[-] FALHA CRÍTICA: Arquivo ausente -> {f}")
        erros += 1
    else:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                ast.parse(file.read())
            print(f"[+] AST (Sintaxe) OK: {f}")
        except SyntaxError as e:
            print(f"[-] ERRO SINTAXE em {f}: {e}")
            erros += 1

# Validação de Chaves de Riqueza (Evita deploy sem API)
if os.path.exists(JSON_PATH):
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not data.get("APIs_Elite_IA_Orquestracao", {}).get("GROQ_API_KEY", "").startswith("gsk_"):
        print("[-] VULNERABILIDADE: GROQ_API_KEY corrompida.")
        erros += 1
    if not data.get("Engenharia_Financeira", {}).get("MP_ACCESS_TOKEN", "").startswith("APP_USR-"):
        print("[-] VULNERABILIDADE: MP_ACCESS_TOKEN corrompido.")
        erros += 1
else:
    print("[!] master_data.json ausente no CI. Ignorando validação de chaves locais.")

if erros > 0:
    print(f"\n[-] SHUTDOWN: {erros} vulnerabilidades encontradas. Abortando Deploy.")
    sys.exit(1) # Código 1 avisa ao GitHub que a build quebrou
else:
    print("\n[+] Auditoria Verde. Arquitetura validada. Deploy Autorizado.")
    sys.exit(0) # Código 0 aprova a subida do código
