# GitHub for Cybersecurity

**A hands-on project for learning Git, GitHub, secure collaboration, cybersecurity documentation, Python log analysis, automated testing, and continuous integration.**

[![Validate Log Parser](https://github.com/BecomingCyber/GitHub-for-Cybersecurity/actions/workflows/validate-log-parser.yml/badge.svg)](https://github.com/BecomingCyber/GitHub-for-Cybersecurity/actions/workflows/validate-log-parser.yml)

## Project Overview

This repository began as a Git and GitHub learning project and grew into a small defensive cybersecurity capstone. It demonstrates both the fundamentals of version control and how those practices can support cybersecurity documentation and review workflows.

It is intended for cybersecurity students, career changers, SOC learners, digital forensics learners, recruiters, hiring managers, and technical reviewers. The material assumes little programming experience and uses PowerShell examples where useful.

> **Simulation notice:** All incidents, logs, usernames, hosts, IP addresses, and investigation scenarios in this repository are fictional training data. The labs are learning exercises, not production incident-response experience.

## What This Project Demonstrates

- Git fundamentals and local version control
- GitHub repositories and remote workflows
- Repository security and safe publishing practices
- Branches, pull-request concepts, and change review
- SOC-style investigation documentation using fictional data
- Simulated incident investigation and timeline writing
- Python log parsing and simple defensive threshold detection
- Automated tests with Python's built-in `unittest`
- GitHub Actions CI validation
- Documentation, change tracking, and reviewable commits

## Learning Path

| Path                                                                     | Focus                                                                                   |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| [01-git-basics](01-git-basics/README.md)                                 | Git fundamentals and the local version-control workflow                                 |
| [02-github-basics](02-github-basics/README.md)                           | Remote repositories, push, pull, fetch, clone, and GitHub concepts                      |
| [03-cybersecurity-workflow](03-cybersecurity-workflow/README.md)         | Using Git to document a simulated SOC investigation                                     |
| [04-branches-and-pull-requests](04-branches-and-pull-requests/README.md) | Branches, review workflows, pull requests, and protecting `main`                        |
| [05-github-security](05-github-security/README.md)                       | Repository security, secrets, Dependabot, CodeQL, Actions security, and safe publishing |
| [labs](labs/)                                                            | Hands-on exercises corresponding to the learning modules                                |

## Defensive Log Analysis Capstone

The capstone analyzes a bundled fictional authentication log with a small Python script. The sample includes this intentional training pattern:

| Field           | Simulated value     |
| --------------- | ------------------- |
| Source IP       | `192.168.10.25`     |
| Account         | `lab-user`          |
| Target host     | `LAB-WKS-01`        |
| Failed attempts | `12`                |
| Alert threshold | `5` failed attempts |

The analyzer groups failed attempts by source IP, account, and target host, then reports groups that meet or exceed the configured threshold. The bundled sample contains **26 total authentication events**, **11 successful authentications**, and **15 failed authentications**.

**A threshold match is a prompt for investigation, not proof of malicious activity.** The fictional IP is not a real attacker address or attribution.

## Project Architecture

```text
GitHub-for-Cybersecurity/
├── 01-git-basics/                 # Git fundamentals and command reference
├── 02-github-basics/              # GitHub concepts and remote workflow
├── 03-cybersecurity-workflow/      # Simulated incident documentation
├── 04-branches-and-pull-requests/  # Branch and review workflow
├── 05-github-security/             # Repository security learning material
├── labs/                           # Five guided hands-on exercises
├── sample-data/
│   └── authentication.log          # Fictional authentication events
├── scripts/
│   └── log_parser.py               # Defensive sample-log analyzer
├── tests/
│   └── test_log_parser.py          # Seven standard-library tests
├── .github/
│   └── workflows/
│       └── validate-log-parser.yml # Read-only CI validation workflow
├── docs/                           # Currently empty
├── .gitignore
└── README.md
```

## How the Analyzer Works

```text
Fictional Authentication Log
             |
             v
        Python Parser
             |
             v
  Parse Authentication Events
             |
             v
 Group Failed Attempts By:
 Source IP + Account + Target Host
             |
             v
   Compare Against Threshold
             |
             v
 Report Potential Repeated Login Activity
```

The analyzer reads only the bundled fictional log. It parses valid authentication events, skips and counts malformed event lines, counts successes and failures, groups failed attempts by source/account/host, and reports groups meeting the threshold. It uses simple threshold-based logic, not machine learning or a SIEM integration.

## Run the Project

Install Python 3.12 or another compatible Python 3 release. From PowerShell, clone the repository:

```powershell
git clone https://github.com/BecomingCyber/GitHub-for-Cybersecurity.git
cd GitHub-for-Cybersecurity
```

Run the analyzer, tests, or syntax validation from the repository root:

```powershell
python scripts/log_parser.py
python -m unittest discover -s tests -v
python -m py_compile scripts/log_parser.py tests/test_log_parser.py
```

## Automated Testing

[`tests/test_log_parser.py`](tests/test_log_parser.py) contains seven automated tests using Python's built-in `unittest` framework. The tests cover:

- Valid authentication-event parsing
- Malformed-line rejection and safe skip counting
- Failure grouping by source IP, account, and target host
- The five-failure threshold boundary
- Below-threshold behavior
- Bundled sample totals
- The expected simulated repeated-login pattern

No third-party Python packages are required.

## GitHub Actions CI

The [validation workflow](.github/workflows/validate-log-parser.yml) runs for relevant changes pushed to `main`, pull requests targeting `main`, and manual `workflow_dispatch` runs. It checks out the repository, sets up Python, displays the Python version, validates Python syntax, runs the unit tests, and executes the sample analyzer.

Workflow permissions are restricted to `contents: read`. CI passing is one layer of validation and does not prove that software is completely secure.

## Security Practices

- Use `.gitignore` to help keep matching untracked local files out of commits, but remember it does not remove tracked files or erase Git history.
- Do not commit credentials, passwords, API keys, tokens, private keys, production logs, or real forensic evidence.
- Use fictional and sanitized sample data only. This project contains no real production logs or forensic evidence.
- Review `git status`, `git diff`, and `git diff --staged` before committing or publishing.
- If a credential is exposed, treat it as compromised and revoke or rotate it with its provider, then follow approved response procedures.
- Use least-privilege permissions for automation. The included workflow requests read-only repository contents access.
- Review repository visibility, files, screenshots, and history before publication.

## Key Commands

| Command                     | Purpose                                                                  |
| --------------------------- | ------------------------------------------------------------------------ |
| `git status`                | See current branch and pending file changes                              |
| `git diff`                  | Review unstaged changes to tracked files                                 |
| `git diff --staged`         | Review changes selected for the next commit                              |
| `git add <file>`            | Stage a chosen file's changes                                            |
| `git commit -m "message"`   | Save staged changes in local history                                     |
| `git log --oneline`         | Scan recent commit summaries                                             |
| `git branch --show-current` | Confirm the current local branch                                         |
| `git switch -c <branch>`    | Create and switch to a local branch                                      |
| `git remote -v`             | Inspect configured remote URLs                                           |
| `git push`                  | Send committed changes to the configured remote                          |
| `git pull`                  | Fetch and integrate remote changes into the current branch               |
| `git fetch`                 | Retrieve remote updates without integrating them into the current branch |

## Skills Demonstrated

The repository provides practice with Git, GitHub, VS Code, PowerShell, Python, `unittest`, GitHub Actions, CI validation, log analysis, security and incident documentation, repository security, branch workflows, pull-request concepts, and secure development practices.

These are skills practiced through this learning project. Describe them as coursework or portfolio practice, not as employer, client, production, enterprise, or professional incident-response experience.

## Important Limitations

- All security events and data are simulated.
- This is not a production SIEM. The analyzer uses simple threshold-based detection.
- The project does not perform network monitoring or connect to external APIs.
- It contains no real forensic evidence and does not replace enterprise SOC tooling.
- Git is used for version control and documentation, not as a formal chain-of-custody system.
- CI passing does not guarantee software security.

## Project Status

The repository currently includes five learning modules, five hands-on labs, fictional SOC investigation examples, sanitized authentication training data, a Python authentication-log analyzer, seven automated tests, and GitHub Actions CI validation.

## Portfolio Context

This project demonstrates learning through hands-on implementation: documenting fictional investigations, reviewing changes with Git, writing a small defensive parser, testing its behavior, and validating it in CI. It shows practice with these workflows, not production cybersecurity experience.
