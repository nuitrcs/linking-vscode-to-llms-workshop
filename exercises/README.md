# Test your LLM agents 

This file provides a series of exercises meant to test your LLM coding agents.   Each exercise uses the same data file and asks for increasingly harder tasks.  For each exercise, I provide a starting prompt.  Please start with this, but feel free to modify the prompt afterwards as necessary to try to achieve the desired result.  Try these exercises with different LLM agents (both local and cloud) to get a better understanding of their capabilities and limitations.

These exercises use the standard [Palmer Penguins dataset](https://allisonhorst.github.io/palmerpenguins/), i.e. the `penguins.csv` file included here.  Each exercise asks the LLM to work in Python.

> **Note:** In the example prompts below, you will see `@` symbols.  If you are using the Continue extension in VS Code, these are indications to use the `@` feature (you will have to manually replace that portion of the prompt below within the chat).  If you are not using Continue, you should delete the `@` symbol. 


## Exercises

1. Ask an agent to write a Python script to read in a csv file with data and generating a simple scatter plot.  This exercise will test the agent's ability write working Python code and to use Tools to create a file.  The resulting figure should look similar to the figure at the top of the [R palmerpenguins](https://allisonhorst.github.io/palmerpenguins/) website, though without the fit lines. 

```
I have a CSV file called penguins.csv. Write a Python script that:
- Reads this CSV into a pandas DataFrame
- Creates a scatter plot of the columns flipper_length_mm (x-axis) vs bill_length_mm (y-axis)
- Colors the points by the column species
- Adds a legend, axis labels, and a title
- Saves the figure as penguins_scatter_plot.png

Use seaborn and pandas. Keep the script simple and well-commented.

Save the script in a new file called create_penguin_scatter.py in my @local_agent_test directory.
```

2. Ask the agent to add error handling to that existing script.  This exercise will test the agent's ability to interpret an existing Python script, make choices on how to implement tests, and use Tools to modify a file.  If you are using a local ollama LLM, you may benefit from starting a new conversation for this exercise to free up more context space.  Evaluate the resulting code yourself, and run it to check if the error handling works. 
```
Here is a Python script that reads a CSV and generates a scatter plot: @create_penguin_scatter.py

Modify the script to add error handling for these cases:
- The CSV file does not exist or the path is wrong
- Expected columns are missing from the CSV
- Rows with missing values in the relevant columns

The script should print a clear, helpful error message for each case and 
exit gracefully rather than crashing. Do not change the plotting logic.
```

Alternative prompt with less guidnace on what error handling to include:
```
Here is a Python script that reads a CSV and generates a scatter plot: @create_penguin_scatter.py .

Modify the script to add error handling.  The script should print a clear, helpful error message 
for each case and exit gracefully rather than crashing. Do not change the plotting logic.
```


3. Ask for a figure that shows a boxplot plus runs a t-test and annotates the plot with the p-value and significance stars. The requires combining scipy, matplotlib, and some conditional logic. Small models (e.g., local ollama LLMs) will likely fail on this task in a variety of ways.  You can compare the result from your test with Claude's result that I generated and saved in the `exercise3_from_Claude/` directory.
```
I have a CSV file called penguins.csv. I want to compare Adelie vs Chinstrap penguins.

Write a Python script that:
- Reads the CSV and filters to only Adelie and Chinstrap species
- Creates a boxplot of flipper_length_mm for each species
- Runs an independent samples t-test (scipy.stats.ttest_ind) comparing 
  the two groups
- Annotates the plot with the p-value and significance stars using this 
  convention: *** p<0.001, ** p<0.01, * p<0.05, ns p>=0.05
- Draws a horizontal bracket above the two boxes with the annotation 
  centered over it
- Saves the figure as penguins_boxplot_ttest.png

Use pandas, matplotlib, and scipy. Add comments explaining each step.

Save the script in a new file called create_penguin_boxplot_stats.py in my @local_agent_test directory.

```