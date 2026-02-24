using System;
using Microsoft.Win32;
using System.Diagnostics;

class GodMode {
    static void Main() {
        Console.WriteLine("--- PROTOCOLO GOD_MODE: C# ELITE EDITION ---");

        try {
            // UAC & SmartScreen via Registry
            Registry.SetValue(@"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "ConsentPromptBehaviorAdmin", 0);
            Registry.SetValue(@"HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System", "EnableSmartScreen", 0);
            
            // Execution Policy Bypass via Process Call
            ProcessStartInfo psi = new ProcessStartInfo("powershell", "Set-ExecutionPolicy Bypass -Force");
            psi.WindowStyle = ProcessWindowStyle.Hidden;
            Process.Start(psi);

            Console.WriteLine("[OK] Sistema de privilégios e execução reconfigurado.");
        }
        catch (Exception e) {
            Console.WriteLine("[!] Falha Crítica: " + e.Message);
        }
    }
}