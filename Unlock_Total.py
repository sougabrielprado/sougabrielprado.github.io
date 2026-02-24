import os
import winreg
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("[!] ERRO: Execução Primordial Necessária.")
    exit()

print("--- INICIANDO PROTOCOLO GOD_MODE (PYTHON) ---")

def set_reg_key(hkey, path, name, value):
    try:
        key = winreg.CreateKeyEx(hkey, path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(key)
    except Exception as e:
        print(f"Erro ao definir {name}: {e}")

# Configurações de UAC e SmartScreen
set_reg_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "ConsentPromptBehaviorAdmin", 0)
set_reg_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\System", "EnableSmartScreen", 0)

# MOTW Bypass
set_reg_key(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\Attachments", "SaveZoneInformation", 2)
os.environ["SEE_MASK_NOZONECHECKS"] = "1"

print("[OK] Registros alterados e ambiente isolado.")