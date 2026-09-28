# Lab 05: Secure a Cybersecurity GitHub Repository

> **Fictional training exercise:** This lab prepares a simulated cybersecurity project for review. It does not use real credentials or production data. Do not create a real secret for this exercise, change `.gitignore`, alter GitHub settings, or publish anything as part of the lab.

## 1. Objective

Practice reviewing ignore rules, checking whether example paths are ignored, inspecting tracked files and repository changes, and identifying security features to review before publishing.

You will use `git status`, `git check-ignore`, `git ls-files`, `git diff`, `git diff --staged`, `git log --oneline`, `git remote -v`, and `git branch --show-current` as inspection commands. This lab does not stage, commit, push, or modify configuration.

## 2. Scenario

You are preparing a fictional cybersecurity learning project for a possible GitHub portfolio. Before sharing it, you will inspect which files Git tracks, whether typical local-secret and log filenames match ignore rules, and whether the current branch and remote are the ones you expect.

All examples are fictional. A filename such as `.env` or `debug.log` is used only to check Git's ignore rules. You do not need to create either file.

## 3. Prerequisites

- Git is installed and available in PowerShell.
- You have opened the learning repository in VS Code.
- Open **Terminal > New Terminal** and confirm that PowerShell is at the repository root.
- Read commands before running them. They are inspection examples only.

## 4. Step 1: Check Repository Status

Run:

```powershell
git status
```

This shows the current branch and staged, unstaged, or untracked changes. Note any unexpected changes, but do not stage or discard them for this lab.

## 5. Step 2: Review `.gitignore`

Display the file in PowerShell:

```powershell
Get-Content .\.gitignore
```

Review whether its rules cover these categories:

- `.env` and `.env.*` local environment files.
- Private key file patterns used by the project.
- Log files, such as `*.log`.

The existing project may include an explicit exception for a fictional sanitized training log. Read the full rules and understand both the general ignore pattern and any exception. Do not change `.gitignore` automatically or as part of this lab.

`.gitignore` affects matching untracked files. It does not stop Git from tracking a file that is already tracked, and it does not erase content from Git history.

## 6. Step 3: Verify Whether `.env` Is Ignored

Run this check without creating a `.env` file:

```powershell
git check-ignore -v .env
```

If `.env` is untracked or does not exist and a matching ignore rule applies, Git should print the source file, line number, matching rule, and path. The exact line number depends on the file.

If there is no output, the path may not match an ignore rule, or it may already be tracked. Check tracking separately with:

```powershell
git ls-files -- .env
```

A path already tracked by Git is not treated as ignored by the default `git check-ignore` behavior. Do not create a file containing a secret to test this.

## 7. Step 4: Verify Log Handling

Use the fictional filename `debug.log` without creating it:

```powershell
git check-ignore -v debug.log
```

If an applicable ignore rule matches an untracked path, Git reports the rule and path. If no rule is reported, inspect `.gitignore` and determine whether that filename is supposed to be ignored. The project may intentionally allow a specific sanitized training log, so check for exceptions as well.

## 8. Step 5: Check Tracked Files

Run:

```powershell
git ls-files
```

This lists paths currently tracked in the repository index. It does not list every untracked file or prove that the listed content is safe. Review the paths and open files where necessary.

## 9. Step 6: Review Repository Changes

Run:

```powershell
git status
git diff
git diff --staged
```

- `git status` summarizes the current branch and file states.
- `git diff` shows unstaged changes to tracked files. It does not normally show the full contents of a new untracked file, so inspect new files directly.
- `git diff --staged` shows the changes prepared for the next commit. This lab does not stage anything, so it may show no output.

Review these results before any future commit or push. Do not stage or commit during this lab.

## 10. Step 7: Review Recent History

Run:

```powershell
git log --oneline
```

This summarizes recent commit identifiers and messages. History matters because a secret removed from the latest file may still exist in an earlier commit. The one-line log is not a scan of commit contents; when investigating possible exposure, follow provider and organizational procedures to determine where the value remains.

## 11. Step 8: Confirm the Current Branch

Run:

```powershell
git branch --show-current
```

This prints the current local branch name. Confirm it is the branch you expect before preparing or sharing changes.

## 12. Step 9: Confirm Remote Configuration

Run:

```powershell
git remote -v
```

This lists configured remote names and fetch/push URLs. Confirm the URLs point to the intended repository before any future push. If there is no remote, Git prints no remote entries. This lab does not add or change a remote.

## 13. Step 10: Perform a Safe Manual Repository Inspection

A filename or a line containing words such as `password`, `secret`, `token`, `key`, or `credential` deserves review. A match is not proof that a real secret exists, and a search with no matches does not prove that all sensitive information has been found.

The following PowerShell example inspects filenames and common text-file contents. It excludes the `.git` directory from the working-file scan and does not change any files:

```powershell
$files = Get-ChildItem -Path . -Recurse -File | Where-Object {
    $_.FullName -notmatch '[\\/]\.git[\\/]'
}

$files |
    Where-Object { $_.Name -match '(?i)password|secret|token|key|credential' } |
    Select-Object -ExpandProperty FullName

$textFiles = $files | Where-Object {
    $_.Name -eq '.env' -or $_.Extension -in '.md', '.txt', '.py', '.ps1', '.yml', '.yaml', '.json'
}

if ($textFiles) {
    Select-String -Path $textFiles.FullName -Pattern '(?i)\b(password|secret|token|key|credential)\b'
}
```

Inspect matches carefully, and do not paste any real secret into notes or chat. This quick check covers selected current working files, not every file type, ignored file, Git object, or historical commit. Use approved scanning and incident-response processes as required.

## What If You Accidentally Committed a Secret?

Consider this fictional placeholder:

```text
DEMO_API_KEY=example-placeholder
```

This is **not a real key** and cannot authenticate to a service. Do not replace it with an actual credential.

If a real secret is accidentally committed:

1. Assume it is exposed.
2. Revoke or rotate the real credential at the provider that issued it. Do this first.
3. Remove it from current project files and prevent it from being committed again.
4. Investigate Git history to determine whether earlier commits still contain it.
5. Follow approved organizational and provider procedures for history cleanup if required. Coordinate with collaborators; this lab does not provide history-rewriting commands.
6. Review usage or access logs where applicable and document the response without repeating the secret.

## Why Deleting the File Is Not Enough

Git commits preserve snapshots of repository content. Deleting a file in a later commit changes the current version, but an earlier commit may still contain the original value. Treat a committed credential as exposed until it has been revoked or rotated, regardless of whether the file is still visible in the latest version.

## Why Making the Repository Private Is Not Enough

Private visibility limits access according to repository and organization settings, but it cannot recall content that someone may already have copied or accessed. A private repository is not secret storage. Rotate or revoke an exposed credential even if the repository was private or has since been made private.

## GitHub Security Features

In GitHub's repository settings and security views, identify where your project owner would review these features, if available:

- Secret scanning and push protection.
- Dependabot alerts and security updates.
- Code scanning, including CodeQL where supported and configured.
- Branch protection or related rules.

Feature availability and behavior depend on repository settings, supported content, account or organization capabilities, and configuration. Do not assume every feature is enabled, and do not treat a clean scan as proof that the project is secure.

## Pre-Publish Security Checklist

Before publishing, verify each item:

- [ ] No credentials
- [ ] No API keys
- [ ] No tokens
- [ ] No private keys
- [ ] No sensitive logs
- [ ] No customer data
- [ ] No confidential files
- [ ] Sample data is sanitized or fictional
- [ ] Screenshots reviewed for sensitive information
- [ ] Current branch confirmed
- [ ] Remote confirmed
- [ ] Repository visibility reviewed
- [ ] README accurately labels simulated experience

## Final Challenge

Explain in your own words: **Why does adding a filename to `.gitignore` not remove it if Git is already tracking the file?**

Write your explanation before opening the hint. The hint points you toward the relevant Git concept but does not provide a complete answer.

<details>
<summary>Optional hint</summary>

Think about the difference between Git's ignore rules for files it has not started tracking and the repository index for files that are already tracked.

</details>

## Reflection Questions

1. What does `git check-ignore -v` tell you about a path?
2. Why does `.gitignore` not remove a file Git already tracks?
3. Why might a secret remain exposed after its file is deleted?
4. Why should a credential be rotated before attempting history cleanup?
5. What can a clean secret scan tell you, and what can it not guarantee?
