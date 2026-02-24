$scripts = @(
    "1_AI_Orchestrator\nexus_core.py",
    "1_AI_Orchestrator\social_proof_injector.py",
    "2_OSINT_Scraper\omni_hunter.py",
    "3_Financial_Nexus\mercadopago_gateway.py",
    "3_Financial_Nexus\whatsapp_reports.py",
    "4_Interface_CLevel\dashboard_sync.py",
    "sentinel_guardian.py",
    "7_Cloud_Mirror\cloud_replicator.py"
)

Write-Host "--- SHADOW WATCHDOG ATIVO: PROTEÇÃO DE UPTIME ---" -ForegroundColor Cyan

while($true) {
    foreach ($s in $scripts) {
        $process = Get-Process pythonw -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*$s*" }
        if (-not $process) {
            Write-Host "[!] Agente Off-line: $s. Reiniciando..." -ForegroundColor Red
            Start-Process pythonw -ArgumentList "`"E:\4 . Engenharia\Unlock_Total\$s`"" -WindowStyle Hidden
        }
    }
    Start-Sleep -Seconds 60
}