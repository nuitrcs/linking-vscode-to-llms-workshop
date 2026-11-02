# Exercise 4: Reviewing changes with `git diff`

When an agent edits your files, **you** are responsible for checking what it changed.  VS Code can show you changes visually, two ways: in the chat while the agent is editing (before you accept), and through `git` (after).  In this exercise you will learn to use both, first on the bug fix from Exercise 3, and then on a new modification.

Throughout this exercise, remember that `git` is your safety net: as long as your starting point is committed, you can always see what changed and go back.

**Setup:** open your **working copy** of the exercises (see [Setup](README.md#setup-make-your-own-working-copy)) in VS Code.  It is a `git` repository, with `penguin_summary_buggy.py` saved in the original, buggy form in your "Starting point" commit.

As in Exercise 3, use **Agent** mode (not Ask mode, which cannot edit files) and keep **Manual** permissions on (Manual permissions in Copilot Chat, Manual in Claude Code), so that the agent's edits are shown to you for approval.  Parts B and D rely on this: the review happens *before* you accept.


## Part A: Look at the bug fix from Exercise 3

If you haven't done Exercise 3 Task 4 yet, do it now and come back.  After you have asked an agent to fix the bug, you can look at what it changed:

1. Click the **Source Control** icon in the left sidebar (it looks like a branching graph), or press `Ctrl+Shift+G`.  Under **Changes** you should see `penguin_summary_buggy.py` marked with an `M` (modified).
2. Click on the file name.  VS Code opens a **side-by-side diff**: the original (committed) version on the left, and your current version on the right.  Lines removed are highlighted in red, and lines added are highlighted in green.  Within a changed line, the specific characters that changed are highlighted more strongly.
3. Look carefully:
   - Did the agent change the line you expected (the `/ 100` becoming `/ 1000`)?
   - Did it change anything else?  Extra changes (new comments, renamed variables, reformatted lines) are not necessarily wrong, but you should know about them.
4. Click the **Inline view** toggle (the icon with two horizontal lines at the top right of the diff editor, or the `⋯` menu → **Inline View**) to see the same changes in a single column.  Which do you prefer?
5. Now use the same view to answer: does the agent's explanation of what it changed match the diff?




## Part B: Review edits *before* you accept them

Many chat tools show an agent's edit in the editor for you to approve or reject.  Here you will ask for a new change and review it in that view.

First, make sure your starting point is committed.  If you changed the file in Part A, commit the fix:
```
git add penguin_summary_buggy.py
git commit -m "Fix mass unit conversion"
```

Now ask your agent (in agent mode, with the file open) for a modification:
```
In penguin_summary_buggy.py, add a column to the output table showing the mean flipper length in mm for each species.  Also add a short docstring comment to explain each of the main steps.  Do not change anything else.
```

While the agent works, notice how the changes appear:

1. **In the editor:** the proposed changes are highlighted, with green for added lines and red for removed lines.  In Copilot Chat, there are **Keep** and **Undo** buttons (and the chat shows "1 file changed").  In Claude Code, a diff view opens asking whether you want to accept the edit.
2. **Review each change** before accepting.  You can usually step through the changes one at a time using the arrows in the editor.  Is each change something you asked for?
3. **Reject one change.**  Pick one thing you don't like (for example, a comment you think is unnecessary) and use **Undo** (Copilot) or edit it out yourself to reject it, then **Keep** or accept the rest.  This is a good habit: you don't have to accept the agent's work all-or-nothing.
4. Run the script.  Does it still work?  Does it show the new column?  Does the resulting table look correct?  (Hint: Adelie penguins have an average flipper length of about 190 mm.)


## Part C: Review the result with git

After accepting the edits, go back to the **Source Control** view.

1. Click on the file to open the diff again.  Compare this to what you saw in the chat.  Do they agree?
2. In the diff, hover over a changed block, and look in the gutter (the narrow strip between the two sides of the diff) for the buttons to **stage** or **revert** that single block.  Try reverting just one change, and then check that the script still runs.
3. When you are happy with the file, stage it with the `+` button next to the file name, type a short commit message in the box above the file list (for example, "Add mean flipper length column"), and click **Commit**.
4. Optional: open the **Timeline** section at the bottom of the Explorer sidebar while the file is open, to see the commit history for the file.  Click a commit to see what changed in that commit.


## Part D: Undo a change you don't like

1. Ask the agent for a larger, more open-ended change:
   ```
   Refactor penguin_summary_buggy.py to make it cleaner and easier to read.
   ```
2. Without accepting anything yet, review the proposed changes.  How big are they?  Is it clear that each change is an improvement?
3. Accept the changes, then look at the diff in Source Control.  Do you want to keep them?
4. If not, you can throw away **all** changes since your last commit:  right-click the file under **Changes** and choose **Discard Changes**, or in the terminal run
   ```
   git restore penguin_summary_buggy.py
   ```
   Check that the file is back to the committed version.

This is the safety net: because you committed before asking the agent for the change, there is no risk in trying a big change.  (Be careful: discarding changes cannot be undone!)


## Reflection questions

- What did the diff show you that the agent's chat summary did not?
- Did the agent ever change something you did not ask for?  How easy was that to notice without the diff view?
- Why is it helpful to commit *before* asking the agent to make changes?
- How would you review a change that touched ten files instead of one?
