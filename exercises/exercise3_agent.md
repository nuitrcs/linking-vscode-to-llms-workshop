# Exercise 3: Agent mode

In the previous exercise (chat), the model only *talked*.  In **agent mode**, the model can also *act*: it can create and edit files, and run terminal commands, to complete a task.  That makes agents much more powerful, and much more important to supervise.

> **Before you start:** keep the "ask before acting" setting on, which is called **Manual permissions** in Copilot Chat and **Manual** in Claude Code (see the Safety section of the main workshop README).  Each time the agent proposes to edit a file or run a command, **read** the proposal before you approve it.  Notice whether the agent only touches the files you expect.

**Setup:** open your **working copy** of the exercises (see [Setup](README.md#setup-make-your-own-working-copy)) in VS Code, so that the agent works in that folder and can find `penguins.csv`.  In Copilot Chat, choose **Agent** mode (not Ask).  In Claude Code, check the mode indicator at the bottom of the prompt box, and switch it to **Manual** if it shows something else.

> **Two different settings, both called "ask":**
> - **Ask mode** (Copilot Chat's mode picker) is chat-only: the model *cannot* edit files.  This is what you used in Exercise 2.  For this exercise, and for Exercise 4, switch to **Agent** mode.  (To go back to chatting only, switch the mode picker back to Ask.)
> - **Manual permissions** (Copilot Chat's permissions picker) or **Manual** (Claude Code's mode indicator) means the agent *can* edit, but pauses for your approval first.  Keep this on for every exercise.  Do **not** use higher levels such as **Allow all**, **Autopilot**, **Auto**, **Edit automatically**, or **Bypass permissions**.

This file provides a series of tasks meant to test your LLM coding agents.   Each task uses the same data file and asks for increasingly harder things.  For each task, I provide a starting prompt.  Please start with this, but feel free to modify the prompt afterwards as necessary to try to achieve the desired result.  Try these exercises with different LLM agents (both local and cloud) to get a better understanding of their capabilities and limitations.

These exercises use the standard [Palmer Penguins dataset](https://allisonhorst.github.io/palmerpenguins/), i.e. the `penguins.csv` file included here.  Each exercise asks the LLM to work in Python.


## Tasks

1. **Task 1.** Ask an agent to write a Python script to read in a csv file with data and generate a simple scatter plot.  This exercise will test the agent's ability to write working Python code and to use Tools to create a file.  The resulting figure should look similar to the figure at the top of the [R palmerpenguins](https://allisonhorst.github.io/palmerpenguins/) website, though without the fit lines. 

    ```
    I have a CSV file called penguins.csv. Write a Python script that:
    - Reads this CSV into a pandas DataFrame
    - Creates a scatter plot of the columns flipper_length_mm (x-axis) vs bill_length_mm (y-axis)
    - Colors the points by the column species
    - Adds a legend, axis labels, and a title
    - Saves the figure as penguins_scatter_plot.png

    Use seaborn and pandas. Keep the script simple and well-commented.

    Save the script in a new file called create_penguin_scatter.py.
    ```

    (In order to run the script your model generates, you will need Python and the packages the script calls, likely `pandas`, `matplotlib` and `seaborn`.  See step 4 of the [installation instructions](../installation_instructions.md) if you haven't installed these yet.  If the agent offers to install packages for you, decline, and install them yourself.)

2. **Task 2.** Ask the agent to add error handling to that existing script.  This exercise will test the agent's ability to interpret an existing Python script, make choices on how to implement tests, and use Tools to modify a file.  If you are using a local Ollama LLM, you may benefit from starting a new conversation for this exercise to free up more context space.  Evaluate the resulting code yourself, and run it to check if the error handling works. 
    ```
    I have a Python script named create_penguin_scatter.py that reads a CSV file and generates a scatter plot.

    Modify the script to add error handling for these cases:
    - The CSV file does not exist or the path is wrong
    - Expected columns are missing from the CSV
    - Rows have missing values in the relevant columns

    The script should print a clear, helpful error message for each case and 
    exit gracefully rather than crashing. Do not change the plotting logic.
    ```

    Alternative prompt with less guidance on what error handling to include:
    ```
    I have a Python script named create_penguin_scatter.py that reads a CSV file and generates a scatter plot.

    Modify the script to add error handling.  The script should print a clear, helpful error message for each case and exit gracefully rather than crashing. Do not change the plotting logic.
    ```


3. **Task 3.** Ask for a figure that shows a boxplot plus runs a t-test and annotates the plot with the p-value and significance stars. This can be done with `scipy`, `matplotlib`, and some conditional logic. Small models (e.g., local Ollama LLMs) may fail on this task in a variety of ways.  You can compare the result from your test with Claude's result that I generated and saved in the `exercise3_results_from_Claude/` directory.
    ```
    I have a CSV file called penguins.csv. I want to compare Adelie vs Chinstrap penguins.

    Write a Python script that:
    - Reads the CSV and filters to only Adelie and Chinstrap species
    - Creates a boxplot of flipper_length_mm for each species
    - Runs an independent samples t-test (scipy.stats.ttest_ind) comparing the two groups
    - Annotates the plot with the p-value and significance stars using this convention: *** p<0.001, ** p<0.01, * p<0.05, ns p>=0.05
    - Draws a horizontal bracket above the two boxes with the annotation centered over it
    - Saves the figure as penguins_boxplot_ttest.png

    Use pandas, matplotlib, and scipy. Add comments explaining each step.

    Save the script in a new file called create_penguin_boxplot_stats.py.

    ```

4. **Task 4.** Find and fix a bug.  The file [penguin_summary_buggy.py](penguin_summary_buggy.py) in this folder prints a summary table for each penguin species, but it contains a bug.  This task tests whether the agent can run code, notice that the output is wrong, find the cause, and make a small, targeted fix.

    Start by running the script yourself to see its output:
    ```
    python penguin_summary_buggy.py
    ```
    Do you notice anything strange?  (Hint: look at the mean mass column.)

    (Your working copy has this original, buggy version saved in git from the setup step, so in the next exercise we will be able to see exactly what the agent changes.)

    Then ask your agent:
    ```
    The script penguin_summary_buggy.py prints a summary of the penguin data by species, but the output looks wrong.  Run it, find the bug, and fix it.  Explain what was wrong.  Make the smallest change that fixes the bug.
    ```

    Check the result: Did the agent find the real bug?  Did it change only the line that needed to change, or did it also "improve" other things you did not ask for?  Does the corrected output look reasonable (Adelie penguins weigh about 3.7 kg)?

    When the agent shows its edit to `penguin_summary_buggy.py`, read it, then accept it (**Keep** in Copilot Chat, or approve the edit in Claude Code).  Don't discard it.  **Keep the file with the agent's fix.  We will look at exactly what changed in the next exercise** ([Exercise 4: Reviewing changes with git diff](exercise4_git_diff.md)).
