# Exercise 2: Chat (asking questions, no edits)

In this exercise you use the **chat** window as a knowledgeable tutor.  You will ask the model to explain code and data, but you will **not** ask it to change any files.

You can use any of the tools you installed.  The goal is not to find the "best" one, but to notice what each does well:
- **GitHub Copilot Chat:** open the chat panel and select **Ask** mode (not Agent mode).  Choose either a cloud model or your local Ollama model in the model picker.
- **Claude Code:** open the Claude Code panel.  You can ask questions without allowing any edits.

If you can, repeat the questions with two different models (for example, a local Ollama model and a cloud model) and compare the answers.

**Setup:** open your **working copy** of the exercises (see [Setup](README.md#setup-make-your-own-working-copy)) in VS Code.  We will use the Claude-generated script [Claude_create_penguin_boxplot_stats.py](exercise3_results_from_Claude/Claude_create_penguin_boxplot_stats.py) as a piece of code to ask about, and `penguins.csv` as the data.


## Part A: Explain this code

1. Open [Claude_create_penguin_boxplot_stats.py](exercise3_results_from_Claude/Claude_create_penguin_boxplot_stats.py) so that it is the active file in the editor.  Most chat tools will automatically include the active file as context.  (In Copilot Chat you can also type `#file` and select the file; in Claude Code, type `@` and select the file.)
2. Start with a high-level question:
   ```
   In a few sentences, what does this script do?
   ```
3. Ask for more detail:
   ```
   Walk me through this script step by step.  Assume I know basic Python but have never used scipy.
   ```
4. **Select a few lines** in the editor (for example, the lines that run the t-test and the lines that draw the bracket), then ask:
   ```
   Explain the selected lines.  Why is this done this way?
   ```
5. Ask a question about something you don't understand.  For example: "What is the difference between `df.dropna(subset=[...])` and `df.dropna()`?"

**Notice:** Does it matter whether you selected lines or only had the file open?  How does the answer change if you give the model a different level of background (for example, "explain this like I am new to programming" versus "I am an experienced R user, explain this in R terms")?


## Part B: Ask about the data

1. Open `penguins.csv` and look at it for a moment.  Then ask:
   ```
   What columns are in penguins.csv, and what does NA mean in this file?
   ```
2. Ask a question whose answer you can check:
   ```
   How many penguins in penguins.csv are missing a value for sex?
   ```
   A chat model that only *reads* the file may not count correctly!  Check the answer yourself (for example, in a Mac/Linux/Git Bash terminal, `grep -c ',NA,[0-9]*$' penguins.csv` counts the rows where `sex` is `NA`; or use pandas, where `df['sex'].isna().sum()` gives the answer).  Did the model get it right?  Did it say how it got its answer?
3. Ask a question that needs judgment:
   ```
   What analyses would be reasonable to run on this dataset to compare the three species?
   ```

**Notice:** Models are confident in tone whether or not they are right.  For anything with a definite numerical answer, ask the model to *write code* to find it (which you can run), or check it yourself.


## Part C: Review without editing

1. With the Claude script open, ask:
   ```
   What could go wrong when running this script?  List the most likely problems, but do not change any files.
   ```
2. Look at the list.  Which concerns are real?  Which are not relevant?  Did the model mention that the script requires `penguins.csv` to be in the current working directory?
3. Ask a follow-up:
   ```
   How would you make this script easier for someone else to reuse?  Describe the changes in words only.
   ```

**Notice:** The model *described* changes without making them.  In the next exercise, we will ask an agent to actually make changes to files.


## Reflection questions

- Which answers were most helpful?  Which seemed vague or incorrect?
- Did you notice any difference between the answers of the local and cloud models?
- How did the context you gave (open file, selected lines, `#file`/`@` references) change the answers?
- When would you use chat instead of code completion (Exercise 1), and when would you want an agent (Exercise 3)?
