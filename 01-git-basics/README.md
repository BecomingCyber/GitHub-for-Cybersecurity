# Module 01: Git Basics for Cybersecurity

Git helps you keep a clear history of changes to files. In cybersecurity work, that history can make investigation notes, scripts, and configuration changes easier to review and explain.

## Learning Objectives

By the end of this module, you should be able to:

- Explain the difference between Git and GitHub.
- Describe a repository, working directory, staging area, and commit.
- Recognize whether a file is untracked, modified, staged, or committed.
- Use `git status`, `git add`, `git commit`, `git log`, and `git diff` in a basic workflow.
- Explain what `git clone`, `git pull`, and `git push` do.
- Review changes for accidental sensitive information before creating a commit.

## Git and GitHub

**Git** is a version-control tool. It runs on your computer and records selected changes to files as commits. A commit is a saved checkpoint in the repository's history.

**GitHub** is a web service where Git repositories can be hosted and shared. It adds collaboration features such as pull requests, issues, and security tools. Git works locally without GitHub; GitHub is commonly used to share a repository with other people.

## The Basic Workflow

```text
Working Directory
        |
        v
   git status
        |
        v
     git add
        |
        v
  Staging Area
        |
        v
   git commit
        |
        v
 Local Repository
        |
        v
    git push
        |
        v
     GitHub
```

- **Working directory:** The project files you can see and edit in VS Code or File Explorer.
- **`git status`:** A report showing changes between your working directory, staging area, and latest commit. It identifies untracked files and staged or unstaged changes; a clean status means there are no pending changes.
- **`git add`:** Selects changes to include in the next commit. It copies the selected version of a change into the staging area; it does not upload the file.
- **Staging area:** The review list of changes prepared for the next commit.
- **`git commit`:** Saves staged changes as a checkpoint in your local repository, usually with a short message describing the change.
- **Local repository:** The Git history stored on your computer.
- **`git push`:** Sends local commits to a remote repository, such as one hosted on GitHub. It does not automatically include unstaged changes.

You can also use `git clone` to copy an existing remote repository to your computer, and `git pull` to bring newer remote commits into your local repository.

## File States in Plain Language

| State         | Meaning                                                                             | Example                                                        |
| ------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Untracked** | Git sees a new file but it is not yet included in version control.                  | You create `detection-notes.md` for a lab.                     |
| **Modified**  | A file Git already tracks has edits that are not staged.                            | You update a detection rule that is already in the repository. |
| **Staged**    | You selected the current version of a change for the next commit with `git add`.    | You stage a reviewed update to a fictional incident report.    |
| **Committed** | The staged change has been saved in the local repository history with `git commit`. | A checkpoint records a change to a lab script.                 |

Tracked files are files Git has been told to manage, usually by staging and committing them. A tracked file can still have staged or unstaged changes.

A committed change stays in your local history until you push it or otherwise share the repository. Staging is a separate step, so you can inspect what you selected before saving the commit.

## Why Version Control Matters in Cybersecurity

Version control provides a history of documented changes. For example, a team can use Git to review edits to incident reports, detection rules, PowerShell or Python scripts, forensic notes, SOC investigation documentation, and configuration files. A useful commit message helps explain what changed and why.

This does not replace an approved case-management system, evidence-handling procedure, or access-controlled storage. Follow your organization's rules for records, evidence, privacy, and retention. Do not use a public repository for restricted work.

## Review Before You Commit

Cybersecurity files can contain sensitive details, and a small edit can change the behavior of a detection or response script. Before committing, inspect the changed files and their contents. Confirm that the changes are expected, understandable, and free of unrelated edits or sensitive data. In VS Code, review the Source Control view or open the diff; in PowerShell, use `git status` and `git diff`.

The staging area helps you choose exactly which changes enter a commit. Avoid blindly staging everything with `git add .` when unrelated work or sensitive files may be present.

## Cybersecurity Safety Note

Git history can preserve sensitive information even after a file is deleted from the current working directory. Deleting a file in a later commit does not erase the earlier version from history.

Never commit passwords, API keys, tokens, private keys, credentials, sensitive logs, personal information, or production secrets. Use fictional training data for exercises. If a real credential is accidentally committed, treat it as exposed and promptly revoke or rotate it, then follow your organization's response process. Removing it from the latest version alone is not enough.

## Knowledge Check

Try to answer these without looking up the answers:

1. How is Git different from GitHub?
2. What does the staging area help you do?
3. What is the difference between an untracked file and a modified file?
4. Which command saves staged changes as a checkpoint in your local repository?
5. Why can deleting a secret from the current version fail to remove the risk?

<details>
<summary>Knowledge check answers</summary>

1. Git is version-control software; GitHub hosts Git repositories and provides collaboration features.
2. It lets you select and review the changes that will go into the next commit.
3. An untracked file is new to Git; a modified file is already tracked but has edits not yet staged.
4. `git commit` saves staged changes in local history.
5. Earlier commits may still contain the secret, so it must be treated as exposed and revoked or rotated.

</details>
