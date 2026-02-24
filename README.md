<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0A192F&height=200&section=header&text=Unlock_Total&fontSize=50&fontColor=D4AF37&animation=fadeIn&fontAlignY=38&desc=Privilege%20Escalation%20Protocol&descAlignY=55&descAlign=50" alt="Unlock Total Banner" />
</div>

<h2 align="center">Acesso Absoluto e Supressão de Restrições Nativas</h2>

<p align="center">
  O <b>Unlock_Total</b> é um protocolo de engenharia de infraestrutura projetado para preparar ambientes Windows para automação extrema e integração de agentes de IA. Ele remove sistematicamente as fricções de segurança nativas (UAC, SmartScreen, MOTW) que impedem a execução de rotinas autônomas.
</p>

---

### 🧠 Arquitetura do Protocolo (O Que Ele Faz)

Para garantir que ecossistemas complexos operem em <i>background</i> sem a necessidade de intervenção humana (pop-ups de permissão), o script atua em quatro pilares do sistema operacional:

1. **Lobotomia do UAC (User Account Control):**
   Neutraliza os alertas de elevação de privilégio alterando os registros `ConsentPromptBehaviorAdmin` e `PromptOnSecureDesktop`.
2. **Supressão do SmartScreen:**
   Desativa o bloqueio de aplicativos e downloads não reconhecidos, modificando as chaves `EnableSmartScreen` no Windows e no Microsoft Edge.
3. **Quebra de Correntes (Execution Policy):**
   Libera o PowerShell para executar scripts não assinados injetando o comando `Set-ExecutionPolicy Bypass -Scope LocalMachine -Force`.
4. **Erradicação do Mark of the Web (MOTW):**
   Desativa a verificação de zona de anexos da internet (`SaveZoneInformation`) e aplica um varrimento recursivo (`Unblock-File`) nas pastas Críticas (Downloads e Desktop) para desbloquear qualquer arquivo baixado por agentes autônomos.

### ⚙️ Vetores de Execução (Como Trabalha)

A estratégia de <i>deploy</i> é poliglota, garantindo execução indetectável dependendo da restrição do ambiente alvo:

<p align="left">
  <img src="https://img.shields.io/badge/C%23_Elite_Edition-0A192F?style=for-the-badge&logo=csharp&logoColor=D4AF37" />
  <img src="https://img.shields.io/badge/Python_Core-0A192F?style=for-the-badge&logo=python&logoColor=D4AF37" />
  <img src="https://img.shields.io/badge/Batch_Native-0A192F?style=for-the-badge&logo=windows&logoColor=D4AF37" />
</p>

* **C# / .EXE (`Unlock_Total.exe`):** Compilação direta usando `Microsoft.Win32.Registry` para alterações silenciosas e chamadas de processo ocultas (`ProcessWindowStyle.Hidden`).
* **Python (`Unlock_Total.py`):** Utiliza as bibliotecas `winreg` e `ctypes` para validação de privilégios (`IsUserAnAdmin()`) e injeção direta no registro, ideal para servidores rodando ecossistemas de dados.
* **Batch (`Unlock_Total.bat`):** Execução nativa e direta via CMD, com injeção ágil de chaves de registro e comandos PowerShell aninhados.

### ⚠️ Diretrizes de Operação

A estratégia recomendada é a **Integração Isolada**. Este protocolo altera o nível de segurança da máquina a zero.
> **Uso Exclusivo em Ambientes Controlados:** Utilize apenas em máquinas virtuais (VMs), instâncias em nuvem (AWS/GCP) ou <i>sandboxes</i> dedicadas à operação de agentes autônomos de automação de marketing e cibersegurança. 

<div align="center">
  <br>
  <a href="https://g.dev/sougabrielprado" target="_blank"><img src="https://img.shields.io/badge/Google_Developers-0A192F?style=for-the-badge&logo=google&logoColor=D4AF37" alt="Google Developers"/></a>
  <a href="https://linkedin.com/in/sougabrielprado" target="_blank"><img src="https://img.shields.io/badge/LinkedIn_C--Level-0A192F?style=for-the-badge&logo=linkedin&logoColor=D4AF37" alt="LinkedIn"/></a>
</div>
