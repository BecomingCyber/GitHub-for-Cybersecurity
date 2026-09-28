# Sample Incident: Repeated Failed Login Attempts

> **Simulated training example:** Every name, event, time, and record below is fictional. This document does not describe a real incident or production investigation.

**Incident ID:** LAB-003  
**Alert Type:** Repeated Failed Login Attempts  
**Severity:** Medium  
**Status:** Closed - Simulated Activity  
**Source IP:** 192.168.10.25  
**Target Host:** LAB-WKS-01  
**Target Account:** lab-user

## 1. Incident Summary

A fictional SIEM alert detected repeated failed authentication attempts against the lab workstation `LAB-WKS-01`. The training record associated the attempts with the fictional private source address `192.168.10.25` and the lab account `lab-user`. Review of the exercise context confirmed that the activity was part of an authorized lab simulation.

## 2. Scope

This is simulated training data for learning how to document an investigation. It does not represent a real system, user, production event, or incident response engagement. All records and timestamps below were invented for the exercise. No real credentials or production logs are included.

## 3. Initial Alert

- **Incident ID:** LAB-003
- **Alert:** Repeated Failed Login Attempts
- **Severity:** Medium, as assigned by the fictional lab alert
- **Activity summary:** 12 failed login attempts within 5 minutes
- **Source IP:** 192.168.10.25, a fictional private RFC1918 address
- **Target Host:** LAB-WKS-01, a fictional lab workstation
- **Target Account:** lab-user, a fictional account

No password values or authentication secrets are part of this example.

## 4. Evidence Reviewed

The exercise documentation refers to these fictional sources:

- Simulated Windows Security event logs created for training.
- Fictional authentication records containing no real credentials.
- Lab-generated timestamps listed in the timeline below.

These descriptions are not real collected evidence and must not be treated as an evidence package.

## 5. Investigation Timeline

All times are fictional lab times on the same simulated exercise day. The timezone is intentionally unspecified because this training example does not model a real event record.

| Time  | Activity                                                                            |
| ----- | ----------------------------------------------------------------------------------- |
| 09:00 | Fictional SIEM alert generated for repeated failed login attempts.                  |
| 09:02 | Simulated triage started and the alert details were recorded.                       |
| 09:05 | The training record showed 12 failed attempts within five minutes.                  |
| 09:08 | The fictional source address `192.168.10.25` was reviewed against the lab scenario. |
| 09:12 | The activity was identified as part of the authorized simulation.                   |
| 09:15 | The simulated incident was documented as closed.                                    |

## 6. Observations

The following statements are observations from the fictional exercise materials:

- The simulated alert described 12 failed authentication attempts within five minutes.
- The training record listed `192.168.10.25` as the source address.
- The training record listed `LAB-WKS-01` as the target host and `lab-user` as the target account.
- The exercise instructions identified this activity as an authorized lab simulation.

## 7. Findings

The fictional records associate repeated failed authentication attempts against `LAB-WKS-01` and `lab-user` with source address `192.168.10.25`. This finding is limited to the supplied simulated training records and does not establish that any real system or account was involved.

## 8. Conclusion

Within the scope of this exercise, the activity was determined to be part of an authorized lab simulation. No conclusion about a real environment is made.

## 9. Remediation

The following safe documentation and lab actions were recorded:

- Confirm the activity matched the expected lab scenario.
- Review the example account lockout settings as a learning exercise. No real account settings were changed.
- Document the investigation steps and the limits of the fictional records.
- Close the simulated incident as `Closed - Simulated Activity`.

## 10. Lessons Learned

A beginner can use this exercise to practice documenting what an alert said, identifying the source of each observation, building a timeline, and distinguishing a finding from a conclusion. It also demonstrates why training data must be labeled clearly and why an investigation note should not claim more than its sources support.
