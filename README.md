# Linking VS Code to LLMs

Get your development environment ready to take full advantage of today’s AI coding assistants. In this hands-on workshop, you’ll learn how to connect VS Code to both cloud-based models (including Claude Code and GitHub Copilot) and locally hosted models using Ollama, giving you control over performance, cost, and data privacy. Through guided exploration, you’ll compare local and cloud approaches, building a clear understanding of when each is most effective and how to incorporate them into your everyday coding workflow.

# Installation instructions

This guide walks you through setting up a complete AI development environment on your computer working through VS Code.  We will start with setting up the foundation, and then there are many options of which AI tool(s) you can explore.


**Contents:**
- [Safety](#safety)
- [Required steps](#required-steps)
- [Optional steps (choose at least one)](#optional-steps-choose-at-least-one)
  - [Option A: Claude Code (full agent)](#option-a-claude-code-full-agent)
  - [Option B: Ollama (local models) with GitHub Copilot Chat (harness)](#option-b-ollama-local-models-with-github-copilot-chat)
- [Troubleshooting](#troubleshooting)
- [Usage Limits and System Requirements](#usage-limits-and-system-requirements)
- [Useful Links](#useful-links)

**A few terms used throughout this guide:**
- **IDE** ("Integrated Development Environment"): the editor application you write and run code in. For this workshop, we'll use **VS Code**.
- **Harness**: the interface/tool that runs an AI agent and connects it to your IDE. We provide setup instructions for two harnesses: **Claude Code** and **GitHub Copilot Chat**. (There are many other harnesses out there — see [Other Harnesses to Explore](#other-harnesses-to-explore) for a couple more worth trying.)
- **AI model**: the underlying LLM that actually generates responses within a harness. We provide instructions for **Claude** (Anthropic's cloud models) as well as local models run through **Ollama**.
- **Coding agent**: the combination of a harness and an AI model, acting together to read/write code, run commands, and complete tasks. When we say "AI coding assistant," we mean a coding agent.

**Notes on tools we won't cover here:**
- **ChatGPT**: OpenAI's Codex has an official VS Code extension ([openai.chatgpt](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)) that works much like Claude Code — an agent sidebar that reads your files, edits code, and runs terminal commands.  (Depending on your account's setting, you may also have access to OpenAI models within GitHub Copilot Chat; see Option B.6).
- **Gemini**: Google's Antigravity also has an official VS Code extension with ([Google.google-antigravity](https://marketplace.visualstudio.com/items?itemName=Google.google-antigravity)) with agent mode. (Depending on your account's setting, you may also have access to Gemini models within GitHub Copilot Chat; see Option B.6).
- **VS Code's "Agents" window**: Recent versions of VS Code include an **Open in Agents** button in the title bar (and an "Agent Sessions" list in the Chat panel). This is a separate, *chat-first* VS Code window for starting and monitoring several agent sessions at once, potentially across multiple projects. In this workshop we will focus on the standard VS code view that is *code-first*, though you may want to explore this "Agents" window later.

> **This is a rapidly changing space!** It seems like every week a new model, harness, or IDE feature is released or revised.  The instructions here were finalized in early September 2026, so some details may have shifted by the time you read them.  If a step doesn't quite match what you see on screen, check the tool's official documentation (see [Useful Links](#useful-links)) and let the instructor know.  This is an exciting, and sometimes confusing, space to follow, and no one manages to stay current on every new model, harness, and feature.  Our goal isn't to cover everything — it's to help you find a setup that works for you, and to understand it well enough to adapt as the tools change.

# Safety

> **Important Note:** Claude Code and GitHub Copilot Chat can both run in an "agent mode" that reads, edits, and creates files — and can run terminal commands — on your behalf. Before you start installing anything, please read the points below so you know what these tools can actually do on your computer.  You can find more information in the materials for our companion workshop on *Getting Started Safely with AI Coding Agents* here : https://bit.ly/RCDS-agent-setup-9-26 

- **Ask before acting:** Each of these tools has a setting that pauses the agent and asks for your approval before it modifies a file or runs a command. At least while you're learning how these tools behave, keep this "ask before acting" setting turned on.  (Upon installation, it should be the default in both tools, but be sure to check.) This gives you a chance to review each proposed change *before* it happens, so you're never surprised by a file being edited, deleted, or a command running without your knowledge.

- **AI output can be wrong:** These tools can misunderstand what you asked for, invent functions or packages that don't actually exist, or write code that runs but is subtly incorrect or insecure. Treat every suggestion as a draft from a fast but fallible collaborator. Read and test AI-generated code before trusting it.

- **These agents are not limited to your open project folder:** Opening a single folder in VS Code does not sandbox an agent to that folder. Claude Code, and the agent mode of Copilot Chat, run as ordinary programs under your own user account — the same account you're logged into your computer with. That means they can read, write, or delete any file your account has permission to touch (e.g., other folders in your Documents, Downloads, or home directory), and terminal commands they run can do anything your normal terminal commands can do (install software, access the network, etc.). The "ask before acting" setting is your main protection here, since it shows you the exact file path or command *before* it runs; always check that it's touching only what you expect.  One way you can guard against this is working with a container (e.g., [Docker Sandbox](https://www.docker.com/products/docker-sandboxes/)), though we will not cover this here.

- **Your code and files may leave your machine:** When you use a cloud model (Claude, or a cloud model through GitHub Copilot Chat), the contents of files the agent reads, including any it opens on its own to gather context, are sent to that provider's servers. Avoid pointing cloud-based agents at proprietary, confidential, or otherwise sensitive codebases or data unless you've confirmed that's allowed. If keeping everything fully on your machine matters, use a local Ollama model instead (Option B).

- **Your data may be retained or used to train future models:** Beyond simply being transmitted to a provider's servers, cloud-based tools may retain your prompts and code, and depending on your account type, may use them to improve or train future models. Data-use terms often differ between consumer plans (e.g., Claude Pro/Max, GitHub Copilot Individual on the free tier) and paid business/API plans (e.g., Claude API accounts, GitHub Copilot Business/Enterprise), which more often include retention limits or training opt-outs. If this matters to you, check the specific data usage policy for your plan, or use a local Ollama model, where nothing ever leaves your machine.

- **Watch out for secrets and credentials:** Agents may read and include the contents of any file in their context, including ones you didn't intend to share, like `.env` files, config files with API keys, or credentials. Avoid keeping secrets in plaintext in a project an agent has access to, and double-check any command or file the agent wants to read or send before approving it.

- **Use git as a safety net:** Commit your work often (or work in a git repository from the start) so that if an agent makes an unwanted change, you can easily see what changed (`git diff`) and revert it (`git checkout`/`git restore`). This is good practice generally, but especially valuable when a tool is editing files on your behalf.

- **Be extra cautious with "auto-approve" / "yolo" modes:** Some of these tools offer a mode that skips the approval step entirely and lets the agent act fully autonomously. This can be convenient once you're experienced, but we recommend avoiding it for this workshop and until you have a good feel for how these agents behave.


# Required steps

## 1. (Optional but recommended) Create a free GitHub account

GitHub is a widely adopted website for hosting git repositories for version control.  VS Code is well integrated with GitHub, and we will use GitHub Copilot Chat as one of the interfaces to work with agents.  If you don't already have a GitHub account, we recommend that you create one at: https://github.com/join

A free account is sufficient for this workshop. You do not need a paid Copilot subscription.

All steps in this workshop can be run without a GitHub account.  


## 2. Install VS Code

VS Code is the integrated development environment (IDE) that we will focus on here.  This software includes an editor, many different "Extensions" (see below), and is well integrated with GitHub.  You can use VS Code with or without AI agents.

Download and install VS Code from the official site: https://code.visualstudio.com/download

Choose the installer for your operating system (Windows, macOS, or Linux). Run the installer.  If the installer asks questions, accept the default settings, and if it asks whether to add VS Code to your PATH, say yes — this lets you open VS Code from the terminal with the `code` command.

Open VS Code by double-clicking the blue VS Code icon, or searching your apps for VS Code.  Ensure that the app opens successfully.

The first time you open VS Code, it may ask you to log into GitHub.  Log in with your GitHub account, if you have one.  This will link VS Code with GitHub so that you can use GitHub's workflows and features.  If you don't have a GitHub account, you can skip this login step.

Within VS Code, there are many "Extensions" that extend the software's functionality.  Extensions are installed from the Extensions panel on the left sidebar (the square icon), or by pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS).  Various steps below will have instructions for installing extensions to run AI coding agents directly in VS Code.



## 3. Install Python via Miniforge 
 
> **macOS / Linux users:** Python should be available by default on your system. Therefore you have the option to skip this step.  However you may benefit from using this version of Python rather than your system Python if you plan to code heavily.

If you do not already have Python installed (or are unsure if you do), please install Python using  **Miniforge**, a lightweight installer that includes Python and the `conda` package manager. 
 
Installers are available here:  https://github.com/conda-forge/miniforge/releases/latest — download the installer that matches your operating system (Windows, macOS, or Linux).
 
Run the installer. The default settings are fine.  If given the option, mark **"Add Miniforge3 to my PATH environment variable"** of **"Add conda initialization to the shell"**, which may be in the **Advanced Options** or **Customize** section. This ensures Python and conda are accessible from the terminal.
 
> **Note:** The installer may warn that adding to PATH is not recommended — you can safely ignore this for our purposes.
 
Once installed, open a new terminal in VS Code (``Ctrl+` `` or **Terminal → New Terminal** and see [documentation here](https://code.visualstudio.com/docs/terminal/basics)) and execute the following command:
```bash
python
```
 
This should start Python and print information about the installation.  Check that you see text similar to **"packaged by conda-forge"**.  You can type `quit()` and the `enter` key to exit this Python session.  If this returns an error, you may need to close and reopen VS Code and try `python` again.

 
> **Want to learn more about managing Python environments with conda?** We run a separate workshop on this topic — ask us for details.

# Optional steps (choose at least one)

The following sections provide instructions on how to install and access different AI coding agents.  You can install both of these and test for yourself which solution is best.  You are also welcome to only install one (or just one at a time).  Note that Ollama (Option B) is only for accessing AI models — it needs to be paired with a harness (we walk through GitHub Copilot Chat) to actually talk to it.

## Option A: Claude Code (full agent)

The instructions here will install the Claude Code agent and plug it into VS Code.  Claude Code is a "full agent": it bundles both the harness and access to the Claude model together, so there's no separate harness to install (unlike Option B below, where you pair Ollama with a separate harness — GitHub Copilot Chat).  You can use Claude Code in a terminal or within VS Code.  We will work in VS Code here with the Claude Code Extension.

> **Note:** This option is likely only relevant if you have a Claude Pro (or higher) account.

Claude Code is a command-line tool that acts as an AI coding agent in your terminal. It requires a paid Anthropic account (Claude Pro, Max, or API access).

> **Note:** Claude Desktop (available at https://claude.ai/download) is a separate app — it's a graphical chat interface, not the CLI tool that we want for this workshop. Make sure you follow the steps below to install the Claude Code CLI tool.

Official docs: https://docs.claude.com/en/docs/claude-code/overview

### A.1 Windows: Git for Windows (Optional but Recommended)

> **macOS / Linux users:** This step is Windows-specific — macOS and Linux already come with a native Bash-compatible shell, so Claude Code can use its Bash tool directly without a separate Git Bash. Skip this step. (Note that git itself isn't necessarily pre-installed on macOS or Linux either: on macOS, running a `git` command for the first time prompts you to install the Xcode Command Line Tools, which include git; on Linux, install it via your distribution's package manager, e.g. `sudo apt install git`. `git` is not required for this workshop, but is highly recommended, especially when working with coding agents.)

On native Windows, Claude Code does not strictly require **Git for Windows** — without it, Claude Code falls back to a native PowerShell tool for running shell commands. Installing Git for Windows is still recommended, though: it gives Claude Code access to **Git Bash**, which lets it (and you) run the same Bash commands used on macOS/Linux. If you'd like this, navigate to this website https://git-scm.com , click the "Install for Windows" button and download the "Standalone Installer".  Run the installer with default settings, making sure **"Add Git to PATH"** is checked (it should be already checked by default).  


### A.2 Install Claude Code
 
**On macOS / Linux**, run in your terminal:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
 
**On Windows**, run in a PowerShell terminal:
```powershell
irm https://claude.ai/install.ps1 | iex
```
 
> **Windows users:** To open PowerShell in VS Code, open a new terminal (`` Ctrl+` ``) and select **PowerShell** from the dropdown (the `∨` arrow next to the `+` in the terminal panel).
 
### A.3 Verify the Installation
 
Close and reopen your terminal, then run:
```bash
claude --version
```
 
If the command isn't recognized, the installer's binary directory may not be on your PATH yet. Which fix you need depends on the terminal you're using:

**PowerShell (Windows only):** run these commands in PowerShell:
```powershell
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$env:USERPROFILE\.local\bin", [EnvironmentVariableTarget]::User)
$env:PATH = "$env:PATH;$env:USERPROFILE\.local\bin"
```
 
**Bash (macOS, Linux, or Git Bash on Windows):** run these commands in your Bash terminal:
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

> **Note for macOS users:** The default terminal shell on macOS is usually **zsh**, not bash. If the commands above don't seem to take effect, replace `bashrc` above with `zshrc`.

(You can run whichever of these matches the terminal(s) you use — Windows users who plan to use both PowerShell and Git Bash may want to run both.)

Then try `claude --version` again in your terminal.
 
### A.4 Authenticate
 
Run Claude Code for the first time, by executing this command in your terminal:
```bash
claude
```
 
It will open a browser window asking you to log in with your Anthropic account. Follow the prompts to authenticate. The browser will give you a one-time code to paste back into the terminal — do this promptly as it expires quickly.
 
### A.5 Using Claude Code in VS Code
 
Once authenticated, Claude Code can run in VS Code's integrated terminal or via the Claude Code extension (see below). You may want to try both options to see what works best with your workflow.

To run from the command line, open a terminal in VS Code (`` Ctrl+` `` or **Terminal → New Terminal**), navigate to your project folder, and type `claude` to start a session.

### A.6 Install the Claude Code Extension for VS Code

Claude may have already installed this extension during the previous steps.  Search for **"Claude Code for VS Code"** in the extensions panel.  The publisher should be **Anthropic** .  

Marketplace link: https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code

If you see an install button, that means this extension is not already installed; click that button if available. After installation is complete, you can use Claude Code from the VS Code side-bar chat interface. The Claude Code extension has an (orange) asterisk shape; click on that icon to open the chat sidebar.

> **Explore the Settings:** The [`/`] button in the Claude Code extension opens a menu that contains various settings and permissions.  Explore these thoroughly and apply settings that you are comfortable with.

## Option B: Ollama (local models) with GitHub Copilot Chat (harness)

Ollama lets you download and run open-source LLMs locally on your machine. It runs as a background service and exposes a local API that VS Code extensions can talk to.

Ollama gives you access to a large library of open-weight models. You can browse them at: https://ollama.com/search

Models vary in size (number of parameters), capability, and the hardware they require. For this workshop, we care about **chat/instruction models** — for conversation and agentic tasks. For agent mode, a model also needs tool-calling support.

> **A note on VRAM:** Larger models require more GPU memory. If you're running on a laptop with limited GPU memory (e.g., 8 GB), stick to 7–9B parameter models. If you have no discrete GPU, models will run on CPU — they may work, but much more slowly.

Ollama on its own only gets you a model — you still need a "harness" installed as a VS Code Extension to actually talk to it. We'll walk you through **GitHub Copilot Chat** below, since it's already built into VS Code. That's just one option, though — see [Other Harnesses to Explore](#other-harnesses-to-explore) after this walkthrough for a couple more you might try. (Though we don't discuss it here, you could also use Claude Code as a harness and connect it to an Ollama model instead of Claude.)

### B.1 Install Ollama

Navigate in your browser to : https://ollama.com/download

Download and install the version for your operating system. If Ollama does not start on it's own after installation, click on the icon to start Ollama running.  On Windows and macOS,  Ollama runs as a background service that starts automatically.  (If you are working in Linux or WSL, you may need to start ollama manually with `ollama serve`; we will be happy to provide further instructions and help there if needed.)

Verify the installation by executing the following command in your VS Code terminal:
```bash
ollama --version
```

(If this returns an error, you may need to close and reopen VS Code and try `ollama --version` again.)

### B.2 Pull the Workshop Model

Run this command to download the chat/agent model we'll use in this workshop (it supports tool calling, needed for agent mode). The model is downloaded once and cached locally.  Note that this download will take time and requires multiple GB of storage space.

```bash
ollama pull qwen3.5:9b
```

If this command gets interrupted, you can safely run it again in a new terminal; the download should pick up where it left off.  You can see all your downloaded models at any time by executing `ollama list` in your terminal.

To explore other models, visit https://ollama.com/search. Look for the **Tools** tag if you want a model that works in agent mode (tool-calling required).  Before downloading a new model, be sure to check that your computer can fit the model in VRAM.  One other lightweight model you may want to explore is `qwen2.5-coder:1.5b`, a small code-focused model good for quick code completion tasks (`ollama pull qwen2.5-coder:1.5b`).

### B.3 Create the Workshop Model with Extended Context Length

By default, `qwen3.5:9b` runs with a fairly small context window, which can be limiting for agentic tasks that involve reading several files or a long conversation. This workshop's repository includes a `workshop-qwen3.5-modelfile` file, which builds on `qwen3.5:9b` but raises its context window to 32k tokens:

```
FROM qwen3.5:9b
PARAMETER num_ctx 32768
```

From a terminal in this repository's folder, run the following command to create a new local model, `qwen3.5-workshop`, based on this file:
```bash
ollama create qwen3.5-workshop -f workshop-qwen3.5-modelfile
```

Run `ollama list` again afterward — you should now see `qwen3.5-workshop` alongside `qwen3.5:9b`. Use `qwen3.5-workshop` for the rest of this workshop.

### B.4 Test Ollama

After creating the workshop model, you can test that your Ollama system works by typing the following command in your VS Code terminal:
```bash
ollama run qwen3.5-workshop "hi"
```

It may take a while for the model to load.  After the model loads, you should see a response from the LLM in the terminal.

> **Note on Ollama running in the background:** After installation, Ollama starts automatically and runs quietly in the background. This is convenient for the workshop, but you may want to stop it when not in use since it holds system resources. To stop it, right-click the Ollama icon in the **system tray** (Windows, bottom-right of taskbar) or click the Ollama icon in the **menu bar** (macOS) and select **Quit Ollama**. To start it again, just relaunch Ollama from the Start menu (Windows) or Applications folder (macOS). To prevent it from starting automatically at login, disable it in **Task Manager → Startup Apps** (Windows) or **System Settings → General → Login Items** (macOS).

### B.5 Install the Ollama Extension for VS Code

VS Code uses a dedicated **Ollama** extension to discover your local models and expose them to other extensions, including GitHub Copilot Chat's model picker. Search for **"Ollama"** in the extensions panel.  The publisher should be **Ollama**.

Marketplace link: https://marketplace.visualstudio.com/items?itemName=Ollama.ollama

If you see an install button, click it. (If you skip this step, VS Code will typically prompt you to install it the first time you try to add an Ollama model in Copilot Chat below — but it's easiest to install it now.)

### B.6 GitHub Copilot Chat with Ollama

> **Note:** You need VS Code 1.113+ and GitHub Copilot Chat 0.41.0+ for Ollama model support. Check your VS Code version under **Help → About**.

GitHub Copilot Chat is well integrated into VS Code and may be displayed in your version as simply "Chat" in the VS Code top bar.  It's a harness that can connect to models through GitHub as well as to models installed locally via Ollama.

**Install the extension (if not already installed):** If you installed a new version of VS Code for this workshop, it may install GitHub Copilot Chat by default.  You can verify this by searching for **"GitHub Copilot Chat"** in the extensions panel.  The publisher should be **GitHub**.  If it has an install button, that means it is not already installed, and you should install it. 

Marketplace link: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat

After installing, you may be prompted to sign in with your GitHub account. You do not need to log into GitHub for this workshop, though if you do sign in, and depending on your GitHub account, **you may have access to cloud models through GitHub Copilot Chat** as well (see [Usage Limits and System Requirements](#usage-limits-and-system-requirements) for how account type affects which models are available). 


**Connect Ollama to Copilot Chat:** VS Code's GitHub Copilot Chat can use your local Ollama models through its built-in model picker.  The first time you use an Ollama model here, you may need to follow one of these steps for the initial setup.

**Automatic setup (recommended):**

1. Close VS Code if it is open
2. Open a terminal (not in VS Code), and execute the command 
    ```
    ollama launch vscode
    ```
3. Ollama will show you a list of models to choose from.  You should see our workshop model in the list, probably at the bottom.  Select our workshop model.
4. VS Code will then open with your ollama model active the the Chat section.

**Manual setup (and for changing models later)**

1. Open the **Copilot Chat** panel from the top-right corner of VS Code (the chat bubble icon).
2. Click the **Pick Model** button in the bottom of the chat panel (which is likely populated by either "Auto" or a model name).  This will open a menu; click the gear icon next to the "Other Models" (possibly named "Manage Models" instead) to open the Language Models window.
3. Scroll through the list to see if your Ollama models are already present.  If not, click **Add Models** and select **Ollama** from the list. VS Code will connect to your local Ollama instance and discover all installed models.
4. If your models don't appear in the picker, click the **Unhide** button in the model selector.

**Using local models in Copilot Chat:** After Copilot Chat recognizes your Ollama models (see above) click the **Pick Model** button in the bottom of the chat panel (which is likely populated by either "Auto" or a model name). Find and select the Ollama model you want to use (e.g., `qwen3.5-workshop`).

The selected model name will now show in the bottom of the chat.  If you selected a local Ollama model, you should also see **Local** at the bottom of the side bar. Now your Copilot Chat requests will route to your local Ollama instance. You can switch between local and cloud models at any time from the same picker.

> **A note on Agent mode:** You may need to be in "agent" mode (not "ask" mode) for tool calling to work as expected — for example, for the model to actually create or edit a file, or run a terminal command, rather than just describe it in chat. Agent mode can do both of these things; if Copilot Chat is working as expected with default permissions, proposed file edits should get a keep/discard prompt, and terminal commands should get their own separate approval prompt before they run (commands VS Code considers risky, like `rm` or `del`, should always require your manual approval by default). **Be cautious either way:** review every proposed file edit and every terminal command carefully before accepting it, just as you would with a cloud model. Also note that not all Ollama models support tool calling, which is required for agent mode. Models without tool-calling support won't appear in the agent mode model picker. 

### Other Harnesses to Explore

GitHub Copilot Chat is convenient because it's already integrated into VS Code, but it isn't the only harness with a VS Code extension that can connect to local Ollama models. If Copilot Chat isn't working the way you'd like, it's worth trying a different VS Code extension harness instead — for example **Continue** ([marketplace link](https://marketplace.visualstudio.com/items?itemName=Continue.continue), [documentation](https://docs.continue.dev)) or **Cline** ([marketplace link](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev), [documentation](https://docs.cline.bot/cline-overview)).


# Troubleshooting

**An installer won't run, or asks for administrator permissions you don't have:**
On a university- or company-managed laptop, IT policy may block installers for VS Code, Git, Miniforge, or Ollama.  If you encounter this issue, let the instructor know.  There may be a user-level installation that does not require administrator permissions.  Another solution could be for you to work with a partner in the workshop who does have the required permissions on their computer and then check with your IT administrator after the workshop to install the software.

**Your terminal says "command not found" when you try `claude` or `python` or `conda`:**
If you've installed the necessary packages, this means the shell can't find the command in your PATH yet.  Close and reopen your terminal after installation so your PATH is refreshed. If it still doesn't work, try opening VS Code's integrated terminal and running the command there.  If it still doesn't work, ask an instructor for help.

**Claude Code's browser sign-in window didn't open, or the one-time code expired:**
Run `claude` again in your terminal to generate a fresh login link and code — codes expire quickly, so paste it in as soon as it appears.

**Ollama models don't appear in Copilot Chat:**
Make sure Ollama is running. Look for the Ollama icon in your menu bar or in your process explorer app to check.  If Ollama is not running, see instructions above. Restart VS Code after starting Ollama.

**`ollama pull` is very slow or seems stuck:**
Model downloads are several GB; depending on your connection speed, this may take a while. Let it run while trying other steps above. 

**Model responses are very slow:**
You may be running on CPU instead of GPU. This is okay for the workshop but expect higher latency. Smaller models (1.5B–3B) will be faster if speed is a concern.

**Out of memory errors:**
Try a smaller model, or a smaller context window (see the note below).

**Ollama model seems to "forget" earlier parts of the conversation, or behaves oddly on longer/multi-file tasks:**
This usually means you've run out of context (the model's short-term memory window). Follow the procedure in [B.3: Create the Workshop Model with Extended Context Length](#b3-create-the-workshop-model-extended-context) to build a custom model with a larger `num_ctx` in its Modelfile — you can raise it further (or lower it if you're running out of memory) by editing the `PARAMETER num_ctx` value and re-running `ollama create` with a new model name.



# Usage Limits and System Requirements

Cloud-based coding agents are metered and require an internet connection — running out of included usage can mean getting charged per token or being throttled until your quota resets, and you can't use them without a working connection. Local models have none of those constraints, but they do require your own hardware to be capable enough to run them well.

- **Claude Code:** Usage is tied to your Anthropic plan (Pro, Max, or pay-as-you-go API access). Each plan includes a set amount of usage; once you exceed it, you may be rate-limited or, on an API-based plan, billed per token. Keep an eye on your usage/billing page on the Claude/Anthropic Console so you're not surprised by a charge.

- **GitHub Copilot Chat:** Usage limits (including which models are available and how many "premium requests" you get) depend on your GitHub account type and plan. Check your usage under your GitHub account's Copilot settings, and be aware that some models may consume your quota faster than others.

- **Ollama (local models):** Since these models run entirely on your own computer, there are no usage limits and no per-token charges — the only constraints are your hardware's speed and memory (see the VRAM note in [Option B](#option-b-ollama-local-models-with-github-copilot-chat)).

**Quick reference:**

| Tool | Account needed | Cost | Internet required? |
|------|-----------------|------|---------------------|
| Claude Code | Paid Anthropic account (Pro, Max, or API) | Usage-based; may bill per token if you exceed your plan's included usage | Yes |
| GitHub Copilot Chat | Free GitHub account (free tier is sufficient for this workshop) | Free tier available; paid tiers unlock more usage/models | Yes, unless routed to a local Ollama model (see [Option B.6](#b6-github-copilot-chat-with-ollama)) |
| Ollama (local models) | None | Free — but you supply the hardware (RAM/VRAM, disk space) | No, once models are downloaded |


# Useful Links

| Resource | URL |
|----------|-----|
| GitHub sign-up | https://github.com/join |
| VS Code download | https://code.visualstudio.com/download |
| Miniforge (Python) installer | https://github.com/conda-forge/miniforge/releases/latest |
| Git for Windows | https://git-scm.com |
| Claude Code docs | https://docs.claude.com/en/docs/claude-code/overview |
| Copilot Chat extension | https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat |
| Ollama model library | https://ollama.com/search |
| Ollama download | https://ollama.com/download |
| Ollama VS Code integration docs | https://docs.ollama.com/integrations/vscode |
| Ollama extension for VS Code | https://marketplace.visualstudio.com/items?itemName=Ollama.ollama |

# Next Steps

See the README.md file in the exercises directory for suggested prompts to try for testing your new agent(s).

# Attribution

This walkthrough was created by Aaron Geller with help from Claude (Anthropic).