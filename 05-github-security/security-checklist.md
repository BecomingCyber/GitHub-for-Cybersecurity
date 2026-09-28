# GitHub Repository Security Checklist

Use this checklist before committing, pushing, or publishing a cybersecurity learning repository. Adapt it to your organization's requirements. No checklist or scanning feature can guarantee that all risks have been found.

## Before the First Commit

- [ ] `.gitignore` exists and has been reviewed.
- [ ] `.env` and other local secret files are ignored where appropriate.
- [ ] Credentials are excluded.
- [ ] Private keys are excluded.
- [ ] Sensitive logs are excluded.
- [ ] Sample data is fictional, public, or properly sanitized and approved.
- [ ] Repository visibility has been considered and matches the intended audience.

## Before Every Commit

Review the repository and proposed changes:

```powershell
git status
git diff
git diff --staged
```

Check for:

- [ ] Credentials
- [ ] Tokens
- [ ] API keys
- [ ] Passwords
- [ ] Private keys
- [ ] Unexpected files
- [ ] Sensitive personal information
- [ ] Production logs
- [ ] Unrelated changes

`git diff` reviews unstaged changes in tracked files. `git diff --staged` reviews what is selected for the next commit. A new untracked file's contents may not appear in `git diff`, so open and inspect it directly before staging.

## Before Every Push

Confirm the branch, destination, and commits you intend to share:

```powershell
git branch --show-current
git remote -v
git log --oneline
git status
```

- [ ] The current branch is the intended branch.
- [ ] The remote URL points to the intended repository.
- [ ] Repository visibility is correct for the intended audience.
- [ ] Recent commit history has been reviewed.
- [ ] Staged content and committed content being pushed have been inspected.
- [ ] No secrets were added in the current changes or commits being shared.
- [ ] GitHub Actions workflow changes have been reviewed, if applicable.

`git log --oneline` shows commit summaries, not the full contents of historical changes. Review the relevant changes and files rather than treating commit messages as a secret scan.

## GitHub Security Features to Review

Check which features are available and how they are configured for this repository:

- [ ] Secret scanning
- [ ] Push protection
- [ ] Dependabot alerts
- [ ] Dependabot security updates
- [ ] Code scanning, including CodeQL where supported and configured
- [ ] Branch protection or related rules
- [ ] Pull request review requirements

Availability and configuration vary by repository, organization, GitHub plan, supported languages, and project settings. A feature being enabled does not guarantee that every issue or secret will be detected.

## If a Secret Is Exposed

- [ ] Treat the credential as exposed.
- [ ] Revoke or rotate it with the provider that issued it, immediately.
- [ ] Remove it from current project files and prevent reintroduction.
- [ ] Review Git history to understand where it remains.
- [ ] Follow provider and organizational guidance, including any approved history-cleanup procedure.
- [ ] Review provider access or activity logs where applicable.
- [ ] Document the incident without repeating the secret value.
- [ ] Do not assume deleting the file solved the exposure.

Credential rotation or revocation comes before history cleanup. Deleting a file or making a repository private does not invalidate a copied credential or remove it from earlier commits.

## Portfolio Repository Review

- [ ] No real employer data
- [ ] No customer data
- [ ] No production logs
- [ ] No confidential reports
- [ ] No internal infrastructure details
- [ ] No real forensic evidence
- [ ] No real credentials
- [ ] Simulated data is clearly labeled
- [ ] Screenshots are reviewed for sensitive information
- [ ] README accurately describes lab experience

- [ ] Repository reviewed before publication.
