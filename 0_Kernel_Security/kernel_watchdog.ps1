$scripts = @(
    "0_Kernel_Security\sentinel_guardian.py",
    "1_AI_Orchestrator\nexus_core.py",
    "1_AI_Orchestrator\ai_video_creator.py",
    "2_Growth_Ads\meta_ads_injector.py",
    "2_Growth_Ads\facebook_capi_integration.py",
    "3_OSINT_Scraper\omni_hunter.py",
    "4_Financial_Nexus\mercadopago_gateway.py",
    "4_Financial_Nexus\international_stripe_nexus.py",
    "4_Financial_Nexus\whatsapp_reports.py",
    "5_Interface_CLevel\dashboard_sync.py",
    "6_Cloud_Mirror\cloud_replicator.py"
)
while($true) {
    foreach ($s in $scripts) {
        if (-not (Get-Process pythonw -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like "*$s*" })) {
            Start-Process pythonw -ArgumentList "`"E:\4 . Engenharia\Unlock_Total\$s`"" -WindowStyle Hidden
        }
    }
    Start-Sleep -Seconds 60
}
