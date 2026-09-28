# Lab 03: Document a Simulated SOC Investigation with Git

> **Simulation only:** This lab takes place in a fictional environment. It does not use production systems or represent production SOC experience. Do not add real credentials, personal information, customer data, or production logs.

## 1. Objective

Practice documenting a simulated investigation in focused steps and using Git to review and record each documentation change. You will use `git status`, `git diff`, `git add`, `git diff --staged`, `git commit`, and `git log --oneline`.

You will also practice recording observations, updating findings, documenting remediation, and creating focused commits that tell a clear story.

## 2. Scenario

You are acting as a junior SOC analyst in a fictional lab environment. A simulated SIEM alert reports repeated failed login attempts. The exercise record contains:

- **Incident ID:** LAB-003
- **Source IP:** 192.168.10.25
- **Target Host:** LAB-WKS-01
- **Target Account:** lab-user
- **Failed Attempts:** 12

The source address is in RFC1918 private space. All names, events, and data in the lab are fictional. This is practice, not a real incident or production experience.

## 3. Prerequisites

- Git is installed and available in PowerShell.
- You have opened the learning repository in VS Code.
- Open **Terminal > New Terminal** and confirm that PowerShell is at the repository root.
- Start with a clean working tree for this lab, or carefully leave any pre-existing unrelated changes untouched. Check `git status` before you begin.

The commands below are instructions for you to run in your own learning repository. They are not run automatically by this guide.

## 4. Step 1: Confirm Repository Status

Run:

```powershell
git status
```

Check the current branch and whether there are existing staged, unstaged, or untracked changes. Do not include unrelated changes in the lab commits.

## 5. Step 2: Create `incident-LAB-003.md`

Create this file in the repository root. In PowerShell, run the following here-string command:

```powershell
@'
# Simulated SOC Incident Record

Incident ID: LAB-003
Alert Type: Repeated Failed Login Attempts
Source IP: 192.168.10.25
Target Host: LAB-WKS-01
Target Account: lab-user
Status: Under Investigation
'@ | Set-Content -Path .\incident-LAB-003.md -Encoding utf8
```

This writes only fictional training details to the new Markdown file. `Set-Content` replaces the target file if it already exists, so confirm that you are creating this lab file and do not use this command to overwrite unrelated work.

You can instead create the file in VS Code and enter the same content.

## 6. Step 3: Check Status Again

Run:

```powershell
git status
```

Git should list `incident-LAB-003.md` as untracked because it is a new file that has not yet been staged or committed. If other files are listed, keep them out of this lab's commits.

## 7. Step 4: Review the Incident File

Open `incident-LAB-003.md` in VS Code or display it in PowerShell:

```powershell
Get-Content .\incident-LAB-003.md
```

Confirm the incident fields are present, the status is `Under Investigation`, and the data is fictional. The file is untracked, so `git diff` will not display it yet.

## 8. Step 5: Stage the Incident Record

Stage only the new incident file:

```powershell
git add incident-LAB-003.md
```

`git add` selects the current version of the file for the next commit. It does not commit or upload it.

## 9. Step 6: Review Staged Changes

Run:

```powershell
git diff --staged
```

Check the exact content prepared for the commit. It should contain only the fictional incident record. If the diff includes anything unexpected, stop and correct the file before committing.

## 10. Step 7: Create the First Commit

After reviewing the staged diff, save the incident record in local Git history:

```powershell
git commit -m "Create simulated SOC incident record"
```

This commit records the initial incident details with status `Under Investigation`. It does not push anything to GitHub.

## 11. Step 8: Add an Investigation Timeline

Edit `incident-LAB-003.md` in VS Code and append this fictional timeline:

```markdown
## Investigation Timeline

All times below are fictional lab times on the same simulated exercise day.

| Time  | Activity                                                    |
| ----- | ----------------------------------------------------------- |
| 09:00 | Simulated alert generated.                                  |
| 09:02 | Triage started.                                             |
| 09:05 | 12 failed attempts confirmed in the fictional record.       |
| 09:08 | Fictional source address reviewed against the lab scenario. |
```

The timeline contains no real event timestamps. In a real process, document approved timestamps and timezone context according to organizational procedures.

## 12. Step 9: Review the New Changes

Run:

```powershell
git diff
```

Because this file is already tracked, `git diff` should show the new timeline as unstaged changes. Review it for accuracy and confirm that you changed only the intended file.

## 13. Step 10: Stage and Commit the Timeline Update

First stage the file, then inspect the staged version:

```powershell
git add incident-LAB-003.md
git diff --staged
```

If the staged diff contains only the timeline update, create the second commit:

```powershell
git commit -m "Add simulated authentication timeline"
```

The `git add` step must happen before this commit so the timeline update is included.

## 14. Step 11: Add Findings and Remediation Sections

Append these sections to `incident-LAB-003.md`:

```markdown
## Findings

The fictional training records associate 12 failed authentication attempts against LAB-WKS-01 and lab-user with source address 192.168.10.25. This statement applies only to the simulated data.

## Conclusion

The activity was determined to be authorized simulated lab activity. No conclusion about a real environment is made.

## Remediation

- Confirm the activity matches the expected lab scenario.
- Review the example account lockout settings as a learning exercise. No real account settings were changed.
- Document the investigation and close the simulated incident.
```

These sections distinguish a supported finding from the conclusion and the documented follow-up actions. Do not add real evidence or production claims.

## 15. Step 12: Change the Incident Status

In the incident record's initial details near the top, change:

```text
Status: Under Investigation
```

to:

```text
Status: Closed - Simulated Activity
```

The status update, findings, conclusion, and remediation will be reviewed together as one focused documentation update.

## 16. Step 13: Review the Final Changes Before Staging

Run:

```powershell
git diff
```

Review every changed line. Confirm that the findings refer only to the fictional records, the conclusion says the activity was authorized simulated lab activity, remediation is described as a learning exercise, and the status is `Closed - Simulated Activity`.

## 17. Step 14: Stage and Inspect

Stage only this incident file and review the exact staged patch:

```powershell
git add incident-LAB-003.md
git diff --staged
```

Confirm that the staged changes include the findings, conclusion, remediation, and final status, with no unrelated content.

## 18. Step 15: Create the Final Commit

After reviewing the staged diff, record the update:

```powershell
git commit -m "Document simulated findings and remediation"
```

This creates the third focused commit for the exercise. It does not push the commits to GitHub.

## 19. Step 16: Review the Investigation History

Run:

```powershell
git log --oneline
```

Look for the three lab commits:

- `Create simulated SOC incident record`
- `Add simulated authentication timeline`
- `Document simulated findings and remediation`

The sequence tells the story of how the documentation developed. It records repository changes, but it is not proof that a real operational investigation or remediation occurred.

## Investigation Commit History

```text
Create incident record
        |
        v
Add timeline
        |
        v
Document findings
        |
        v
Record remediation
        |
        v
Close incident
```

The final commit groups the findings, the simulated conclusion, the remediation notes, and the status change as one focused documentation update.

## Why Not Use One Giant Commit?

One large commit can combine many different changes, making it harder for a reviewer to understand what happened at each stage. Focused commits make the documentation easier to review and help readers follow the progression from initial record to timeline and final findings. They also make it easier to identify which update changed a particular statement.

Use commits to record changes to approved project files. Do not treat Git history as a replacement for formal evidence handling, chain of custody, enterprise case management, legal requirements, or organizational incident-response procedures.

## Final Challenge

Add a `Lessons Learned` section to `incident-LAB-003.md` with two or three points that a beginner could take from the simulated exercise. Choose a concise commit message that describes this documentation update. First determine how you would inspect, stage, review, and commit the change. Do not publish it as part of this challenge.

<details>
<summary>Hints</summary>

- Check the repository state before editing and review the unstaged changes afterward.
- Stage only `incident-LAB-003.md` and inspect the staged diff.
- Use a commit message that says the lessons learned were added to the simulated investigation record.

</details>

## Reflection Questions

1. Why did you check repository status before creating the incident note?
2. What did `git diff` show after you added the timeline?
3. Why did you run `git diff --staged` before each commit?
4. How do the three focused commits tell the investigation's documentation story?
5. Which formal investigation or evidence-handling requirements would Git not replace?
