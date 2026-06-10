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


## 1. Install VS Code

Download and install VS Code from the official site: https://code.visualstudio.com/download

Choose the installer for your operating system (Windows, macOS, or Linux). Run the installer and accept the default settings. When it asks whether to add VS Code to your PATH, say yes — this lets you open VS Code from the terminal with the `code` command.

If you are working from the terminal, you can verify the installation by opening a terminal and running:
```bash
code --version
```

You should see a version number printed.

You can also test the installation by double-clicking the VS Code icon and ensuring that the app opens successfully.


## 2. Create a (free) GitHub account, if you do not already have one

GitHub Copilot's free tier lets you use the model picker, including for local Ollama models. If you don't already have a GitHub account, create one at: https://github.com/join

A free account is sufficient for this workshop. You do not need a paid Copilot subscription.


## 3. Install VS Code Extensions

Open VS Code. Extensions are installed from the Extensions panel on the left sidebar (the square icon), or by pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS).

### 3.1 GitHub Copilot Chat

Search for **"GitHub Copilot Chat"** and install it. The publisher should be **GitHub**.

Marketplace link: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat

After installing, you'll be prompted to sign in with your GitHub account. Follow the prompts in your browser to authorize VS Code.

> **Note:** You need VS Code 1.113 or newer for Ollama model support. Check your version under **Help → About**.

### 3.2 Continue

Search for **"Continue"** and install it. The publisher should be **Continue**.

Marketplace link: https://marketplace.visualstudio.com/items?itemName=Continue.continue

Continue will add a new icon to your left sidebar (a blue "C" logo). You'll configure it to use your local Ollama models in a later step.


## 4. Install Claude Code

Claude Code is a command-line tool that acts as an AI coding agent in your terminal. It requires a paid Anthropic account (Claude Pro, Max, or API access).

Official docs: https://docs.claude.com/en/docs/claude-code/overview

### 4.1 Prerequisites

Claude Code can be installed via a native installer (no other dependencies needed) or via npm. The native installer is simpler.

**Native installer (recommended):**

On macOS or Linux, run this in your terminal:
```bash
curl -fsSL https://claude.ai/install.sh | sh
```

On Windows, download the installer from: https://claude.ai/download

**npm installer (alternative):**

If you prefer npm, you'll first need Node.js 18 or newer:
- Check your version: `node --version`
- If you need to install or upgrade, download from https://nodejs.org (choose the LTS version)

Then install Claude Code:
```bash
npm install -g @anthropic-ai/claude-code
```

> **Important:** Do not use `sudo` with `npm install`. If you get permission errors, the right fix is to use [nvm](https://github.com/nvm-sh/nvm) rather than running as root.

### 4.2 Verify the Installation

Execute the following command in your terminal.

```bash
claude --version
```

You should see a version number.

### 4.3 Authenticate

Run Claude Code for the first time from the terminal inside VS Code (`Ctrl+\` or **Terminal → New Terminal**):
```bash
claude
```

It will open a browser window asking you to log in with your Anthropic account. Follow the prompts to authenticate.  Claude will ask you a few questions; I recommend accepting the defaults.

### 4.4 Using Claude Code in VS Code

Once authenticated, Claude Code can run in VS Code's integrated terminal or via the Claude Code extension.  You may want to try both options to see what works best with your workflow.

To run from the command line, open a terminal in VS Code, navigate to your project folder, and type `claude` to start a session.

To run from the Claude Code from the VS Code side-bar chat interface, you will use the Claude Code extension (https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code).  This was likely installed automatically in Step 4.3 above.  If not, you can install manually in a similar manner to Step 3. above.  The Claude Code extension has an orange asterisk shape; click on that to open the chat sidebar.

---

## 5. Install Ollama

Ollama lets you download and run open-source LLMs locally on your machine. It runs as a background service and exposes a local API that VS Code extensions can talk to.

Navigate to : https://ollama.com/download

Download and install the version for your operating system. On native Windows and macOS, the installer sets up Ollama as a background service that starts automatically.  (If you are working in Linux or WSL, you may need to start ollama manually with `ollama serve`; we will be happy to provide further instructions and help there if needed.)

Verify the installation by executing the following command in your terminal:
```bash
ollama --version
```

### 5.1 Understanding Ollama Models

Ollama gives you access to a large library of open-weight models. You can browse them at: https://ollama.com/search

Models vary in size (number of parameters), capability, and the hardware they require. For this workshop, we care about:

- **Chat/instruction models** — for conversation and agentic tasks (these need tool-calling support for agent mode)
- **Embedding models** — used by Continue for code search and context retrieval

> **A note on VRAM:** Larger models require more GPU memory. If you're running on a laptop with limited GPU memory (e.g., 8 GB), stick to 7–9B parameter models. If you have no discrete GPU, models will run on CPU — they'll work, just more slowly.

### 5.2 Pull the Workshop Models

Run these commands to download the models we'll use. Each model is downloaded once and cached locally.  I have suggestions on models below

**Chat/agent model (good all-around, supports tool calling):**
```bash
ollama pull qwen3.5:9b
```

**Code-focused model:**
```bash
ollama pull qwen2.5-coder:1.5b
```

**Embedding model (used by Continue for codebase indexing):**
```bash
ollama pull nomic-embed-text
```

> You can see all your downloaded models at any time with `ollama list`.

To explore other models, visit https://ollama.com/search. Look for the **Tools** tag if you want a model that works in agent mode (tool-calling required).  Before downloading a new model, be sure to check that your computer can fit the model in VRAM.



## 6. Connect Ollama to GitHub Copilot Chat

VS Code's GitHub Copilot Chat can use your local Ollama models through its built-in model picker. This requires VS Code 1.113+ and GitHub Copilot Chat 0.41.0+.

### 6.1 Quick Setup (Recommended)

Ollama provides a one-command setup for VS Code. In your terminal:
```bash
ollama launch vscode
```

This will print a list of recommended models and configure VS Code automatically. Follow any on-screen instructions.

### 6.2 Manual Setup

If you prefer to configure manually:

1. Open the **Copilot Chat** panel from the top-right corner of VS Code (the chat bubble icon).
2. Click the **settings gear icon** in the chat panel header to open the Language Models window.
3. Click **Add Models** and select **Ollama** from the list. VS Code will connect to your local Ollama instance and discover all installed models.
4. If your models don't appear in the picker, click the **Unhide** button in the model selector.


### 6.3 Using Local Models in Copilot Chat

In the Copilot Chat panel, click the model name at the top to open the model picker. Make sure **Local** is selected at the bottom of the picker. Your Ollama models will be listed there.

Select a model to route your Copilot Chat requests to your local Ollama instance. You can switch between local and cloud models at any time from the same picker.

> **A note on Agent mode:** Not all Ollama models support tool calling, which is required for agent mode (where Copilot can autonomously read files, run terminal commands, and edit code). Models without tool-calling support won't appear in the agent mode model picker. 



## 7. Connect Ollama to Continue

Continue uses a configuration file (`config.yaml`) to define which models it uses for chat, autocomplete, and embeddings. We provided an example `config.yaml` file for the workshop. This section explains where the file lives and how to apply it.

### 7.1 Find the Config File

Continue's configuration file is stored at:

| OS | Path |
|----|------|
| macOS / Linux | `~/.continue/config.yaml` |
| Windows | `%USERPROFILE%\.continue\config.yaml` |

You can also open it directly from VS Code: click the Continue icon in the left sidebar, then click the **gear icon** at the top of the Continue panel.

### 7.2 Apply the Workshop Config

Copy the contents of the `config.yaml` file from this workshop into your `~/.continue/config.yaml` file (replacing what's there). Save the file — Continue reloads automatically.

### 7.3 What the Config Does

The config file tells Continue:
- Which Ollama model to use for **chat/agent** (conversational assistance)
- Which Ollama model to use for **autocomplete** (inline code suggestions as you type)
- Which Ollama model to use for **embeddings** (indexing your codebase for context)

All three point to your local Ollama instance, so nothing leaves your machine.

> **Note:** Only models with tool capabilities should be used in the agent mode.  Other models can be used in the chat mode.

### 7.4 Verify the Connection

Click the **Continue** icon in the left sidebar. At the top of the chat panel, you should see your configured model name. Type a test message — if you get a response, you're connected.

For autocomplete, open any Python file, put your cursor mid-function, and pause for a moment. A gray suggestion should appear. Press `Tab` to accept it.




## 8. Troubleshooting

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



## 9. Useful Links

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