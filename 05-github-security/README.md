# Module 05: GitHub Security for Cybersecurity Projects

A GitHub repository can be useful for learning and collaboration, but anything committed may be shared, copied, or retained in history. This module covers practical habits and GitHub features that can reduce common repository risks. These features help with security work, but none of them replaces careful review or organizational policy.

## Learning Objectives

By the end of this module, you should be able to:

- Explain why committing sensitive information can expose it beyond the current file version.
- Describe what `.gitignore` does and what it cannot do.
- Use `.env` and `.env.example` appropriately without committing real secrets.
- Explain the purpose and limitations of secret scanning and push protection.
- Describe dependency risks and the role of Dependabot alerts and updates.
- Explain CodeQL and code scanning at a beginner level.
- Identify basic safeguards for GitHub Actions workflows.
- Explain repository visibility, least privilege, and branch protection.
- Perform a basic security review before publishing a repository.
- Describe the first steps to take if a credential is accidentally committed.

## Why Repositories Need Security Review

A repository can become a security risk when sensitive information is committed. Examples include API keys, passwords, access tokens, private keys, cloud credentials, database connection strings, customer data, internal hostnames, and sensitive logs. A secret can be copied quickly, and Git history may retain it after the file is edited or deleted.

Only put information in a repository that you are authorized to store there. Review both the current files and relevant history before sharing a repository. Follow your organization's classification, incident-response, and data-handling rules.

## `.gitignore`

A `.gitignore` file tells Git which matching, untracked files to leave out of normal staging when you use commands such as `git add .`. It is useful for local files such as `.env`, generated output, or private key files that should not enter the repository.

A `.gitignore` file:

- Helps prevent specified **untracked** files from being added to future commits.
- Does **not** remove a file that Git already tracks. If a file is tracked, adding its name to `.gitignore` does not stop Git from tracking later changes to it.
- Does **not** erase sensitive information from existing Git history.
- Does **not** guarantee a file is safe. Review `git status` and the diff before committing.

An ignore rule is a guardrail, not secret storage. Do not rely on `.gitignore` instead of checking what is staged.

## Environment Variables, `.env`, and `.env.example`

An **environment variable** is a name and value supplied to a process through its environment. Applications and development tools may read environment variables for settings. A `.env` file is a common local convention for storing development settings, but PowerShell or an application does not automatically load every `.env` file. A tool or application must be configured to read it.

A local `.env` might hold real credentials for development, so keep it out of version control and use an approved secret store or local configuration method. Never commit actual secrets. A committed `.env` can remain in Git history even if you later delete it.

An `.env.example` file documents the variable names a project expects, with placeholders only. For example:

```dotenv
API_KEY=example-placeholder
```

`example-placeholder` is explanatory text, not a working key. Do not copy a real value into `.env.example`.

## Secret Scanning and Push Protection

**Secret scanning** can look for certain known credential patterns in supported repositories and configurations. GitHub or an integration may report a detected pattern so the repository owner can respond. Coverage depends on the provider, supported secret types, repository settings, and other configuration. Secret scanning cannot detect every possible secret, and a clean result does not prove the repository contains none.

**Push protection** is a feature that may warn about or block a push when a supported configuration recognizes a secret in the proposed changes. Availability and behavior depend on GitHub product, repository and organization settings, and the type of secret. Do not assume it is enabled everywhere or use it as a substitute for reviewing changes before a push.

## If a Secret Is Accidentally Committed

Treat a committed credential as exposed, even if the repository is private or the file has since been deleted. Prioritize response in this order:

1. Treat the credential as exposed.
2. Revoke or rotate it through the provider that issued it. This is the priority because removing text from a file does not invalidate a copied credential.
3. Remove the secret from current project files and prevent it from being reintroduced.
4. Investigate whether Git history still contains it.
5. Follow organizational procedures for history cleanup if required. Coordinate before any history rewrite because it affects collaborators and does not replace credential rotation.
6. Review provider activity or access logs where appropriate, and follow the organization's incident-response process.

Deleting the file alone does not make the credential safe again. Making a repository private does not make an exposed credential trustworthy again. Do not put real secret values in an issue, report, or chat while documenting the response.

## Dependency Security and Dependabot

A **dependency** is an external library, package, or component that a project uses. A vulnerable or outdated dependency can introduce risk into software that relies on it. Keep dependency information and update decisions reviewable, and verify changes before adopting them.

**Dependabot** is a GitHub service with features that can help identify and update dependencies, depending on repository support and configuration. Conceptually, it can provide:

- **Dependency alerts:** Notifications about known vulnerabilities in dependencies GitHub can identify.
- **Dependency update pull requests:** Proposed changes to dependency versions.
- **Security updates:** Pull requests intended to update dependencies affected by security advisories.

Repositories do not all have identical manifests, alert coverage, update configuration, or permissions. Review an update's source, release notes, compatibility, tests, and diff before merging it. An alert or an update proposal is useful input, not proof that all dependency risk has been found or fixed.

## Code Scanning and CodeQL

**Code scanning** analyzes source code for certain patterns that may indicate vulnerabilities or other problems. **CodeQL** is GitHub's semantic code analysis technology, which can query code to identify supported patterns in supported languages and configurations.

Scanning can help find issues for human review, but it does not find every vulnerability. It is not a replacement for code review, testing, threat modeling, or other security assessment appropriate to the project. Review findings in context and consider whether the code and configuration have been analyzed as intended.

## GitHub Actions Security Basics

GitHub Actions workflows can run commands when repository events occur. A workflow may have access to repository contents, tokens, or configured secrets, so review workflow changes carefully. Beginner safeguards include:

- Review third-party actions and their maintainers, source, permissions, and update history before using them.
- Pin dependencies or action versions when appropriate. For higher assurance, teams may pin an action to a full commit SHA and update it through a reviewed process.
- Grant workflows and jobs only the permissions they need. Use minimal token permissions where supported.
- Protect secrets using the repository or organization secret mechanisms and limit which workflows can access them.
- Avoid printing secrets to logs. Be careful with commands and debugging output that might reveal environment values.
- Review changes to workflow files as security-sensitive changes, including triggers, permissions, external actions, and handling of untrusted input.

Exact controls depend on the repository configuration. A workflow that passes does not automatically mean it is safe.

## Branch Protection

As introduced in Module 04, protected branches can require changes to go through a pull request and may require approvals, passing status checks, resolved review conversations, or restrictions on direct pushes. These rules help make review a normal part of changing an important branch.

Available settings and enforcement depend on repository configuration, organization policy, and GitHub account or plan capabilities. Branch protection supports a security process; it does not make every change safe by itself.

## Repository Visibility

- **Public:** Anyone can view the repository. Public repositories can be useful for a cybersecurity portfolio, but must contain only material cleared for public release.
- **Private:** Access is limited to authorized users, subject to GitHub and organization settings. Private is not the same as secret storage, and authorized users or connected workflows may still access or copy content.

Do not commit secrets to either type. Least privilege means giving people, applications, and workflows only the access required for their task, and reviewing that access over time.

## Security Before Convenience

It can feel faster to paste a credential into a configuration file or commit it temporarily to make a project work. Do not do that, even in a private repository. Secrets can be copied, logged, included in history, or exposed through permissions and automation. Use an approved secret store or local environment configuration, keep real values out of tracked examples, and review the staged change before committing.

## Security Review Before Publishing

Use these commands from the repository root and read each result before sharing work:

```powershell
git status
git diff
git diff --staged
git log --oneline
```

- `git status` shows the current branch and staged, unstaged, or untracked changes. It helps you notice unexpected files.
- `git diff` shows unstaged changes to tracked files. It does not normally display the contents of an untracked file.
- `git diff --staged` shows what is prepared for the next commit. Check that exact content for secrets and unrelated changes.
- `git log --oneline` summarizes recent commit messages. It helps you review recent history, but it does not scan old commit contents for secrets.

Before publishing, also check repository visibility, remote destination, workflows, dependency alerts, scanning configuration, and any project-specific review requirements. Tools can help, but they do not guarantee that every sensitive item has been found.

## Knowledge Check

Try to answer these questions before opening the answers:

1. What does `.gitignore` do, and what does it not do for a file Git already tracks?
2. What belongs in `.env.example`, and why should real values stay out of it?
3. Does secret scanning find every possible secret?
4. What is the first priority if a real credential is committed?
5. Why are GitHub Actions workflow changes worth reviewing carefully?

<details>
<summary>Knowledge check answers</summary>

1. It helps exclude matching untracked files from normal staging. It does not untrack files or erase existing history.
2. Variable names and placeholders only, such as `API_KEY=example-placeholder`. Real values must stay in an approved local or secret-management system.
3. No. It detects certain patterns in supported configurations, and coverage is not complete.
4. Treat it as exposed and revoke or rotate it through the issuing provider.
5. Workflows can run code and may access repository permissions or secrets, so unsafe triggers, actions, permissions, or logging can expose data or enable unintended changes.

</details>
