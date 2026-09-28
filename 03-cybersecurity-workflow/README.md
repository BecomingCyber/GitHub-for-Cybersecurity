# Module 03: Git for Cybersecurity Investigations

Git can help learners and teams document how an investigation develops. A clear set of notes and focused commits makes it easier to see what was observed, what changed, and why. This module uses a fictional SOC alert to practice those habits.

> **Training only:** The examples in this module are simulated. They do not describe a real incident or represent production incident-response experience.

## Learning Objectives

By the end of this module, you should be able to:

- Describe how Git can support cybersecurity documentation and change tracking.
- Explain the difference between an observation, a finding, a conclusion, and a remediation.
- Organize investigation notes, evidence references, and a timeline in a readable way.
- Use `git status`, `git diff`, `git add`, `git diff --staged`, `git commit`, and `git log` to track documentation changes.
- Explain how commit history can support review, collaboration, and reproducibility.
- Identify why Git does not replace formal evidence handling or organizational incident processes.
- Label lab work as simulated rather than production experience.

## How Git Can Support Cybersecurity Documentation

A cybersecurity investigation often produces information that changes over time. Git can preserve a reviewable history of approved documentation and project files, when its use fits the organization's policies. For example, version control can help with:

- **SOC investigations:** Track updates to a sanitized investigation summary or a fictional alert triage exercise.
- **Digital forensics notes:** Maintain versioned learning notes or templates. Do not use Git as the evidence store for original forensic material unless an approved process explicitly permits it.
- **Detection engineering:** Review changes to detection logic and its documentation.
- **Incident response documentation:** Track updates to approved response checklists and training playbooks.
- **Configuration tracking:** Review changes to permitted, non-sensitive configuration examples.
- **Security scripts:** See how a script evolves and inspect proposed changes before using it.
- **Remediation documentation:** Record the documented status and rationale for an approved corrective action.

Use only material you are authorized to store in the repository. Follow organizational requirements for classification, access control, retention, and approved systems.

## A Basic Investigation Workflow

A simplified investigation workflow can be represented as:

```text
Alert
  |
  v
Triage
  |
  v
Evidence Collection
  |
  v
Analysis
  |
  v
Findings
  |
  v
Remediation
  |
  v
Documentation
```

The real process varies by organization and incident type. Documentation should be created throughout the work, not only after it is complete. For approved notes or simulated exercises, Git can help track those documentation changes:

```text
Create notes
    |
    v
git status
    |
    v
Review changes
    |
    v
git add
    |
    v
git diff --staged
    |
    v
git commit
    |
    v
Documented investigation history
```

`git status` shows which files have changed. `git diff` can show unstaged edits to tracked files. `git add` selects the changes for a commit, and `git diff --staged` displays the selected changes for review. `git commit` saves the staged snapshot in local Git history. Review content and repository policy before storing or sharing investigation documentation.

## Why Commit History Can Be Useful

When used with suitable data and approved procedures, commit history can help a team:

- **Track investigation progress:** Focused commits can mark stages such as creating a case summary, adding a timeline, and recording findings.
- **Show when findings changed:** The history identifies which commit introduced a documented change. Commit timestamps are Git metadata, not proof of when an event occurred; record event timestamps separately with their source and timezone when relevant.
- **Document remediation updates:** A commit can show when the documentation was updated to record an approved remediation step.
- **Review changes:** A reviewer can inspect a diff to see exactly what changed.
- **Collaborate safely:** Teammates can review a proposed change before it is shared or integrated, subject to the team's workflow and access controls.
- **Support reproducibility:** Versioned documentation, scripts, and safe sample data can help someone repeat a lab or understand its method. A commit alone does not make a result reproducible; record inputs, tools, versions, assumptions, and steps as appropriate.

## Important Limits

Git history is not a substitute for:

- Formal evidence handling or secure evidence storage.
- Chain-of-custody procedures that document evidence possession, transfer, and integrity.
- Enterprise case-management systems.
- Legal evidence management requirements.
- Organizational incident-response procedures.

Do not place original evidence, restricted case material, or sensitive production data in an ordinary Git repository unless your organization has explicitly approved that use and controls. Follow the assigned evidence and case-management process.

## Cybersecurity Documentation Principles

Good investigation notes are clear, careful, and reviewable:

- **Record factual observations:** Write what the evidence or source actually showed, not what you assume it means.
- **Separate observations from conclusions:** Label direct observations separately from interpretations and decisions.
- **Document timestamps:** Record relevant event times and timezone or source context when known. Do not confuse an event timestamp with a Git commit timestamp.
- **Identify evidence sources:** Note which approved log, system, or artifact supports an observation. In a training example, label the source as fictional or simulated.
- **Avoid unsupported assumptions:** If something is unknown, say it is unknown and describe what would be needed to verify it.
- **Use consistent terminology:** Keep labels such as alert, observation, finding, and remediation distinct throughout the record.
- **Protect sensitive information:** Use approved repositories and access controls. Sanitize or fictionalize data before using it in a learning project.

## Observation, Finding, Conclusion, and Remediation

| Term            | Plain-language meaning                                                    | Example from a simulated investigation                                                             |
| --------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Observation** | A directly recorded fact from a stated source.                            | The fictional alert record lists 12 failed authentication attempts in five minutes.                |
| **Finding**     | A supported statement formed by reviewing one or more observations.       | The attempts in the lab record are associated with the fictional source address `192.168.10.25`.   |
| **Conclusion**  | The assessment made from the findings, within the limits of the evidence. | The activity matches the authorized training simulation.                                           |
| **Remediation** | An action taken or recommended to address a risk or improve controls.     | Confirm expected lab activity, review the lab account lockout configuration, and document closure. |

A conclusion should not claim more than the evidence supports. Record whether a remediation is proposed, completed, or not applicable so readers do not confuse a recommendation with a completed action.

## What Makes a Good Cybersecurity Commit?

A useful commit message says what changed. For example:

| Weak message | Stronger message                          |
| ------------ | ----------------------------------------- |
| `update`     | `Document repeated failed login findings` |
| `stuff`      | `Add authentication timeline`             |
| `changes`    | `Record simulated remediation steps`      |

Use one focused change per commit when practical. For example, keep a timeline update separate from a later findings update. Smaller commits make reviews more specific, help readers follow the investigation's documented progression, and make it easier to identify which change introduced a particular note. A commit is a record of repository content, not a formal audit or proof that an operational action occurred.

## Simulated vs Production Experience

Describe training labs as **simulated**, **lab**, or **coursework** experience. Do not present a fictional incident, sample data, or practice workflow as production incident response experience. Be clear about what you did, what data was simulated, and what the exercise does not demonstrate.

## Knowledge Check

Try to answer these questions before opening the answers:

1. Why might a team use Git to track approved investigation documentation?
2. How is an observation different from a finding?
3. Does a Git commit timestamp prove when an event occurred?
4. Name two responsibilities Git history does not replace.
5. Why should a learner label a fictional incident as simulated?

<details>
<summary>Knowledge check answers</summary>

1. It can provide a reviewable history of documentation changes and help collaborators understand what changed.
2. An observation is a recorded fact from a source; a finding is a supported statement formed by examining observations.
3. No. A commit timestamp records Git metadata, not the event time. Record event timestamps and their context separately.
4. Examples include formal evidence handling, chain of custody, enterprise case management, legal evidence requirements, and organizational response procedures.
5. To represent the work honestly and avoid implying that a training exercise was a real production incident.

</details>
