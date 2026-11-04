# Linking VS Code to LLMs

Get your development environment ready to take full advantage of today’s AI coding assistants. In this hands-on workshop, you’ll learn how to connect VS Code to both cloud-based models (including Claude Code and GitHub Copilot) and locally hosted models using Ollama, giving you control over performance, cost, and data privacy. Through guided exploration, you’ll compare local and cloud approaches, building a clear understanding of when each is most effective and how to incorporate them into your everyday coding workflow.

## Workshop Outline

1. Review the remainder of this file.
2. Install the software, following the [installation instructions](installation_instructions.md).
3. Work through the [exercises](exercises/README.md) and discuss.

## Why work this way? Advantages of an in-editor coding agent

You can already talk to an LLM by pasting code into a chat window in your browser. So why bother connecting VS Code to Claude Code, GitHub Copilot Chat, or Ollama instead? A few reasons:

- No more copy-pasting code back and forth between browser-based chat and code files.
- It sees your whole project, not just one snippet. 
- It can act, not just talk.
- Multi-file changes happen together.
- You can choose local/private models.

And why VS Code specifically, rather than another app?

- It's free and runs on all operating systems.
- It has official extensions for many AI tools (including those in this workshop), and huge extension ecosystem beyond AI.
- It's the most widely used editor, so it's also the most widely supported.
- Built-in terminal and git integration.
- Lightweight and fast.

## Notes and terminology

### A few terms used throughout this guide

- **IDE** ("Integrated Development Environment"): the editor application you write and run code in. For this workshop, we'll use **VS Code**.
- **Harness**: the interface/tool that runs an AI agent and connects it to your IDE. We provide setup instructions for two harnesses: **Claude Code** and **GitHub Copilot Chat**. (There are many other harnesses out there — see [Other Harnesses to Explore](installation_instructions.md#other-harnesses-to-explore) for a couple more worth trying.)
- **AI model**: the underlying LLM that actually generates responses within a harness. We provide instructions for **Claude** (Anthropic's cloud models) as well as local models run through **Ollama**.
- **Coding agent**: the combination of a harness and an AI model, acting together to read/write code, run commands, and complete tasks. When we say "AI coding assistant," we mean a coding agent.

### Notes on tools we won't cover here

- **ChatGPT**: OpenAI's Codex has an official VS Code extension ([openai.chatgpt](https://marketplace.visualstudio.com/items?itemName=openai.chatgpt)) that works much like Claude Code — an agent sidebar that reads your files, edits code, and runs terminal commands.  (Depending on your account's setting, you may also have access to OpenAI models within GitHub Copilot Chat; see Option B.6).
- **Gemini**: Google's Antigravity also has an official VS Code extension with ([Google.google-antigravity](https://marketplace.visualstudio.com/items?itemName=Google.google-antigravity)) with agent mode. (Depending on your account's setting, you may also have access to Gemini models within GitHub Copilot Chat; see Option B.6).
- **VS Code's "Agents" window**: Recent versions of VS Code include an **Open in Agents** button in the title bar (and an "Agent Sessions" list in the Chat panel). This is a separate, *chat-first* VS Code window for starting and monitoring several agent sessions at once, potentially across multiple projects. In this workshop we will focus on the standard VS code view that is *code-first*, though you may want to explore this "Agents" window later.

> **This is a rapidly changing space!** It seems like every week a new model, harness, or IDE feature is released or revised.  The instructions here were finalized in early September 2026, so some details may have shifted by the time you read them.  If a step doesn't quite match what you see on screen, check the tool's official documentation (see [Useful Links](#useful-links)) and let the instructor know.  This is an exciting, and sometimes confusing, space to follow, and no one manages to stay current on every new model, harness, and feature.  Our goal isn't to cover everything — it's to help you find a setup that works for you, and to understand it well enough to adapt as the tools change.

## Safety

> **Important Note:** Claude Code and GitHub Copilot Chat can both run in an "agent mode" that reads, edits, and creates files — and can run terminal commands — on your behalf. Before you start installing anything, please read the points below so you know what these tools can actually do on your computer.  You can find more information in the materials for our companion workshop on *Getting Started Safely with AI Coding Agents* here : https://bit.ly/RCDS-agent-setup-9-26 

- **Ask before acting:** Each of these tools has a setting that pauses the agent and asks for your approval before it modifies a file or runs a command. At least while you're learning how these tools behave, keep this "ask before acting" setting turned on.  This setting is called **Manual permissions** in GitHub Copilot Chat (in the permissions picker at the bottom of the chat box) and **Manual** in Claude Code (in the mode indicator at the bottom of the prompt box).  It is the default in Copilot Chat, but newer versions of Claude Code may start in a different mode (such as **Auto**), so be sure to check and switch to **Manual**. This gives you a chance to review each proposed change *before* it happens, so you're never surprised by a file being edited, deleted, or a command running without your knowledge.

- **AI output can be wrong:** These tools can misunderstand what you asked for, invent functions or packages that don't actually exist, or write code that runs but is subtly incorrect or insecure. Treat every suggestion as a draft from a fast but fallible collaborator. Read and test AI-generated code before trusting it.

- **These agents are not limited to your open project folder:** Opening a single folder in VS Code does not sandbox an agent to that folder. Claude Code, and the agent mode of Copilot Chat, run as ordinary programs under your own user account — the same account you're logged into your computer with. That means they can read, write, or delete any file your account has permission to touch (e.g., other folders in your Documents, Downloads, or home directory), and terminal commands they run can do anything your normal terminal commands can do (install software, access the network, etc.). The "ask before acting" (Manual) setting is your main protection here, since it shows you the exact file path or command *before* it runs; always check that it's touching only what you expect.  One way you can guard against this is working with a container (e.g., [Docker Sandbox](https://www.docker.com/products/docker-sandboxes/)), though we will not cover this here.

- **Consider the "sandbox" option:** Both Claude Code and GitHub Copilot Chat have an optional sandbox mode that uses operating-system features to restrict what terminal commands run by the agent can do — for example, limiting file writes to your project folder and limiting network access to approved domains. This guards against a mistaken or malicious command (e.g., from a prompt injection) even if you approve it, and in some modes it lets sandboxed commands run without constant approval prompts. You can turn it on in each tool's settings (in Claude Code, type `/sandbox`; in Copilot Chat, set `chat.agent.sandbox.enabled` to `on`). Drawbacks: it is off by default, it may break some tools (e.g., Docker or `ssh`), it has some setup requirements (WSL2 or Linux packages, and Windows support is limited or experimental), it covers only terminal commands (not the agent's built-in file tools), and the agent can ask to run a command outside the sandbox. Copilot Chat also leaves network access open by default. See the docs for [Claude Code](https://code.claude.com/docs/en/sandboxing) and [Copilot Chat](https://code.visualstudio.com/docs/agents/run/agent-sandboxing) for details.

- **Your code and files may leave your machine:** When you use a cloud model (Claude, or a cloud model through GitHub Copilot Chat), the contents of files the agent reads, including any it opens on its own to gather context, are sent to that provider's servers. Avoid pointing cloud-based agents at proprietary, confidential, or otherwise sensitive codebases or data unless you've confirmed that's allowed. If keeping everything fully on your machine matters, use a local Ollama model instead (Option B).

- **Your data may be retained or used to train future models:** Beyond simply being transmitted to a provider's servers, cloud-based tools may retain your prompts and code, and depending on your account type, may use them to improve or train future models. Data-use terms often differ between consumer plans (e.g., Claude Pro/Max, GitHub Copilot Individual on the free tier) and paid business/API plans (e.g., Claude API accounts, GitHub Copilot Business/Enterprise), which more often include retention limits or training opt-outs. If this matters to you, check the specific data usage policy for your plan, or use a local Ollama model, where nothing ever leaves your machine.

- **Watch out for secrets and credentials:** Agents may read and include the contents of any file in their context, including ones you didn't intend to share, like `.env` files, config files with API keys, or credentials. Avoid keeping secrets in plaintext in a project an agent has access to, and double-check any command or file the agent wants to read or send before approving it.

- **Use git as a safety net:** Commit your work often (or work in a git repository from the start) so that if an agent makes an unwanted change, you can easily see what changed (`git diff`) and revert it (`git checkout`/`git restore`). This is good practice generally, but especially valuable when a tool is editing files on your behalf.

- **Be extra cautious with "auto-approve" / "yolo" modes:** Some of these tools offer a mode that skips the approval step entirely and lets the agent act fully autonomously. This can be convenient once you're experienced, but we recommend avoiding it for this workshop and until you have a good feel for how these agents behave.

# Installation instructions

See the [installation_instructions.md](installation_instructions.md) file for detailed instructions on how to install all the software for this workshop.

# Exercises

After you have installed all the software, see the [exercises/](exercises/README.md) directory for a series of exercises to try with your new tools (code completion, chat, agent mode, and reviewing changes with git).

# Usage Limits and System Requirements

<details>
<summary><b><i>👉 Click to show / hide</i></b></summary>

Cloud-based coding agents are metered and require an internet connection — running out of included usage can mean getting charged per token or being throttled until your quota resets, and you can't use them without a working connection. Local models have none of those constraints, but they do require your own hardware to be capable enough to run them well.

- **Claude Code:** Usage is tied to your Anthropic plan (Pro, Max, or pay-as-you-go API access). Each plan includes a set amount of usage; once you exceed it, you may be rate-limited or, on an API-based plan, billed per token. Keep an eye on your usage/billing page on the Claude/Anthropic Console so you're not surprised by a charge.

- **GitHub Copilot Chat:** Usage limits (including which models are available and how many "premium requests" you get) depend on your GitHub account type and plan. Check your usage under your GitHub account's Copilot settings, and be aware that some models may consume your quota faster than others.

- **Ollama (local models):** Since these models run entirely on your own computer, there are no usage limits and no per-token charges — the only constraints are your hardware's speed and memory (see the VRAM note in [Option B](installation_instructions.md#option-b-ollama-local-models-with-github-copilot-chat-harness)).

**Quick reference:**

| Tool | Account needed | Cost | Internet required? |
|------|-----------------|------|---------------------|
| Claude Code | Paid Anthropic account (Pro, Max, or API) | Usage-based; may bill per token if you exceed your plan's included usage | Yes |
| GitHub Copilot Chat | Free GitHub account (free tier is sufficient for this workshop) | Free tier available; paid tiers unlock more usage/models | Yes, unless routed to a local Ollama model (see [Option B.6](installation_instructions.md#b6-github-copilot-chat-with-ollama)) |
| Ollama (local models) | None | Free — but you supply the hardware (RAM/VRAM, disk space) | No, once models are downloaded |

</details>

<br/>

# Useful Links

<details>
<summary><b><i>👉 Click to show / hide</i></b></summary>

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

</details>

<br/>



# Attribution

This walkthrough was created by Aaron Geller with help from Claude (Anthropic).