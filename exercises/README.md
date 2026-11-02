# Exercises

Work through these exercises after you have installed the software in the [installation instructions](../installation_instructions.md).  The exercises go from the least to the most autonomy for the AI.

1. [Code completion](exercise1_code_completion.md): ghost-text suggestions as you type (needs a GitHub account; starter file: [exercise1_completion_starter.py](exercise1_completion_starter.py)).
2. [Chat](exercise2_chat.md): ask the model to explain code and data, without any edits.
3. [Agent mode](exercise3_agent.md): ask the agent to write, modify, and fix code (results of the Claude agent are in [exercise3_results_from_Claude/](exercise3_results_from_Claude/); these are for comparison, not new exercises).
4. [Reviewing changes with git diff](exercise4_git_diff.md): inspect exactly what the agent changed.

## Setup: make your own working copy

Several exercises ask an AI to edit files, and exercise 4 uses git to review those edits.  So that your edits never get mixed up with the workshop repository, work in your own copy of this folder, **outside** the workshop repository.

1. Copy this `exercises/` folder to somewhere else on your computer, for example your Documents folder, and give it a new name such as `workshop-exercises`.  (Use your file explorer, or in a terminal: `cp -r exercises ~/Documents/workshop-exercises`.)
2. In VS Code, open the new folder (**File → Open Folder**).
3. Open a terminal in VS Code (`` Ctrl+` ``) and make a git repository from your copy, saving the starting point:
   ```bash
   git init
   git add .
   git commit -m "Starting point"
   ```
   If git says "Please tell me who you are", run these two commands (with your own name and email, which stay on your computer), then repeat the `git commit`:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

Use this working copy for all four exercises.  You never need to push anything.

The data are from the [Palmer Penguins dataset](https://allisonhorst.github.io/palmerpenguins/), in `penguins.csv`.  All exercises use Python.
