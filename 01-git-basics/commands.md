# Git Commands for Cybersecurity Learners

Run these commands in the VS Code integrated terminal or another PowerShell window. Start in the repository folder. Examples use fictional documentation and scripts. Do not use real sensitive data in practice files.

## Everyday Commands

### `git status`

- **What it does:** Shows the current branch and whether files are untracked, modified, staged, or committed with no pending changes.
- **When to use it:** Before and after staging, and before creating a commit. It is a quick way to see what Git will include.
- **Example:**

  ```powershell
  git status
  ```

### `git add filename`

- **What it does:** Stages the current version of one named file for the next commit. Replace `filename` with a path relative to the repository root.
- **When to use it:** When you have reviewed a specific file, such as a fictional incident report, and want that change in the next commit.
- **Example:**

  ```powershell
  git add .\incident-notes.md
  ```

### `git add .`

- **What it does:** Stages new, changed, and deleted files under the current directory. If run from the repository root, this can stage many files throughout the project.
- **When to use it:** Only when you have checked all affected files and intentionally want to stage all eligible changes in the current directory tree.
- **Example:**

  ```powershell
  git add .
  ```

  Review the result with `git status` and `git diff --staged`. Prefer `git add filename` if you only intend to include a specific file.

### `git commit -m "message"`

- **What it does:** Records the staged changes as a new checkpoint in the local repository. The message briefly describes the change.
- **When to use it:** After reviewing the staged diff and confirming it contains only the intended, safe changes.
- **Example:**

  ```powershell
  git commit -m "Document simulated authentication alert"
  ```

### `git log`

- **What it does:** Shows commit history, including commit identifiers, authorship information configured in Git, dates, and messages.
- **When to use it:** To review how investigation documentation or a detection rule changed over time.
- **Example:**

  ```powershell
  git log
  ```

### `git log --oneline`

- **What it does:** Shows a compact, one-line summary for each commit.
- **When to use it:** To scan a repository's recent history quickly.
- **Example:**

  ```powershell
  git log --oneline
  ```

### `git diff`

- **What it does:** Shows line-by-line changes in tracked files that have not been staged. It does not show the staged changes.
- **When to use it:** To inspect edits to a tracked detection rule, script, or report before staging them.
- **Example:**

  ```powershell
  git diff
  ```

### `git diff --staged`

- **What it does:** Shows line-by-line changes that are in the staging area and are prepared for the next commit.
- **When to use it:** Immediately before committing, to confirm the exact staged content.
- **Example:**

  ```powershell
  git diff --staged
  ```

### `git clone`

- **What it does:** Downloads a remote repository and its available history to create a local working copy. It also configures the remote connection for later fetches and pushes.
- **When to use it:** When starting work with a repository hosted on GitHub or another Git service.
- **Example:**

  ```powershell
  git clone https://github.com/OWNER/REPOSITORY.git
  Set-Location .\REPOSITORY
  ```

  Replace `OWNER` and `REPOSITORY` with the actual public project path, or use the authorized clone URL provided by your organization.

### `git pull`

- **What it does:** Fetches commits from the configured remote and integrates them into the current branch. It updates your local branch with remote work.
- **When to use it:** Before continuing work when collaborators may have updated the branch, or when preparing to push your own work.
- **Example:**

  ```powershell
  git pull
  ```

  Review your status and resolve any reported conflicts carefully. Do not overwrite another analyst's work without understanding it.

### `git push`

- **What it does:** Sends local commits to the configured remote repository. It does not send changes that have not been committed.
- **When to use it:** When you are ready to share reviewed commits with the remote repository and have authorization to do so.
- **Example:**

  ```powershell
  git push
  ```

  For a new branch, Git may tell you to set an upstream branch. Follow your team's workflow and confirm you are pushing to the intended remote.

## `git diff` Versus `git diff --staged`

These commands inspect different parts of your changes:

- `git diff` shows unstaged edits in tracked files. These edits are in your working directory but are not yet selected for the next commit. A new untracked file is not shown by this command.
- `git diff --staged` shows changes already selected with `git add`. These are the changes that would be included in the next commit.

For a new file, stage it first with `git add filename`; then `git diff --staged` can display its contents as a proposed addition.

## Commands to Check Before You Commit

Use this review sequence:

```powershell
git status
git diff
git diff --staged
git status
```

1. The first `git status` identifies pending work and helps you notice unrelated files.
2. `git diff` reviews unstaged edits to tracked files.
3. `git diff --staged` reviews the exact staged patch for the next commit.
4. The final `git status` confirms which changes remain staged or unstaged.

A commit should contain only the changes you intended. Reviewing is especially important in cybersecurity because a note or script might expose sensitive details, include production data, alter a detection rule unexpectedly, or combine unrelated investigation work. Git history can retain sensitive content after a file is deleted, so inspect the patch for passwords, API keys, tokens, private keys, credentials, sensitive logs, personal information, and production secrets. Use only authorized, fictional training examples in this learning project.
