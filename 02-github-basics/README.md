# Module 02: GitHub Basics for Cybersecurity

GitHub gives you a place to host a Git repository so you can back up, share, and collaborate on project work. This module connects the local Git workflow from Module 01 to a remote repository and introduces the parts of a GitHub repository that help other people understand your work.

## Learning Objectives

By the end of this module, you should be able to:

- Explain how a local Git repository relates to a GitHub repository.
- Describe a remote repository and the conventional remote name `origin`.
- Explain what `clone`, `push`, and `pull` do at a high level.
- Recognize the difference between public and private repository visibility.
- Identify useful repository metadata, including its name, description, topics, README, and About section.
- Use GitHub Issues to document a project task or question.
- Review cybersecurity project content before sharing it.

## Git and GitHub: Local and Remote

**Git** records changes in a repository on your computer. That is your **local repository**. A **remote repository** is another copy of the repository available at a location such as GitHub. A **GitHub repository** is a Git repository hosted by GitHub, with additional web-based collaboration features.

The local and remote repositories have separate histories until you exchange commits. Use `git push` to send commits from your local repository to a remote. Use `git pull` to retrieve remote commits and integrate them into your current local branch.

```text
Local Computer
      |
      v
Local Git Repository
      |
      | git push (send local commits)
      v
GitHub Remote Repository
```

The reverse direction brings remote work into your local branch:

```text
GitHub Remote Repository
      |
      | git pull (fetch and integrate remote commits)
      v
Local Repository
```

`git clone` is commonly how you first create a local copy of a repository hosted on GitHub. Once cloned, Git records the remote URL so you can communicate with that remote.

## What Does `origin` Mean?

A **remote** is a saved name and URL for another copy of a Git repository. `origin` is the conventional name Git assigns to the remote when you clone a repository. It is only a nickname, not a special server or a synonym for GitHub. You can inspect saved remotes with `git remote -v`.

For a locally created repository, you can add a remote and call it `origin`, for example with `git remote add origin URL`. Replace `URL` with the repository URL shown by GitHub. A project can have more than one remote, each with its own name and URL.

## Repository Visibility

When creating a GitHub repository, you choose who can view it. Repository visibility can usually be changed later, but changing it should be a deliberate decision that follows any organization rules.

- **Public:** Anyone can view the repository. This can make a polished learning project easy for employers and other learners to inspect. Never treat a public repository as a place for real incident details, internal procedures, credentials, or customer information.
- **Private:** Access is limited to people or teams you authorize, subject to GitHub and organization settings. Private does not mean suitable for secrets or unrestricted company data. Access can change, and data can be copied or exposed. Follow your organization's data-handling rules.

Use fictional or properly approved sanitized data in portfolio projects, regardless of visibility. A private repository is not a substitute for secret storage or an approved case-management system.

## What Belongs in a Professional Cybersecurity Repository?

A useful repository helps a reviewer understand its purpose and evaluate its contents. Depending on the project, it may include:

- A **README** that explains the project's purpose, scope, safe setup, and how to use it.
- A concise **project description** and relevant repository metadata.
- **Documentation** explaining design choices, methods, and limitations.
- **Screenshots** that have been checked for secrets, personal information, hostnames, and other sensitive details.
- **Scripts** with clear usage instructions and safe example inputs.
- **Sample data** that is fictional, public-domain, or approved and sanitized.
- **Findings** written for the intended audience and cleared for sharing.
- **Learning notes** that distinguish lab practice from real work experience.
- A **license**, when appropriate, to state how others may use and share the material. Choose one that fits the project and your rights to its contents.

Do not upload credentials, tokens, real customer data, private keys, production logs, personally identifiable information, or confidential company information. Git history can retain content even after you delete a file from the latest version.

## GitHub Repository Metadata

Repository metadata helps visitors find and understand a project:

- **Repository name:** A short, readable name that identifies the project, such as `auth-log-learning-lab`.
- **Description:** A concise summary, such as "Beginner exercises for reviewing fictional authentication events with Git."
- **Topics:** Short tags that help categorize a repository, such as `cybersecurity`, `git`, `soc`, or `learning-project`. Choose accurate topics and avoid implying professional certifications or experience you do not have.
- **README:** The main project introduction. GitHub displays it on the repository page, making it a useful first explanation for a reviewer.
- **About section:** The repository page area where GitHub displays a short description, topics, and sometimes a project website or other links.

Keep the name, description, topics, and README consistent with what the repository actually contains. Do not put sensitive details in metadata, either.

## GitHub Issues

An **Issue** is a GitHub discussion item used to track a task, question, bug, or improvement. Issues help a project record what needs attention without burying the request in a commit message.

Cybersecurity learning project examples include:

- `Add IOC parser`
- `Improve log analysis`
- `Document investigation findings`
- `Add input validation`
- `Update incident response notes`

Write issues with enough context to act on them. Use fictional examples, avoid sensitive indicators or case details, and do not treat a public Issue as a confidential reporting channel.

## Basic Collaboration Workflow

A simple collaboration flow is:

1. Clone the project or open your existing local repository.
2. Check the current branch and working-tree status.
3. Make a focused change, such as improving documentation for a fictional log-analysis exercise.
4. Review the changes and stage only the intended files.
5. Commit the reviewed changes locally with a clear message.
6. Push your commits to the remote repository when you are ready and authorized to share them.
7. Use an Issue to track follow-up work, or use a pull request when the project workflow calls for review before merging.

Always review the files and staged diff before pushing. Pushing shares commits with the remote and its permitted audience; it is not just a local save.

## Cybersecurity Portfolio Perspective

Code is only one part of a cybersecurity project. Documentation explains the question you explored, the assumptions you made, the data source, the steps you followed, and the limitations of your result. That context lets an employer or peer assess your reasoning rather than guess what a script or screenshot means.

Describe simulated work honestly as a lab or learning exercise. Do not suggest that a fictional investigation was a production incident or that a practice result came from a real employer environment.

## Knowledge Check

Answer these questions before opening the collapsed answer section:

1. What is the difference between a local repository and a remote repository?
2. What does the name `origin` usually refer to?
3. Who can generally view a public GitHub repository, and why should it still contain no secrets?
4. Name two useful types of metadata on a GitHub repository page.
5. What is a GitHub Issue useful for in a cybersecurity learning project?

<details>
<summary>Knowledge check answers</summary>

1. A local repository is the copy and history on your computer; a remote repository is another copy available at a configured location such as GitHub.
2. `origin` is the conventional name Git gives the remote URL when a repository is cloned. It is a nickname, not a special server.
3. Anyone can generally view it. Public content is exposed to everyone, and secrets should not be published even in private repositories.
4. Examples include the repository name, description, topics, README, and About section.
5. An Issue tracks a task, question, bug, or improvement, such as adding input validation to a fictional IOC parser.

</details>
