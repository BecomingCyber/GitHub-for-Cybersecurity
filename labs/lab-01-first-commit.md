# Lab 01: Your First Cybersecurity Git Commit

> **Simulation only:** This exercise uses fictional information. Do not connect it to real production systems or include real credentials, sensitive logs, or personal information. The example address is a private RFC1918 address.

## 1. Objective

Practice checking repository status, creating and reviewing a fictional investigation note, staging a file, committing the change, and reading Git history.

## 2. Scenario

You are a junior SOC analyst documenting a simulated alert about repeated failed login attempts. You will create a short Markdown note in your local learning repository. This scenario is not a real investigation and does not represent production experience.

The fictional details are:

```text
Incident ID: LAB-001
Alert Type: Repeated Failed Login Attempts
Source IP: 192.168.10.25
Target Account: lab-user
Failed Attempts: 12
Status: Under Investigation
```

## 3. Prerequisites

- Git is installed and available in PowerShell.
- You have opened your local learning repository in VS Code.
- Open the VS Code integrated terminal with **Terminal > New Terminal**. Confirm the terminal is in the repository root before running commands.
- This lab creates `investigation-notes.md` in the repository root. If `git status` already lists changes, review them and do not stage unrelated work. In this workspace, the root README may already have a change; leave it alone during this lab.

## 4. Step 1: Check Repository Status

**Command:**

```powershell
git status
```

**What to expect:** If the repository has no pending changes, Git reports that the working tree is clean. If there are pre-existing changes, Git lists them. Do not assume existing changes belong to this lab, and do not stage them.

## 5. Step 2: Create `investigation-notes.md` Using PowerShell

In the VS Code PowerShell terminal, run this command block from the repository root. It creates a Markdown file containing only the fictional details above.

```powershell
@'
# Simulated Investigation Notes

Incident ID: LAB-001
Alert Type: Repeated Failed Login Attempts
Source IP: 192.168.10.25
Target Account: lab-user
Failed Attempts: 12
Status: Under Investigation
'@ | Set-Content -Path .\investigation-notes.md -Encoding utf8
```

`Set-Content` writes the text to the named file. Running this command again replaces that file's contents, so use it only for this lab note.

## 6. Step 3: Run `git status` Again

```powershell
git status
```

Git should list `investigation-notes.md` as an **untracked** file. It is untracked because it is new and has not yet been added to Git's staging area. If pre-existing files are listed too, leave them unchanged and unstaged.

## 7. Step 4: Review the File

Review the new note in VS Code, or print it in PowerShell:

```powershell
Get-Content .\investigation-notes.md
```

Confirm that all details are fictional, the source is a private RFC1918 address, and no real credentials, production logs, or personal information have been included. `git diff` does not display a new untracked file until it is staged.

## 8. Step 5: Stage the File

**Command:**

```powershell
git add investigation-notes.md
```

This selects only `investigation-notes.md` for the next commit. It does not commit or upload the file.

## 9. Step 6: Run `git status` Again

```powershell
git status
```

Git should show `investigation-notes.md` under changes to be committed. Git now has a staged snapshot of the file for the next commit. The file remains in your working directory; staging does not move it. Confirm that no unrelated file was staged.

## 10. Step 7: Review Staged Changes

**Command:**

```powershell
git diff --staged
```

Review the displayed addition line by line. It should contain only the fictional note. Stop and correct the staged content if you see anything unexpected or sensitive. You can edit the file and run `git add investigation-notes.md` again to stage the updated version.

## 11. Step 8: Create the Commit

After confirming the staged diff is correct, create a local commit:

```powershell
git commit -m "Add simulated failed login investigation notes"
```

The commit message briefly describes the checkpoint. This command records staged changes in local history. It does not push anything to GitHub.

## 12. Step 9: Review History

Run both commands:

```powershell
git log
```

```powershell
git log --oneline
```

`git log` shows detailed commit information. `git log --oneline` shows a compact summary. Look for the message `Add simulated failed login investigation notes`.

## 13. Step 10: Confirm Repository Status

```powershell
git status
```

If the lab was the only pending change, the expected result includes:

```text
nothing to commit, working tree clean
```

If other changes existed before you started, Git may still list them. That does not mean the lab commit failed. Do not commit unrelated work just to make the repository clean.

## What Just Happened?

```text
Working Directory
        |
        v
  Untracked File
        |
        | git add investigation-notes.md
        v
  Staging Area
        |
        | git commit -m "..."
        v
      Commit
        |
        v
   Git History
```

You created the file in the working directory. Git identified it as untracked. `git add` staged the file, and `git commit` saved that staged version in the local repository history.

## Reflection Questions

1. What information did `git status` provide before and after you staged the note?
2. Why did `git diff` not show the contents of the new untracked file before staging?
3. What did `git diff --staged` let you review before making the commit?
4. Why is it important to stage only the intended investigation note?
5. Does creating this local commit send the note to GitHub? How can you tell?

## Final Challenge

Change the note's status from `Under Investigation` to `Closed - Simulated Activity`. Determine which Git commands you would use to inspect the change, stage only this file, review the staged version, and create a second commit. Do not push the change as part of this challenge.

<details>
<summary>Hints</summary>

- Edit the status line in VS Code, then check the repository state.
- One command shows unstaged edits in a tracked file.
- Stage `investigation-notes.md` by name, then inspect the staged patch.
- Save the staged update with a new commit message that describes the status change.

</details>
