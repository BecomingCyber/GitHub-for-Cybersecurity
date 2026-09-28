# GitHub Workflow for Cybersecurity Learners

This guide shows how a local Git repository communicates with a GitHub repository. Run the commands from the project folder in PowerShell or the VS Code integrated terminal. Commands shown here are examples for you to run when appropriate; do not use them to publish sensitive or unauthorized work.

## Commands for Connecting to a Remote

### `git remote -v`

- **What it does:** Lists configured remotes and their fetch and push URLs. A remote is a saved name and URL for another copy of the repository.
- **When to use it:** To check where `git pull` and `git push` will communicate, or to verify a newly added remote.
- **Cybersecurity example:** Confirm that a fictional SOC learning project points to the intended portfolio repository before sharing documentation.
- **Expected result:** One or more lines such as `origin  https://github.com/USERNAME/REPOSITORY.git (fetch)` and a matching `(push)` line. If there are no remotes, Git prints no remote entries.

### `git remote add origin URL`

- **What it does:** Adds a remote named `origin` with the URL you provide. It does not upload or download files.
- **When to use it:** To connect an existing local repository to a GitHub repository that you created separately.
- **Cybersecurity example:** Connect a local project containing fictional authentication-analysis notes to its intended GitHub portfolio repository.
- **Expected result:** Usually no output if the remote was added successfully. Check it with `git remote -v`.
- **Example:**

  ```powershell
  git remote add origin https://github.com/USERNAME/REPOSITORY.git
  ```

  Replace the placeholders with the URL for your own repository. Do not put passwords or access tokens in the URL.

### `git push -u origin main`

- **What it does:** Pushes the local `main` branch and its commits to the remote named `origin`. The `-u` option, short for `--set-upstream`, records the remote branch as the local branch's upstream tracking branch.
- **When to use it:** The first time you push a local `main` branch to the matching remote branch, after checking the destination and reviewing the content.
- **Cybersecurity example:** Publish the reviewed first version of a fictional incident-documentation learning project to its selected GitHub repository.
- **Expected result:** Git reports that it sent objects and created or updated the remote `main` branch. The local `main` branch will track `origin/main`; subsequent pushes from that branch can usually use `git push`.

  ```powershell
  git push -u origin main
  ```

  This command publishes commits. Do not run it until you have verified repository visibility, remote URL, and content.

### `git push`

- **What it does:** Sends local commits to the configured upstream branch or remote destination. It does not send uncommitted working-directory changes.
- **When to use it:** After making and reviewing a new commit that is ready to be shared with the configured remote.
- **Cybersecurity example:** Share an approved documentation update describing how a fictional log parser works.
- **Expected result:** Git reports the updates sent to the remote, or says the branch is already up to date. A rejected push requires understanding and integrating remote changes, not blindly forcing the push.

  ```powershell
  git push
  ```

### `git pull`

- **What it does:** Fetches updates from the configured remote and integrates them into the current branch, commonly by merging. The exact integration behavior can depend on Git configuration and command options.
- **When to use it:** To bring collaborators' remote commits into your current local branch before continuing work.
- **Cybersecurity example:** Retrieve a reviewed update to a fictional incident-response note before editing your local copy.
- **Expected result:** Git downloads and integrates available commits, reports that the branch is up to date, or asks you to resolve conflicts. Check `git status` and review the result afterward.

  ```powershell
  git pull
  ```

### `git fetch`

- **What it does:** Downloads new commits and updates remote-tracking references, such as `origin/main`, without integrating those commits into your current branch or changing your working files.
- **When to use it:** To inspect whether collaborators have updated the remote before deciding how to integrate their work.
- **Cybersecurity example:** Check whether a teammate has pushed documentation changes before you incorporate them into a local investigation-template exercise.
- **Expected result:** Git reports fetched objects and updated remote-tracking references, or that there was nothing new. Your current branch is not automatically merged or rebased by a plain `git fetch`.

  ```powershell
  git fetch
  ```

### `git clone URL`

- **What it does:** Creates a local copy of a remote repository, including its available history, and normally configures the source remote under the name `origin`.
- **When to use it:** To start working with a GitHub project on your computer.
- **Cybersecurity example:** Clone a public training repository that contains fictional logs and an educational parser.
- **Expected result:** Git creates a directory named for the repository, downloads its files and history, and configures the remote. Use `Set-Location` to enter it.

  ```powershell
  git clone https://github.com/OWNER/REPOSITORY.git
  Set-Location .\REPOSITORY
  ```

  Replace `OWNER` and `REPOSITORY` with the actual project path. For private repositories, you must have permission and authenticate through an approved method.

## `git fetch` Versus `git pull`

Both commands contact a remote and retrieve new commits, but they do different things afterward:

- `git fetch` updates remote-tracking references, such as `origin/main`. Your current branch and working files are not automatically changed, so you can inspect the fetched work before integrating it.
- `git pull` fetches and then integrates the remote changes into the current branch. It usually merges, unless your Git configuration or options choose another integration strategy such as rebase.

Use `git fetch` when you want to inspect first. Use `git pull` when you are ready to integrate remote work into the current branch. Review the working tree and resolve any conflicts carefully.

## Starting With a Local Project

If you create a new local project before creating its GitHub repository, the common first-publication workflow is:

```text
Create local project
        |
        v
     git init
        |
        v
      git add
        |
        v
     git commit
        |
        v
Create GitHub repository
        |
        v
git remote add origin URL
        |
        v
git push -u origin main
        |
        v
Future commits use git push
```

Example PowerShell sequence, assuming your Git branch is named `main` and you are in the project root:

```powershell
git init
git status
git add README.md
git diff --staged
git commit -m "Add cybersecurity learning project overview"
```

Then create an empty GitHub repository through GitHub's website, set the intended visibility, and copy its repository URL. If your local repository already has a README or other commits, do not initialize the GitHub repository with a second README or initial commit. Add the remote and review the destination before pushing:

```powershell
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git remote -v
git push -u origin main
```

Replace the placeholders. Run the push only when you intend to publish those commits and have reviewed the exact content. After setting the upstream, later commits on `main` can usually be shared with `git push`.

## Troubleshooting

### `remote origin already exists`

A remote named `origin` is already configured. Inspect it first:

```powershell
git remote -v
```

If it points to the wrong repository, confirm the correct URL before changing it. You can update it with `git remote set-url origin URL`. Do not add a second `origin` or push until you have verified the destination.

### Push rejected

A push can be rejected when the remote has commits you do not have locally, the branch is protected, or you do not have permission. First inspect the message and current state:

```powershell
git status
git fetch
git log --oneline --decorate --graph --all
```

If the remote contains work you need, review it and integrate it using your team's workflow, for example with `git pull`. Resolve conflicts deliberately. Do not use `git push --force` as a routine fix; it can overwrite shared history.

### Authentication required

GitHub requires you to authenticate and have permission to access the repository. Use a supported method such as Git Credential Manager/browser sign-in or an authorized SSH key configured in your environment. Follow your organization's guidance. Never store a password or personal access token in source files, scripts, command history, or a remote URL.

### Wrong repository URL

Check the saved URL with `git remote -v` and compare it with the URL shown on the intended GitHub repository page. If you need to correct it, use `git remote set-url origin URL` with the verified URL. Do not push until the owner and repository name are correct.

### Branch name mismatch

Check the current local branch with:

```powershell
git branch --show-current
```

If it is not `main`, `git push -u origin main` will not push the current branch under that name. Follow the repository's expected branch naming. Do not rename or push a branch until you understand which branch is intended and whether collaborators depend on it.
