# Installation instructions

This guide walks you through setting up a complete AI development environment on your computer working through VS Code.  We will start with setting up the foundation, and then there are many options of which AI tool(s) you can explore.


**Contents:**

- [Required steps](#required-steps)
- [Optional steps (choose at least one)](#optional-steps-choose-at-least-one)
  - [Option A: Claude Code (full agent)](#option-a-claude-code-full-agent)
  - [Option B: Ollama (local models) with GitHub Copilot Chat (harness)](#option-b-ollama-local-models-with-github-copilot-chat)
- [Troubleshooting](#troubleshooting)



<br/><br/>

# Required steps

## 1. Create a free GitHub account (optional but recommended) 

<details>
<summary><b><i>👉 Click to show / hide</i></b></summary>


GitHub is a widely adopted website for hosting git repositories for version control.  VS Code is well integrated with GitHub, and we will use GitHub Copilot Chat as one of the interfaces to work with agents.  If you don't already have a GitHub account, we recommend that you create one at: https://github.com/join

A free account is sufficient for this workshop. You do not need a paid Copilot subscription.

All steps in this workshop can be run without a GitHub account, except for the code completion exercise (Exercise 1), which needs a GitHub login.  If you don't have an account, you can work through that exercise with a neighbor who does.

</details>

## 2. Install VS Code

<details>
<summary><b><i>👉 Click to show / hide</i></b></summary>


VS Code is the integrated development environment (IDE) that we will focus on here.  This software includes an editor, many different "Extensions" (see below), and is well integrated with GitHub.  You can use VS Code with or without AI agents.

Download and install VS Code from the official site: https://code.visualstudio.com/download

Choose the installer for your operating system (Windows, macOS, or Linux). Run the installer.  If the installer asks questions, accept the default settings, and if it asks whether to add VS Code to your PATH, say yes — this lets you open VS Code from the terminal with the `code` command.

Open VS Code by double-clicking the blue VS Code icon, or searching your apps for VS Code.  Ensure that the app opens successfully.

The first time you open VS Code, it may ask you to log into GitHub.  Log in with your GitHub account, if you have one.  This will link VS Code with GitHub so that you can use GitHub's workflows and features.  If you don't have a GitHub account, you can skip this login step.

Within VS Code, there are many "Extensions" that extend the software's functionality.  Extensions are installed from the Extensions panel on the left sidebar (the square icon), or by pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS).  Various steps below will have instructions for installing extensions to run AI coding agents directly in VS Code.

</details>

## 3. Install Python via Miniforge (optional but recommended) 

<details>
<summary><b><i>👉 Click to show / hide</i></b></summary>

 
> **macOS / Linux users:** Python should be available by default on your system. Therefore you have the option to skip this step.  However you may benefit from using this version of Python rather than your system Python if you plan to code heavily.

If you do not already have Python installed (or are unsure if you do), please install Python using  **Miniforge**, a lightweight installer that includes Python and the `conda` package manager. 
 
Installers are available here:  https://github.com/conda-forge/miniforge/releases/latest — download the installer that matches your operating system (Windows, macOS, or Linux).
 
Run the installer. The default settings are fine.  If given the option, mark **"Add Miniforge3 to my PATH environment variable"** or **"Add conda initialization to the shell"**, which may be in the **Advanced Options** or **Customize** section. This ensures Python and conda are accessible from the terminal.
 
> **Note:** The installer may warn that adding to PATH is not recommended — you can safely ignore this for our purposes.
 
Once installed, open a new terminal in VS Code (``Ctrl+` `` or **Terminal → New Terminal** and see [documentation here](https://code.visualstudio.com/docs/terminal/basics)) and execute the following command:
```bash
python
```
 
This should start Python and print information about the installation.  Check that you see text similar to **"packaged by conda-forge"**.  You can type `quit()` and the `enter` key to exit this Python session.  If this returns an error, you may need to close and reopen VS Code and try `python` again.

 
> **Want to learn more about managing Python environments with conda?** We run a separate workshop on this topic — ask us for details.

</details>

## 4. Install Python packages for the exercises (optional but recommended)

<details>
<summary><b><i>👉 Click to show / hide</i></b></summary>

The exercises in this workshop ask the AI to write Python code that reads data and makes plots.  To run that code yourself, you will need a few Python packages: `pandas`, `matplotlib`, `seaborn`, and `scipy`.  If you installed Python through Miniforge (step 3), we recommend creating a new conda environment for the workshop.  Run these commands in a terminal:
```bash
conda create -n workshop python pandas matplotlib seaborn scipy
conda activate workshop
```

If you prefer not to make a new environment, you can instead install the packages into your current environment with `conda install pandas matplotlib seaborn scipy`.

To check that everything worked, run:
```bash
python -c "import pandas, matplotlib, seaborn, scipy; print('all good')"
```

If VS Code asks you to select a Python interpreter when you open a `.py` file, choose the one from the `workshop` environment (or press `Ctrl+Shift+P` / `Cmd+Shift+P` and run **Python: Select Interpreter**).  You will need to run `conda activate workshop` in each new terminal unless VS Code does so for you.

</details>

<br/><br/>

# Optional steps (choose at least one)

The following sections provide instructions on how to install and access different AI coding agents.  You can install both of these and test for yourself which solution is best.  You are also welcome to only install one (or just one at a time).  Note that Ollama (Option B) is only for accessing AI models — it needs to be paired with a harness (we walk through GitHub Copilot Chat) to actually talk to it.

## Option A: Claude Code (full agent)

<details>
<summary><b><i>👉 Click to show / hide</i></b></summary>

The instructions here will install the Claude Code agent and plug it into VS Code.  Claude Code is a "full agent": it bundles both the harness and access to the Claude model together, so there's no separate harness to install (unlike Option B below, where you pair Ollama with a separate harness — GitHub Copilot Chat).  You can use Claude Code in a terminal or within VS Code.  We will work in VS Code here with the Claude Code Extension.

> **Note:** This option is likely only relevant if you have a Claude Pro (or higher) account.

Claude Code is a command-line tool that acts as an AI coding agent in your terminal. It requires a paid Anthropic account (Claude Pro, Max, or API access).

> **Note:** Claude Desktop (available at https://claude.ai/download) is a separate app — it's a graphical chat interface, not the CLI tool that we want for this workshop. Make sure you follow the steps below to install the Claude Code CLI tool.

Official docs: https://docs.claude.com/en/docs/claude-code/overview

### A.1 Windows: Git for Windows (optional but recommended)

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

</details>

## Option B: Ollama (local models) with GitHub Copilot Chat (harness)

<details>
<summary><b><i>👉 Click to show / hide</i></b></summary>

Ollama lets you download and run open-source LLMs locally on your machine. It runs as a background service and exposes a local API that VS Code extensions can talk to.

Ollama gives you access to a large library of open-weight models. You can browse them at: https://ollama.com/search

Models vary in size (number of parameters), capability, and the hardware they require. For this workshop, we care about **chat/instruction models** — for conversation and agentic tasks. For agent mode, a model also needs tool-calling support.

> **A note on VRAM:** Larger models require more GPU memory. If you're running on a laptop with limited GPU memory (e.g., 8 GB), stick to 7–9B parameter models. If you have no discrete GPU, models will run on CPU — they may work, but much more slowly.

Ollama on its own only gets you a model — you still need a "harness" installed as a VS Code Extension to actually talk to it. We'll walk you through **GitHub Copilot Chat** below, since it's already built into VS Code. That's just one option, though — see [Other Harnesses to Explore](#other-harnesses-to-explore) after this walkthrough for a couple more you might try. (Though we don't discuss it here, you could also use Claude Code as a harness and connect it to an Ollama model instead of Claude.)

### B.1 Install Ollama

Navigate in your browser to : https://ollama.com/download

Download and install the version for your operating system. If Ollama does not start on its own after installation, click on the icon to start Ollama running.  On Windows and macOS,  Ollama runs as a background service that starts automatically.  (If you are working in Linux or WSL, you may need to start ollama manually with `ollama serve`; we will be happy to provide further instructions and help there if needed.)

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

To explore other models, visit https://ollama.com/search. Look for the **Tools** tag if you want a model that works in agent mode (tool-calling required).  Before downloading a new model, be sure to check that your computer can fit the model in VRAM.  

If the `qwen3.5:9b` model is too large or is taking too long for you to download, you can try a lightweight version of this model family via `ollama pull qwen3.5:0.8b`.

### B.3 Create the Workshop Model with 64k Context Length (optional but recommended) 

By default, `qwen3.5:9b` may run in ollama with a relatively small context window, which can be limiting for agentic tasks that involve reading several files or a long conversation. This workshop's repository includes a `workshop-qwen3.5-modelfile` file, which builds on `qwen3.5:9b` and sets its context window to 64k tokens. From a terminal in this repository's folder, run the following command to create a new local model, `qwen3.5-workshop`, based on this file:
```bash
ollama create qwen3.5-workshop -f workshop-qwen3.5-modelfile
```

Run `ollama list` again afterward — you should now see `qwen3.5-workshop` alongside `qwen3.5:9b`. Use `qwen3.5-workshop` for the rest of this workshop.  

(If you want at different context size, you can change the number at the end of the second line in the file, to change the `num_ctx` parameters, and then run the `ollama create` command again to generate a new model.)

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
4. VS Code will then open with your ollama model active in the Chat section.

**Manual setup (and for changing models later):**

1. Open the **Copilot Chat** panel from the top-right corner of VS Code (the chat bubble icon).
2. Click the **Pick Model** button in the bottom of the chat panel (which is likely populated by either "Auto" or a model name).  This will open a menu; click the gear icon next to the "Other Models" (possibly named "Manage Models" instead) to open the Language Models window.
3. Scroll through the list to see if your Ollama models are already present.  If not, click **Add Models** and select **Ollama** from the list. VS Code will connect to your local Ollama instance and discover all installed models.
4. If your models don't appear in the picker, click the **Unhide** button in the model selector.

**Using local models in Copilot Chat:** After Copilot Chat recognizes your Ollama models (see above) click the **Pick Model** button in the bottom of the chat panel (which is likely populated by either "Auto" or a model name). Find and select the Ollama model you want to use (e.g., `qwen3.5-workshop`).

The selected model name will now show in the bottom of the chat.  If you selected a local Ollama model, you should also see **Local** at the bottom of the side bar. Now your Copilot Chat requests will route to your local Ollama instance. You can switch between local and cloud models at any time from the same picker.

> **A note on Agent mode:** You may need to be in "agent" mode (not "ask" mode) for tool calling to work as expected — for example, for the model to actually create or edit a file, or run a terminal command, rather than just describe it in chat. Agent mode can do both of these things; if Copilot Chat is working as expected with default permissions, proposed file edits should get a keep/discard prompt, and terminal commands should get their own separate approval prompt before they run (commands VS Code considers risky, like `rm` or `del`, should always require your manual approval by default). **Be cautious either way:** review every proposed file edit and every terminal command carefully before accepting it, just as you would with a cloud model. Also note that not all Ollama models support tool calling, which is required for agent mode. Models without tool-calling support won't appear in the agent mode model picker. 

### Other Harnesses to Explore

GitHub Copilot Chat is convenient because it's already integrated into VS Code, but it isn't the only harness with a VS Code extension that can connect to local Ollama models. If Copilot Chat isn't working the way you'd like, it's worth trying a different VS Code extension harness instead — for example **Continue** ([marketplace link](https://marketplace.visualstudio.com/items?itemName=Continue.continue), [documentation](https://docs.continue.dev)) or **Cline** ([marketplace link](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev), [documentation](https://docs.cline.bot/cline-overview)).

</details>

<br/><br/>

## Troubleshooting

<details>
<summary><b><i>👉 Click to show / hide</i></b></summary>

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

</details>