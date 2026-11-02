# Exercise 1: Code completion

In **code completion** (also called "inline suggestions"), the AI predicts what you are about to type and shows it as faint grey "ghost text" in the editor.  You press `Tab` to accept it, or just keep typing to ignore it.  There is no chat window and no conversation: the model reads the code around your cursor and guesses what comes next.

> **GitHub account required.** Inline code completion in this workshop is provided by **GitHub Copilot**, which needs you to be signed in to GitHub (the free tier is enough).  **If you don't have a GitHub account, please find someone nearby who does and work through this exercise together on their machine.**

> **What about local models?**  Ollama models do *not* power the inline suggestions in GitHub Copilot (local models are available in Copilot's chat and agent modes only).  If you want to use Ollama for code completion (and therefore keep everything local) you can use the **Continue** extension, which also has chat and agent modes.  We do not teach Continue in this workshop.


## Setup

1. Make sure you are signed in to GitHub in VS Code (click the **Accounts** icon at the bottom of the left sidebar).
2. Look at the bottom-right status bar for the **Copilot icon**.  Click it to confirm that inline suggestions are enabled, and enabled for Python.  If you see a warning, follow the prompts to sign in or enable completions.
3. Open your **working copy** of the exercises (see [Setup](README.md#setup-make-your-own-working-copy)) in VS Code, then open the file `exercise1_completion_starter.py`.  This file contains all the starting code for this exercise.  (It reads `penguins.csv`, so the folder must be open so the file can be found.)

**Keyboard shortcuts for suggestions** (use `Option` instead of `Alt` on macOS):

| Key | What it does |
|-----|--------------|
| `Tab` | Accept the whole suggestion |
| `Ctrl+→` (`Cmd+→` on macOS) | Accept the suggestion one word at a time |
| `Esc` | Dismiss the suggestion |
| `Alt+]` / `Alt+[` | Show the next / previous alternative suggestion |

A suggestion may take a second to appear.  If nothing shows up, try typing a character and deleting it, or press `Alt+\` to ask for a suggestion manually.


## Part A: Comments become code

Find **Part A** in the starter file.

1. Click at the end of the comment line `# print the mean body_mass_g for each species`, and press `Enter`.  Wait a moment.  Grey text should appear.
2. Read the suggestion *before* you accept it.  Is it what you wanted?  Press `Tab` to accept it, then run the file (the play button at the top right, or `python exercise1_completion_starter.py` in the terminal).  Did it work?
3. Press `Alt+]` a few times before accepting to see whether the model offers other ways to write the same thing.
4. Write your own comment on the next blank line asking for something different (for example, "how many penguins live on each island?"), press `Enter`, and see what you get.

**Try this:** Make the comment vaguer (`# summarize the data`) and then more specific (`# print the mean and median body_mass_g for each species and sex, sorted from largest to smallest`).  How does the suggestion change?


## Part B: Function signatures and docstrings

Find **Part B** in the starter file.  There is a function named `mean_and_std` with a docstring that says what it should do (return the mean and the standard deviation), but no code.

1. Click on the empty line after the docstring, indent with `Tab`, and wait for a suggestion.
2. Accept the suggestion and test it.  Remove the `#` at the start of the test lines below the function, and run the file.  For `mean_and_std([1, 2, 3, 4, 5])` you should get a mean of 3.0 and a standard deviation of about 1.58 (sample) or 1.41 (population).
3. Notice **which kind of standard deviation** the model chose.  Did it use `numpy`, `pandas`, or the `statistics` module?  Did it add an `import` at the top of the file?  Did it handle the missing values (`NaN`) in the penguin data?  If the model made a choice you didn't expect, how could you change your docstring so that it would make a different choice?

**Takeaway:** the docstring and the function name are your "prompt".  Clearer descriptions give better suggestions.


## Part C: Continuing a pattern

Find **Part C** in the starter file.  Two of four histograms are already written.

1. Click at the end of the last line (`axes[0, 1].set_xlabel("bill_depth_mm")`) and press `Enter` twice.  Does the model predict the third histogram, using the next numeric column (`flipper_length_mm`), and the right position in the grid (`axes[1, 0]`)?
2. Accept it, press `Enter` twice again, and see if it completes the fourth (`body_mass_g`, `axes[1, 1]`).
3. Add `plt.show()` at the end and run the file to check the result.

This is where code completion shines: repetitive code with a clear pattern.


## Reflection questions

- What information does the model seem to use?  (Hint: try deleting the `import` lines at the top of the file, or renaming `df` to `data`, and see how the suggestions change.)
- Were there times when the suggestion looked right but was subtly wrong?  How did you notice (or how could you have missed it)?
- How is this different from asking in the chat window?  When would you prefer one over the other?
- Did you ever accept a suggestion without reading it?  Why is that risky?
