# Lab 02: Connect a Cybersecurity Project to GitHub

> **Simulated practice:** This lab describes sharing a fictional cybersecurity learning project. It is not production incident work and does not represent production experience. This guide does not create a GitHub repository or run any commands for you. A `git push` publishes commits to the remote, so perform the optional publishing steps only after reviewing the repository and deciding that you are ready to share it.

## 1. Objective

Understand how a local Git repository connects to GitHub, inspect its remote configuration, and learn how `git push`, `git pull`, `git fetch`, and `git clone` exchange project history.

## 2. Scenario

You completed a simulated cybersecurity investigation project locally. It contains fictional investigation documentation and safe training materials. You want to make a GitHub repository for portfolio use, but first you will check the local project, understand the remote setup, and review what would be shared.

No real production systems, credentials, customer data, or sensitive logs are part of this scenario.

## 3. Prerequisites

- Git is installed and available in PowerShell.
- You have a local Git repository for a cybersecurity learning project.
- You can sign in to GitHub and are authorized to create a repository if you choose to do so.
- You have reviewed the project's visibility and content. A private repository is not a safe place for secrets.
- Open the repository in VS Code and open **Terminal > New Terminal**. Confirm that PowerShell is at the repository root.

This lab contains example publishing commands for you to run only if you choose to publish. The commands have not been run for you. Do not publish work that contains sensitive or unauthorized information.

## 4. Step 1: Check Current Git Status

```powershell
git status
```

Review the current branch and all listed changes. If there are unrelated, staged, or sensitive changes, stop and resolve them before considering a push. Do not stage or publish unrelated work.

## 5. Step 2: Check Existing Remotes

```powershell
git remote -v
```

This displays the saved remote names and URLs used for fetching and pushing. A cloned repository commonly has a remote named `origin` already configured.

If no remote is listed, the repository has no saved remote URL yet. That is normal for a repository created locally with `git init`; you can add a remote after creating the GitHub repository.

## 6. Step 3: Create a GitHub Repository Manually

If you decide to publish this learning project, create the remote repository yourself through GitHub's website:

1. Sign in to GitHub using your own account.
2. Choose **New repository**.
3. Enter a clear project name, such as `cybersecurity-investigation-lab`.
4. Add a short, accurate description that identifies it as a learning project.
5. Choose **Public** or **Private** based on your sharing goals and any applicable rules. Public means anyone can view it. Private limits access to authorized collaborators but does not make secrets safe to store there.
6. If your local repository already contains a README or commits, do not initialize the GitHub repository with a README, license, or other file that creates a separate first commit. Start with an empty remote to avoid unrelated history that may need to be reconciled.
7. Create the repository and copy its HTTPS or SSH repository URL. Do not share or embed credentials in that URL.

No account-specific URL is provided here. Keep the repository empty until you have reviewed the local project and are ready to push.

## 7. Step 4: Add the Remote

Only if you chose to create the GitHub repository and confirmed the local repository has no existing `origin`, add its URL:

```powershell
git remote add origin https://github.com/USERNAME/REPOSITORY.git
```

Replace `USERNAME` with the repository owner's GitHub username or organization name, and `REPOSITORY` with the repository name. Use the exact URL shown on the GitHub repository page. Never put a password, token, or other credential in the URL.

This command only saves the remote's name and URL locally. It does not publish your files.

## 8. Step 5: Verify the Remote

```powershell
git remote -v
```

Confirm that `origin` points to the intended repository and that the fetch and push URLs are correct. If the URL is wrong, do not push. Correct it only after verifying the intended URL.

## 9. Step 6: Push the Main Branch

This step is optional. First confirm that your local branch is named `main`, that the GitHub remote is empty or otherwise ready for this history, and that you have reviewed all content. Then, if you intend to publish:

```powershell
git push -u origin main
```

This sends commits on local `main` to `origin` and sets `origin/main` as the upstream tracking branch. GitHub will then contain the pushed commits, visible according to the repository's visibility and access settings. The `-u` option means `--set-upstream`, which links local `main` to `origin/main` for later commands such as `git push`.

If your local branch has a different name, do not assume this command will work. Check with `git branch --show-current` and follow the intended branch naming. Do not force-push to get around an error.

## 10. Step 7: Make a Safe Documentation Change Locally

If you completed the optional push, make a small, safe documentation edit for this exercise. For example, add this sentence to an appropriate Markdown file in the project:

```text
This project uses fictional data for GitHub workflow practice.
```

Use a file appropriate to your project and do not include real incident details, secrets, internal hostnames, personal information, or production data. If you are not ready to publish, you can still make and review a local change without pushing it.

## 11. Step 8: Stage and Commit the Change

Determine the commands you should use to check the status, stage only the documentation file you edited, review the staged changes, and commit the change. Do not stage unrelated files. Optional hints are below.

<details>
<summary>Optional hints</summary>

Use `git status` to see the changed path. Use `git add` with that specific filename, then `git diff --staged` to inspect the exact content prepared for the commit. Once reviewed, create a commit with a message that describes the documentation change.

</details>

## 12. Step 9: Push the New Commit

If the local branch is connected to the intended remote and you are ready to share the reviewed commit, push it with:

```powershell
git push
```

This shares the new commit with GitHub. Do not run this if you have not reviewed the staged diff, are unsure of the remote, or do not want to publish yet. The lab does not require you to publish anything.

## 13. Step 10: Understand Pull

`git pull` retrieves new commits from the configured remote and integrates them into your current branch, commonly by merging. For example, it can bring a collaborator's approved README clarification into your local project. It may report conflicts if both sides changed the same content. Review your state before and after pulling, and resolve conflicts deliberately.

If you have confirmed the intended remote and are ready to integrate its changes, the command is:

```powershell
git pull
```

Only run `git pull` in a repository with the intended remote configured and when you are ready to integrate remote changes. This guide does not run it for you.

## 14. Step 11: Understand Fetch

`git fetch` retrieves new commits and updates remote-tracking information such as `origin/main`. A plain fetch does not merge or rebase those commits into your current branch and does not automatically change your working files. It lets you inspect remote updates before choosing whether and how to integrate them.

To retrieve remote updates for inspection without integrating them into your current branch, run:

```powershell
git fetch
```

Only run `git fetch` when a remote is configured and you want to check for remote updates. This guide does not run it for you.

## Command Comparison

| Command         | Direction or purpose                                                  | Effect on your current local branch                              |
| --------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `git push`      | Sends local commits to the configured remote.                         | Does not send uncommitted changes.                               |
| `git pull`      | Retrieves remote commits and integrates them into the current branch. | Updates the current branch and may change working files.         |
| `git fetch`     | Retrieves remote commits and updates remote-tracking references.      | Does not automatically integrate them into the current branch.   |
| `git clone URL` | Creates a local copy from a remote repository URL.                    | Creates a repository directory and normally configures `origin`. |

## Before You Push Cybersecurity Work

Check every item before publishing:

- [ ] No credentials
- [ ] No API keys
- [ ] No tokens
- [ ] No private keys
- [ ] No sensitive logs
- [ ] No real customer data
- [ ] README reviewed
- [ ] `git status` reviewed
- [ ] `git diff` reviewed for unstaged changes
- [ ] Staged diff reviewed with `git diff --staged`
- [ ] Correct remote URL and repository visibility confirmed

Git history can retain sensitive content after you delete it from the latest version. If a real credential was committed, treat it as exposed and revoke or rotate it. Do not rely on deleting a file or making the repository private to make an exposed secret safe again.

## Final Challenge

Without looking back at the lesson, explain the difference between `git fetch` and `git pull`. Include what each command changes locally and when you might choose to inspect remote updates before integrating them.

## Reflection Questions

1. What is the difference between your local repository and a GitHub remote repository?
2. What does the remote name `origin` refer to, and how can you confirm its URL?
3. Why should you verify repository visibility and content before using `git push`?
4. How does `git fetch` help you inspect remote work before integrating it?
5. What documentation or project context would help an employer understand your cybersecurity learning project?
