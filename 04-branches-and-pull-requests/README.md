# Module 04: Branches and Pull Requests for Cybersecurity

Branches and pull requests give people a place to develop a change and have it reviewed before it becomes part of the project's primary line of work. In a cybersecurity project, that review can catch documentation gaps, logic errors, or sensitive data before a change is merged.

> **Training examples:** All scenarios in this module are fictional. Do not use production incident information or restricted data in a public learning repository.

## Learning Objectives

By the end of this module, you should be able to:

- Explain what a Git branch is and why a project may use a `main` branch.
- Create and switch to a feature branch using beginner-friendly Git commands.
- Choose a clear branch name without assuming one naming convention is required.
- Review file changes and compare a branch with `main`.
- Explain what a GitHub pull request does and how review comments and approvals fit into collaboration.
- Describe merge conflicts and branch protection at a beginner level.
- Explain why cybersecurity changes should be reviewed before merging.

## What Is a Branch?

A **branch** is a movable name that points to a line of commits in a Git repository. It lets you work on a change separately from another line of work. A branch is not a second folder or a full independent copy of every file. When you switch branches, Git updates the working files to match the selected branch, subject to any local changes that may prevent a safe switch.

For example, a project might have a primary branch named `main` and separate branches for proposed changes:

```text
main
  |
  |---- feature/update-investigation
  |
  |---- feature/add-detection-notes
```

The lines represent work based on the project history. A branch allows a change to be developed and reviewed without immediately changing `main`. In normal Git use, commits made on a feature branch do not become commits on `main` until the histories are integrated, commonly by merging a pull request on GitHub.

## Why Branches Help Cybersecurity Projects

Branches provide a focused place to prepare a change for review. Examples include:

- Updating incident-response documentation.
- Improving a detection rule or its explanation.
- Modifying a PowerShell security script.
- Adding log-analysis logic.
- Updating remediation guidance.
- Correcting forensic learning notes.
- Improving a project README.

For example, a learner can create `docs/update-incident-report`, revise a fictional report, inspect the diff, and ask a reviewer to check the wording before it becomes part of `main`.

## The Main Branch

The **main branch** commonly represents the primary or stable version of a project. Contributors often create a separate branch for proposed work and merge it into `main` after review. The default branch may be named `main`, but branch names and policies vary by project and organization. Always check which branch a repository actually uses.

## Branch Naming

A branch name should be easy to understand and related to the task. Examples include:

- `feature/add-log-analysis`
- `docs/update-incident-report`
- `fix/input-validation`
- `feature/add-ioc-parser`

Prefixes such as `feature`, `docs`, and `fix` can help people scan branch lists, but no single naming convention is mandatory. Follow the repository's contribution guidance when it has one. Avoid names that expose sensitive case details or personal information.

## Branch and Pull Request Workflow

```text
main
  |
  v
Create branch
  |
  v
Make change
  |
  v
Review change
  |
  v
Stage
  |
  v
Commit
  |
  v
Push branch
  |
  v
Open pull request
  |
  v
Review
  |
  v
Merge
  |
  v
Delete branch if no longer needed
```

The exact sequence depends on the project. A team may request draft review early, require automated checks, or use a particular merge method.

## What Is a Pull Request?

A **pull request (PR)** is a GitHub collaboration feature for proposing that changes from one branch be integrated into another branch. A pull request is not a core Git command. Git commands create and move local branches and commits; GitHub provides the pull request page, review discussion, approvals, checks, and merge controls.

A pull request typically shows the proposed changes and their diff. Reviewers can leave comments, request changes, or approve according to the project's rules. After appropriate review and any required checks, an authorized person can merge the proposed changes into the target branch, often `main`.

## Why Pull Requests Are Useful in Cybersecurity

Pull requests create a review point before a change is integrated. They can help a team:

- Use peer review to catch mistakes or unclear assumptions.
- Identify accidentally exposed secrets or sensitive data.
- Review the security logic in a detection, script, or configuration change.
- Improve documentation and explain intended behavior.
- Keep a discussion history about a proposed change.
- Validate test results and other required checks before merging.

A review does not guarantee that a change is secure. It adds a chance to identify issues and ask for evidence or clarification before integration.

## Review Before Merge

Reviewers should examine:

- Which files changed and whether each change fits the pull request's purpose.
- The diff, including additions, edits, and deletions.
- The security impact and any changed detection or response behavior.
- Whether credentials, secrets, personal data, or sensitive logs were included.
- Test results and other required checks.
- Whether the documentation is accurate and complete.
- Any unintended or unrelated changes.

If a problem is found, reviewers can leave a comment or request changes. The author can update the same branch and push another commit; the pull request then reflects the new branch contents.

## Merge Conflicts

A **merge conflict** happens when Git cannot automatically determine how to combine competing changes, such as two branches changing the same lines differently. Git pauses that integration and marks the conflicting parts so a contributor can review and choose the intended result.

A conflict is a normal collaboration situation, not evidence that someone is a bad developer. Resolve it by understanding both changes, discussing with the relevant contributors when needed, editing the file to the agreed result, and reviewing the result before committing or completing the merge. Do not resolve security-sensitive conflicts by blindly choosing one side.

## Protecting Main

Repositories can use **branch protection** or related rules to make changes to `main` go through review. Depending on repository configuration and account or organization capabilities, rules may require:

- Changes to arrive through pull requests.
- One or more approvals.
- Passing automated checks.
- Review conversations to be resolved.
- Restrictions on direct pushes to the protected branch.

Exact settings and available controls depend on the repository's configuration and GitHub plan or organization setup. Protection rules support a process; they do not replace careful review.

## Cybersecurity Review Mindset

Security-related changes can affect what an organization detects, how it responds, and what information it exposes. Reviewers should understand the purpose and scope of a change, check that examples are safe, consider failure cases, and ask whether the evidence supports the documentation. For code or configuration, they should also consider permissions, inputs, outputs, and operational impact.

Use fictional or approved sanitized data in learning repositories. Do not merge a change simply because automated checks pass, and do not assume a pull request approval proves that a system is secure.

## Knowledge Check

Answer these questions before opening the collapsed answers:

1. What does a branch let you do before the change is integrated into `main`?
2. Is a pull request a Git command or a GitHub collaboration feature?
3. What is a merge conflict, and why can it happen during normal collaboration?
4. Name three things a reviewer should inspect before a cybersecurity change is merged.
5. What kinds of rules might a repository use to protect `main`?

<details>
<summary>Knowledge check answers</summary>

1. Develop and commit a proposed change separately so it can be reviewed before integration.
2. A pull request is a GitHub collaboration feature, not a core Git command.
3. It occurs when Git cannot automatically combine competing changes. It can happen when collaborators edit overlapping parts of a file.
4. Examples include changed files and diffs, security impact, possible secrets, test results, documentation, and unrelated changes.
5. Rules may require pull requests, approvals, passing checks, resolved conversations, or restrict direct pushes. The exact rules depend on repository settings and available capabilities.

</details>
