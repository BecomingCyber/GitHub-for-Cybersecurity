# Lab 04: Review a Cybersecurity Change with a Branch

> **Simulated practice:** This lab uses fictional SOC documentation only. It is not production incident-response work and must not be represented as production experience. Do not add real credentials, secrets, production data, or sensitive personal information.

## 1. Objective

Create a branch for a small cybersecurity documentation improvement, inspect and commit the change on that branch, and prepare the branch for a GitHub pull request without publishing or merging it.

## 2. Scenario

You maintain a simulated SOC investigation project. A sentence in the incident documentation should clarify that repeated authentication failures in the exercise were part of authorized training activity. You will make the change on a separate branch so it can be reviewed before it is merged into `main`.

The example file and all activity are fictional. No real system, account, alert, or investigation is involved.

## 3. Prerequisites

- Git is installed and available in PowerShell.
- You have opened the local learning repository in VS Code.
- Open **Terminal > New Terminal** and confirm PowerShell is at the repository root.
- Your repository has a local branch named `main` and no pending work you need to preserve on it.
- Review the initial `git status` before beginning. If unrelated changes exist, do not include or overwrite them.

This lab only describes local Git commands and a later GitHub review. It does not create a branch, stage files, make commits, push, open a pull request, or merge anything for you.

## 4. Step 1: Confirm a Clean Repository

Run:

```powershell
git status
```

For the expected starting point, Git should report a clean working tree. Starting clean makes it easier to tell which changes belong to this exercise. If you have work to keep, do not delete it. Finish or safely set it aside according to your workflow before beginning this lab.

## 5. Step 2: Confirm the Current Branch

Run:

```powershell
git branch --show-current
```

Expected result:

```text
main
```

If the result is not `main`, stop and confirm the correct starting branch for your repository before continuing.

## 6. Step 3: Create a Branch

Run:

```powershell
git switch -c docs/update-simulated-incident
```

This command has two parts:

- `switch` tells Git to move your working tree to another branch.
- `-c` tells Git to create the named branch before switching to it.

The new branch starts from the commit currently checked out, which should be the current `main` commit.

## 7. Step 4: Confirm the Current Branch

Run:

```powershell
git branch --show-current
```

Expected result:

```text
docs/update-simulated-incident
```

You can now make this proposed change without immediately changing the `main` branch.

## 8. Step 5: Create a Safe Example File

Create `branch-review-example.md` in the repository root. In PowerShell, run:

```powershell
@'
# Simulated Incident Documentation Update

Incident ID: LAB-004
Environment: Training Lab
Change Type: Documentation Improvement
Status: Draft

## Proposed Update

Clarify that repeated authentication failures observed in this exercise were generated as part of authorized simulated training activity.

No real production systems or accounts were involved.
'@ | Set-Content -Path .\branch-review-example.md -Encoding utf8
```

This writes the fictional documentation example. `Set-Content` replaces the target file if it already exists, so confirm that you are creating this lab file and do not overwrite other work.

## 9. Step 6: Check Status

Run:

```powershell
git status
```

Git should show `branch-review-example.md` as untracked because it is a new file not yet added to version control. The current branch should still be `docs/update-simulated-incident`.

## 10. Step 7: Review the File

Open the file in VS Code, or read it in PowerShell:

```powershell
Get-Content .\branch-review-example.md
```

Confirm the LAB-004 details and proposed update are present, fictional, and free of secrets or sensitive information.

## 11. Step 8: Review Unstaged Changes Where Applicable

Run:

```powershell
git diff
```

A normal `git diff` shows unstaged changes to tracked files. It may show no output for this new untracked file because Git is not tracking it yet. Inspect the file directly as shown in the previous step. After staging, `git diff --staged` will show the proposed addition.

## 12. Step 9: Stage the File

Stage only the file you reviewed:

```powershell
git add branch-review-example.md
```

This selects the current version for the next commit. It does not commit or publish the file.

## 13. Step 10: Review Staged Changes

Run:

```powershell
git diff --staged
```

Review the complete staged addition. It should contain only `branch-review-example.md` and the expected fictional text. If anything is unexpected, correct the file, stage it again, and review the staged diff again.

## 14. Step 11: Commit

After confirming the staged diff, create a local commit on the feature branch:

```powershell
git commit -m "Improve simulated incident documentation"
```

This records the staged file in the history of `docs/update-simulated-incident`. It does not merge the change into `main` or send it to GitHub.

## 15. Step 12: Review Branch History

Run:

```powershell
git log --oneline
```

The recent history should include `Improve simulated incident documentation`. This is the local history visible from your current branch.

## 16. Step 13: Compare the Branch With `main`

Run:

```powershell
git diff main..docs/update-simulated-incident
```

This compares the file content at the tips of local `main` and `docs/update-simulated-incident`. It should show the new fictional documentation file as an addition. This command compares the endpoint trees; it is not a list of commits between the branches.

## 17. Step 14: Understand the Next GitHub Steps

If you later decide to publish the branch, the typical review process is:

1. Push the branch to the intended remote. Verify the repository URL, visibility, and contents first.
2. Open a pull request on GitHub from `docs/update-simulated-incident` into the project's target branch, commonly `main`.
3. Review the pull request's **Files changed** view and the security implications.
4. Receive reviewer comments or requests for changes, if any.
5. Make corrections on the same branch and push another commit if needed.
6. Obtain approval if the repository's rules require it.
7. Merge into `main` only after the appropriate review and required checks.

A pull request is a GitHub collaboration feature, not a Git command. This lab does not push the branch or create a pull request.

## Pull Request Review Checklist

Before asking for review, check:

- [ ] The change matches its intended purpose.
- [ ] No unrelated files changed.
- [ ] No credentials are included.
- [ ] No secrets are included.
- [ ] No sensitive logs are included.
- [ ] No production data is included.
- [ ] Documentation is accurate.
- [ ] The Git diff was reviewed.
- [ ] The staged diff was reviewed.
- [ ] Test or validation results were reviewed when applicable.
- [ ] The branch contains focused changes.

## What If a Reviewer Requests Changes?

Keep working on the same feature branch so the pull request can collect the follow-up changes:

1. Stay on `docs/update-simulated-incident` and edit the requested documentation.
2. Review the unstaged change with `git diff` and check the status.
3. Stage the specific file and inspect it with `git diff --staged`.
4. Create another focused commit with a message that describes the correction.
5. Push the new commit to the same remote branch when you are authorized and ready.

After that push, GitHub updates the existing pull request to include the new commit. Review the destination and content before pushing. None of these operations are performed automatically by this lab.

## Merge Concept

Merging integrates changes from one branch into another. For example, after review, a GitHub pull request can be merged so the approved documentation change becomes part of `main`. The exact merge method and permissions depend on repository settings. Do not merge until required reviews and checks are complete. This lab does not run `git merge`.

## After Merge

After the pull request has been merged on GitHub, a typical local cleanup is:

```powershell
git switch main
git pull
git branch -d docs/update-simulated-incident
```

This switches to local `main`, updates it from its configured upstream, and safely deletes the local feature branch if Git considers it fully merged. Deleting the local branch does not automatically delete the remote branch. The commands are shown for learning only and are not run here.

## Final Challenge

On `docs/update-simulated-incident`, add a `Lessons Learned` section to `branch-review-example.md` with two or three points from the fictional exercise. Determine how you would inspect the change, stage it, inspect the staged change, and commit it. Do not push it as part of this challenge.

<details>
<summary>Optional hints</summary>

- Check which branch you are on and inspect the change before staging.
- Stage only the file you edited, then review what is staged.
- Choose a commit message that describes adding lessons learned to the simulated documentation.

</details>

## Reflection Questions

1. Why did you create a feature branch instead of editing `main` directly?
2. What did `git diff` show for the new untracked file, and why?
3. How did `git diff --staged` help you review the proposed commit?
4. What does the branch comparison show before you open a pull request?
5. What security or documentation issue could a reviewer help identify before merge?
