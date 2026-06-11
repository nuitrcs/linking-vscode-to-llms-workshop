# Linking VS Code to LLMs

Get your development environment ready to take full advantage of today’s AI coding assistants. In this hands-on workshop, you’ll learn how to connect VS Code to both cloud-based models (including Claude Code and GitHub Copilot) and locally hosted models using Ollama, giving you control over performance, cost, and data privacy. Through guided exploration, you’ll compare local and cloud approaches, building a clear understanding of when each is most effective and how to incorporate them into your everyday coding workflow.


## Installation instructions

This guide walks you through setting up a complete local AI development environment for the workshop. You'll install:

- **VS Code** — the editor
- **GitHub Copilot Chat** — AI chat using both cloud models and local models
- **Continue** — an alternative AI chat/autocomplete extension using local models
- **Claude Code** — Anthropic's terminal-based coding agent that can also work via a VS Code extension
- **Ollama** — a tool for running LLMs locally on your machine

Work through the sections in order. Each section builds on the previous one.

## 1. Create a (free) GitHub account, if you do not already have one

VS Code is well integrated with GitHub, and we will use GitHub Copilot Chat as one of the interfaces to work with agents.  GitHub Copilot's free tier lets you use the model picker, including for local Ollama models. If you don't already have a GitHub account, create one at: https://github.com/join

A free account is sufficient for this workshop. You do not need a paid Copilot subscription.


## 2. Install VS Code

Download and install VS Code from the official site: https://code.visualstudio.com/download

Choose the installer for your operating system (Windows, macOS, or Linux). Run the installer and accept the default settings. When it asks whether to add VS Code to your PATH, say yes — this lets you open VS Code from the terminal with the `code` command.

Open VS Code by double-clicking the blue VS Code icon, or searching your apps for VS Code.  Ensure that the app opens successfully.

The first time you open VS Code, it may ask you to log into GitHub.  Log in with your GitHub account.  This will link VS Code with GitHub so that you can use GitHub Copilot Chat (and other GitHub workflows).

## 3. Windows prerequisites

### 3.1 Git for Windows

> **macOS / Linux users:** You should not need git for this workshop. Skip this step.

Claude Code on Windows requires **Git for Windows**. If you don't already have it, navigate to this website https://git-scm.com , click the "Install for Windows" button and download the "Standalone Installer".  Run the installer with default settings, making sure **"Add Git to PATH"** is checked (it should be already checked by default).  

> **Note:** Git for Windows includes **Git Bash**, a terminal that supports the same commands as macOS/Linux. You can open it from the Start menu, or from within VS Code by opening a new terminal (`` Ctrl+` `` or **Terminal → New Terminal**) and selecting **Git Bash** from the dropdown (the `∨` arrow next to the `+` in the terminal panel).  You may need to close and reopen VS Code for the Git Bash terminal to become available.


### 3.2 Install Python via Miniforge 
 
> **macOS / Linux users:** Python is available by default on your system. You can skip this step.  However you may benefit from using this version of Python rather than your system Python if you plan to code heavily.

If you do not already have Python installed (or are unsure if you do), please instal Python using  **Miniforge**, a lightweight installer that includes Python and the `conda` package manager. 
 
Installers are avilable here:  https://github.com/conda-forge/miniforge/releases/latest — download the file named **Miniforge3-Windows-x86_64.exe**
 
Run the installer. The default settings are fine, with one exception: on the **Advanced Options** screen, check **"Add Miniforge3 to my PATH environment variable"**. This ensures Python and conda are accessible from the terminal.
 
> **Note:** The installer may warn that adding to PATH is not recommended — you can safely ignore this for our purposes.
 
Once installed, open a new terminal in VS Code and execute the following command:
```bash
python --version
```
 
This should print the version number.  If this returns an error, you may need to close and reopen VS Code and try `python --version` again.

 
> **Want to learn more about managing Python environments with conda?** We run a separate workshop on this topic — ask us for details.


## 4. Install Claude Code, if you have a Pro (or higher) account

Claude Code is a command-line tool that acts as an AI coding agent in your terminal. It requires a paid Anthropic account (Claude Pro, Max, or API access).

> **Note:** Claude Desktop (available at https://claude.ai/download) is a separate app — it's a graphical chat interface, not the CLI tool that we want for this workshop. Make sure you follow the steps below to get the Claude Code.

Official docs: https://docs.claude.com/en/docs/claude-code/overview


### 4.1 Install Claude Code
 
**On macOS / Linux**, run in your terminal:
```bash
curl -fsSL https://claude.ai/install.sh | sh
```
 
**On Windows**, run in a PowerShell terminal:
```powershell
irm https://claude.ai/install.ps1 | iex
```
 
> **Windows users:** To open PowerShell in VS Code, open a new terminal (`` Ctrl+` ``) and select **PowerShell** from the dropdown (the `∨` arrow next to the `+` in the terminal panel).
 
### 4.2 Verify the Installation
 
Close and reopen your terminal, then run:
```bash
claude --version
```
 
If the command isn't recognized on Windows, the binary may not be on your PATH yet. 

To enable claude in Windows PowerShell, run these commands in PowerShell:
```powershell
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$env:USERPROFILE\.local\bin", [EnvironmentVariableTarget]::User)
$env:PATH = "$env:PATH;$env:USERPROFILE\.local\bin"
```
 
To enable claude in Git Bash, run these commands in the Git Bash terminal:
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

(You can choose either or both of these depending on which terminal you are most comfortable with.)

Then try `claude --version` again in your terminal.
 
### 4.3 Authenticate
 
Run Claude Code for the first time:
```bash
claude
```
 
It will open a browser window asking you to log in with your Anthropic account. Follow the prompts to authenticate. The browser will give you a one-time code to paste back into the terminal — do this promptly as it expires quickly.
 
### 4.4 Using Claude Code in VS Code
 
Once authenticated, Claude Code can run in VS Code's integrated terminal or via the Claude Code extension (see below). You may want to try both options to see what works best with your workflow.

To run from the command line, open a terminal in VS Code (`` Ctrl+` `` or **Terminal → New Terminal**), navigate to your project folder, and type `claude` to start a session.


## 5. Install VS Code Extensions

Within VS Code, Extensions are installed from the Extensions panel on the left sidebar (the square icon), or by pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS).

### 5.1 Claude Code for VS Code (if you have a Claude Pro, or higher, account)

Claude may have already installed this extension during the previous step.  Search for **"Claude Code for VS Code"** in the extensions panel.  The publisher should be **Anthropic** .  

Marketplace link: https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code

If you see an install button, that means this extension is not already installed; click that button if available. After installation is complete, you can use Claude Code from the VS Code side-bar chat interface. The Claude Code extension has an (orange) asterisk shape; click on that icon to open the chat sidebar.

### 5.2 GitHub Copilot Chat (if not installed already)

If you installed a new version of VS Code for this workshop, it may install GitHub Copilot Chat by default.  You can verify this by searching for **"GitHub Copilot Chat"** in the extensions panel.  The publisher should be **GitHub**.  If it has an install button, that means it is not already installed, and you should install it. 

Marketplace link: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat

After installing, you'll be prompted to sign in with your GitHub account. Follow the prompts in your browser to authorize VS Code.

> **Note:** You need VS Code 1.113 or newer for Ollama model support. Check your version under **Help → About**.

### 5.3 Continue

Search for **"Continue"** and install it. The publisher should be **Continue**.

Marketplace link: https://marketplace.visualstudio.com/items?itemName=Continue.continue

Continue will add a new icon to your left sidebar (a broken octogon logo). You'll configure it to use your local Ollama models in a later step.


## 6. Install Ollama

Ollama lets you download and run open-source LLMs locally on your machine. It runs as a background service and exposes a local API that VS Code extensions can talk to.

Navigate in your browser to : https://ollama.com/download

Download and install the version for your operating system. On native Windows and macOS, the installer sets up Ollama as a background service that starts automatically.  (If you are working in Linux or WSL, you may need to start ollama manually with `ollama serve`; we will be happy to provide further instructions and help there if needed.)

Verify the installation by executing the following command in your VS Code terminal:
```bash
ollama --version
```

(If this returns an error, you may need to close and reopen VS Code and try `ollama --version` again.)

### 6.1 Understanding Ollama Models

Ollama gives you access to a large library of open-weight models. You can browse them at: https://ollama.com/search

Models vary in size (number of parameters), capability, and the hardware they require. For this workshop, we care about:

- **Chat/instruction models** — for conversation and agentic tasks (for agent mode, models need tool-calling support)
- **Embedding models** — used by Continue for code search and context retrieval

> **A note on VRAM:** Larger models require more GPU memory. If you're running on a laptop with limited GPU memory (e.g., 8 GB), stick to 7–9B parameter models. If you have no discrete GPU, models will run on CPU — they'll work, just more slowly.

### 6.2 Pull the Workshop Models

Run these commands to download the models we'll use. Each model is downloaded once and cached locally.  I have suggestions on models below.  Note that these downloads will take time and larger models will require multiple GB of storage space.  

**Chat/agent model (good all-around, supports tool calling):**
```bash
ollama pull qwen3.5:9b
```

**Code-focused model (small model for quick code completion tasks):**
```bash
ollama pull qwen2.5-coder:1.5b
```

**Embedding model (used by Continue for codebase indexing):**
```bash
ollama pull nomic-embed-text
```

> You can see all your downloaded models at any time with `ollama list`.

To explore other models, visit https://ollama.com/search. Look for the **Tools** tag if you want a model that works in agent mode (tool-calling required).  Before downloading a new model, be sure to check that your computer can fit the model in VRAM.

After downloading these models, you can test that your ollama system works by typing the following command in your VS Code terminal:
```bash
ollama run qwen3.5:9b "hi"
```

(After the model loads, you should see a response from the LLM in the terminal.)

> **Note on Ollama running in the background:** After installation, Ollama starts automatically and runs quietly in the background. This is convenient for the workshop, but you may want to stop it when not in use since it holds system resources. To stop it, right-click the Ollama icon in the **system tray** (Windows, bottom-right of taskbar) or click the Ollama icon in the **menu bar** (macOS) and select **Quit Ollama**. To start it again, just relaunch Ollama from the Start menu (Windows) or Applications folder (macOS). To prevent it from starting automatically at login, disable it in **Task Manager → Startup Apps** (Windows) or **System Settings → General → Login Items** (macOS).

## 7. Connect Ollama to GitHub Copilot Chat

VS Code's GitHub Copilot Chat can use your local Ollama models through its built-in model picker. This requires VS Code 1.113+ and GitHub Copilot Chat 0.41.0+.

### 7.1 Quick Setup (Recommended)

Ollama provides a one-command setup for VS Code. In your terminal:
```bash
ollama launch vscode
```

This will print a list of recommended models and configure VS Code automatically. Follow any on-screen instructions.  The models we installed will likely be at the bottom of the list (under "More").  

### 7.2 Manual Setup

If you prefer to configure manually:

1. Open the **Copilot Chat** panel from the top-right corner of VS Code (the chat bubble icon).
2. Click the **Pick Model** button in the bottom of the chat panel (which is likely populated by either "Auto" or a model name).  This will open a menu; click the gear icon next to the "Other Models" to open the Language Models window.
3. Scroll through the list to see if your ollama models are already present.  If not, click **Add Models** and select **Ollama** from the list. VS Code will connect to your local Ollama instance and discover all installed models.
4. If your models don't appear in the picker, click the **Unhide** button in the model selector.


### 7.3 Using Local Models in Copilot Chat

In the Copilot Chat panel, click the **Pick Model** button in the bottom of the chat panel (which is likely populated by either "Auto" or a model name). Find and select the Ollama you want to use.

The selected model name will now show in the bottom of the chat.  If you selected a local Ollama model, you should also see **Local** at the bottom of the side bar. Now your Copilot Chat requests will route to your local Ollama instance. You can switch between local and cloud models at any time from the same picker.

> **A note on Agent mode:** Not all Ollama models support tool calling, which is required for agent mode (where Copilot can autonomously read files, run terminal commands, and edit code). Models without tool-calling support won't appear in the agent mode model picker. 



## 8. Connect Ollama to Continue

Continue uses a configuration file (`config.yaml`) to define which models it uses for chat, autocomplete, and embeddings. We provided an example `config.yaml` file for the workshop. This section explains where the file lives and how to apply it.

### 8.1 Find the Config File

Open Continue's configuration file from VS Code: click the Continue icon in the left sidebar, then click the **gear icon** at the top of the Continue panel, then click **"Configs"** on the side panel.  You should see the **"Local Config"** in the panel.  Click the **gear icon** next to "Local Config" to open the `config.yaml` file in the VS Code file editor panel.

### 8.2 Apply the Workshop Config

Copy the contents of the `config.yaml` file from this workshop into your open `config.yaml` file iun VS Code (replacing the text that is there). Save the file — Continue reloads automatically.  

### 8.3 What the Config Does

The config file tells Continue:
- Which Ollama model to use for **chat/agent** (conversational assistance)
- Which Ollama model to use for **autocomplete** (inline code suggestions as you type)
- Which Ollama model to use for **embeddings** (indexing your codebase for context)

All three point to your local Ollama instance, so nothing leaves your machine.

> **Note:** Only models with tool capabilities should be used in the agent mode.  Other models can be used in the chat mode.

### 8.4 Verify the Connection

Click the **Continue** icon in the left sidebar if it is not already open. At the top of the chat panel, you should see your configured model name. Type a test message — if you get a response, you're connected.

For autocomplete, open any Python file, put your cursor mid-function, and pause for a moment. A gray suggestion should appear. Press `Tab` to accept it.




## 9. Troubleshooting

**Ollama models don't appear in Copilot Chat:**
Make sure Ollama is running. On macOS/Linux you can check with `pgrep ollama` or look for the Ollama icon in your menu bar. Restart VS Code after starting Ollama.

**Continue shows a connection error:**
Check that Ollama is running and that the model name in your `config.yaml` exactly matches what `ollama list` shows.

**Claude Code says "command not found":**
Close and reopen your terminal after installation so your PATH is refreshed. If it still doesn't work, try opening VS Code's integrated terminal and running `claude --version` there.

**Model responses are very slow:**
You may be running on CPU instead of GPU. This is okay for the workshop but expect higher latency. Smaller models (1.5B–3B) will be faster if speed is a concern.

**Out of memory errors:**
Try a smaller model.  If using Continue, try a smaller context in the `config.yaml` file.



## 10. Useful Links

| Resource | URL |
|----------|-----|
| VS Code download | https://code.visualstudio.com/download |
| GitHub sign-up | https://github.com/join |
| Copilot Chat extension | https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat |
| Continue extension | https://marketplace.visualstudio.com/items?itemName=Continue.continue |
| Claude Code docs | https://docs.claude.com/en/docs/claude-code/overview |
| Node.js LTS download | https://nodejs.org |
| Ollama download | https://ollama.com/download |
| Ollama model library | https://ollama.com/search |
| Ollama VS Code integration docs | https://docs.ollama.com/integrations/vscode |
| Continue documentation | https://docs.continue.dev |