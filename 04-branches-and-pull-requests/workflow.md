# Branch and Pull Request Workflow

This guide uses fictional cybersecurity documentation examples. Run commands from the repository root in PowerShell or the VS Code integrated terminal. The commands are examples for a learner to run in their own repository; they are not executed by this guide.

## Branch Commands

### `git branch`

- **What it does:** Lists local branches. The current branch is marked with `*`. With a name argument, it can create a branch, but this guide teaches `git switch -c` for the combined create-and-switch action because the intent is clearer.
- **When to use it:** To see which local branches are available before choosing where to work.
- **Cybersecurity example:** Check whether a branch for a fictional detection-documentation update already exists.
- **Expected result:** A list of local branch names, with an asterisk beside the current branch. A repository with no commits may not yet have a normal branch list.
- **Example:**

  ```powershell
  git branch
  ```

### `git branch --show-current`

- **What it does:** Prints the name of the current local branch.
- **When to use it:** Before editing, committing, or comparing work, to confirm you are on the intended branch.
- **Cybersecurity example:** Confirm that you are on `docs/update-incident-report`, not `main`, before editing a fictional incident note.
- **Expected result:** A branch name such as `main` or `docs/update-incident-report`. In some detached-HEAD situations, Git may print no branch name.
- **Example:**

  ```powershell
  git branch --show-current
  ```

### `git switch -c BRANCH-NAME`

- **What it does:** Creates a new local branch and switches to it. `-c` means create.
- **When to use it:** To start a focused change on a new branch based on your current commit.
- **Cybersecurity example:** Create a branch for updating fictional investigation documentation.
- **Expected result:** Git reports that it switched to the newly created branch. If the name already exists, Git reports an error rather than creating a duplicate.
- **Example:**

  ```powershell
  git switch -c docs/update-incident-report
  ```

### `git switch main`

- **What it does:** Switches the working tree to the existing local branch named `main`.
- **When to use it:** To return to the primary branch after your feature work is committed or safely saved elsewhere.
- **Cybersecurity example:** Return to the project baseline before starting another fictional detection-documentation update.
- **Expected result:** Git reports that it switched to `main`. Git may refuse if local changes would be overwritten; review and safely handle those changes first.
- **Example:**

  ```powershell
  git switch main
  ```

### `git checkout`

- **What it does:** This older multi-purpose command can switch to an existing branch with `git checkout BRANCH-NAME`, create and switch to a branch with `git checkout -b BRANCH-NAME`, and restore files with other options. Its multiple roles can be confusing for beginners.
- **When to use it:** You may encounter it in older instructions or scripts. For creating and switching branches in new learner workflows, prefer `git switch`.
- **Cybersecurity example:** Recognize `git checkout main` in an older project guide as a branch-switching command, while using `git switch main` in your own practice.
- **Expected result:** With `git checkout main`, Git attempts to switch to the existing local `main` branch, subject to uncommitted-change checks.
- **Example:**

  ```powershell
  git checkout main
  ```

## Review and Commit Commands

### `git status`

- **What it does:** Shows the current branch and staged, unstaged, and untracked changes.
- **When to use it:** Before and after editing or staging so you know what files will be part of a commit.
- **Cybersecurity example:** Check that only the fictional documentation file is changed before preparing a review.
- **Expected result:** A summary of the branch and file changes, or a message that the working tree is clean.
- **Example:**

  ```powershell
  git status
  ```

### `git diff`

- **What it does:** Shows unstaged changes to tracked files compared with the index. It does not normally show untracked file contents.
- **When to use it:** To review edits to a tracked incident template before staging them.
- **Cybersecurity example:** Inspect a wording change to a fictional report and confirm no sensitive details were added.
- **Expected result:** A line-by-line diff for unstaged tracked-file changes, or no output if none are present.
- **Example:**

  ```powershell
  git diff
  ```

### `git add FILE`

- **What it does:** Adds the current version of the named file's changes to the staging area for the next commit. Use a path relative to the repository root or current directory.
- **When to use it:** After reviewing a change, when you want to include that file in the next commit.
- **Cybersecurity example:** Stage only the fictional incident report you have reviewed, not unrelated files.
- **Expected result:** Usually no output. `git status` will list the staged change.
- **Example:**

  ```powershell
  git add .\incident-notes.md
  ```

### `git diff --staged`

- **What it does:** Shows the staged changes compared with the latest commit. It is also accepted as `git diff --cached`.
- **When to use it:** Before committing, to inspect exactly what is currently prepared for the next commit.
- **Cybersecurity example:** Check the staged incident-note patch for unintended information before recording it.
- **Expected result:** A line-by-line diff of staged changes, or no output if the staging area has no changes.
- **Example:**

  ```powershell
  git diff --staged
  ```

### `git commit -m "MESSAGE"`

- **What it does:** Saves the staged snapshot as a new commit in the current branch's local history. The message summarizes the change.
- **When to use it:** After reviewing the staged diff and confirming it contains only the intended content.
- **Cybersecurity example:** Record a focused update to fictional incident documentation.
- **Expected result:** Git creates a commit and prints its identifier and summary. Unstaged changes are not included.
- **Example:**

  ```powershell
  git commit -m "Improve simulated incident documentation"
  ```

### `git log --oneline`

- **What it does:** Shows a compact summary of commit history, with one commit per line.
- **When to use it:** To review the recent commits on the current branch.
- **Cybersecurity example:** Confirm that a documentation improvement has a clear entry in the branch history.
- **Expected result:** A list of short commit identifiers and their messages, newest first.
- **Example:**

  ```powershell
  git log --oneline
  ```

## Compare Changes

### `git diff main..BRANCH-NAME`

- **What it does:** Compares the file trees at the tips of the two named branches. It shows how the second branch's content differs from `main`; it is not a list of commits between branches.
- **When to use it:** To review the content difference between your proposed branch and the local `main` branch before opening a pull request.
- **Cybersecurity example:** Inspect all changes in `docs/update-incident-report` relative to `main` and confirm the branch contains only the intended fictional documentation update.
- **Expected result:** A line-by-line patch for content differences. If the branch tips have identical content, Git prints no diff.
- **Example:**

  ```powershell
  git diff main..docs/update-incident-report
  ```

The two-dot form for `git diff` compares the named endpoint trees. This differs from two-dot notation in commands such as `git log`, where it selects a commit range.

## A Safe Local Branch Workflow

This example prepares a documentation change locally. It does not merge it or publish it:

```powershell
git switch -c docs/update-incident-report
```

Make a safe documentation change in a fictional Markdown file, then review it:

```powershell
git status
git diff
```

Stage only the file you reviewed, inspect the staged patch, and commit it:

```powershell
git add .\incident-notes.md
git diff --staged
git commit -m "Improve simulated incident documentation"
```

The commit stays on the current feature branch. To return to the primary branch after the work is safely committed:

```powershell
git switch main
```

Merging should happen only after the appropriate review and checks. In a GitHub collaboration workflow, the next step is usually to push the branch and open a pull request. This guide does not automatically run a merge or publish the branch.

## Local Branch vs Remote Branch

A **local branch** is a branch name in your local repository. A **remote branch** is a branch reference associated with a remote repository, such as `origin/docs/update-incident-report`. A local branch and a remote branch are separate references, even when they point to the same commit.

To share a local branch for the first time, a learner may use:

```powershell
git push -u origin BRANCH-NAME
```

Replace `BRANCH-NAME` with the actual branch name. The `-u` option sets the upstream tracking relationship for later push and pull commands. Verify the remote and review the content before running a push. This is documentation only; no push is performed here.

## After a Pull Request Is Merged

After a pull request has been merged on GitHub, update the local `main` and remove the local feature branch when it is no longer needed:

```powershell
git switch main
git pull
git branch -d docs/update-incident-report
```

The `git pull` updates local `main` from its configured upstream. The safe `-d` option deletes the local branch only if Git considers it fully merged. Deleting a local branch does not automatically delete the remote branch. GitHub may offer to delete the remote branch after merge, or an authorized user can remove that remote branch separately.

## Beginner Troubleshooting

### The branch already exists

`git switch -c docs/update-incident-report` cannot create a branch with a name that is already in use locally. List branches with `git branch` and decide whether to switch to the existing branch or choose another clear name. Do not delete it until you know it is no longer needed.

### You are on the wrong branch

Check with `git branch --show-current`. If you have uncommitted changes, review and save them before switching. Switch only after confirming the intended destination, for example with `git switch docs/update-incident-report` or `git switch main`.

### Uncommitted changes block branch switching

Git may prevent a switch if local changes would be overwritten. Run `git status` and review `git diff`. Commit the work on the correct branch, or use an intentional stash workflow if you understand it. Do not discard work just to make the switch succeed.

### A merge conflict appears

Read the conflict markers and compare both versions. Ask the relevant contributor if the intended result is unclear, especially for detection or response logic. Edit the file to the agreed result, remove conflict markers, and review the complete result before continuing. A conflict is a normal situation when changes overlap.

### Git says the branch is not fully merged

`git branch -d BRANCH-NAME` refuses deletion when Git does not consider the branch fully merged. Switch to the appropriate target branch, check the pull request and history, and confirm whether the work was merged or is still needed. Do not default to force deletion; it may discard a branch reference to work that has not been integrated.
