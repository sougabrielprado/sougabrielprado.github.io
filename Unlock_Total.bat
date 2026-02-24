@echo off
:: G-OS GOD_MODE v8.0 - Batch Version
:: Objetivo: Acesso Absoluto via Registro e CMD Nativo

NET SESSION >nul 2>&1
if %errorLevel% NEQ 0 (
    echo [!] ERRO: Requer privilegios de Administrador.
    pause & exit
)

echo --- INICIANDO PROTOCOLO GOD_MODE (NATIVO) ---

:: 2. UAC BYPASS
echo 1. Lobotomizando UAC...
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "ConsentPromptBehaviorAdmin" /t REG_DWORD /d 0 /f
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "PromptOnSecureDesktop" /t REG_DWORD /d 0 /f

:: 3. SMARTSCREEN
echo 2. Desativando SmartScreen...
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" /v "EnableSmartScreen" /t REG_DWORD /d 0 /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Edge" /v "SmartScreenEnabled" /t REG_DWORD /d 0 /f

:: 4. EXECUTION POLICY & MOTW
echo 3. Quebrando correntes e MOTW...
powershell -Command "Set-ExecutionPolicy Bypass -Scope LocalMachine -Force"
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Attachments" /v "SaveZoneInformation" /t REG_DWORD /d 2 /f
setx SEE_MASK_NOZONECHECKS 1

:: 5. DESBLOQUEIO RECURSIVO
echo 4. Removendo bloqueios do Filesystem...
powershell -Command "Get-ChildItem -Path '%USERPROFILE%\Downloads','%USERPROFILE%\Desktop' -Recurse | Unblock-File"

echo --- GOD_MODE APLICADO ---
pause