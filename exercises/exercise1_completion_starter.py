"""
Starter file for Exercise 1: Code completion.

Work through the parts below IN ORDER.  Each part tells you where to place your
cursor and what to type.  See exercise1_code_completion.md for the full instructions.

This file is meant to be run from the exercises/ folder, so that penguins.csv can be found.
Delete or ignore anything the suggestions add that you don't want.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("penguins.csv")


# ============================================================================
# PART A: Comments to code
# ----------------------------------------------------------------------------
# Place your cursor at the end of the comment line below, press Enter, and wait
# a moment.  A grey suggestion should appear.  Press Tab to accept it, or keep
# typing to ignore it.
# ============================================================================

# print the mean body_mass_g for each species



# Now write your own comment on the next line asking for something different
# (for example: how many penguins live on each island?), press Enter, and see what you get.



# ============================================================================
# PART B: Function signatures and docstrings
# ----------------------------------------------------------------------------
# Place your cursor on the empty line AFTER the docstring below, and wait.
# (The docstring is the text in triple quotes; it tells the model what the
# function should do.)  Accept the suggestion, then test the function.
# ============================================================================

def mean_and_std(values):
    """Return the mean and the standard deviation of a list of numbers."""



# Test your function here, e.g., with a few numbers whose answer you know:
# print(mean_and_std([1, 2, 3, 4, 5]))
# Then try it on a column of the data:
# print(mean_and_std(df["flipper_length_mm"].dropna()))


# Now delete the docstring above and replace it with just a function name that
# describes what it does (e.g., rename the function to  def mean_and_std_of_column(df, column):)
# and see if the suggestion still makes sense.



# ============================================================================
# PART C: Pattern continuation
# ----------------------------------------------------------------------------
# Two histograms are already written below.  Place your cursor at the end of the
# last line and press Enter.  Does the model predict the third histogram
# (for flipper_length_mm)?  Press Enter again after accepting; does it
# keep going with the fourth (body_mass_g)?
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(8, 6))

axes[0, 0].hist(df["bill_length_mm"].dropna())
axes[0, 0].set_xlabel("bill_length_mm")

axes[0, 1].hist(df["bill_depth_mm"].dropna())
axes[0, 1].set_xlabel("bill_depth_mm")

