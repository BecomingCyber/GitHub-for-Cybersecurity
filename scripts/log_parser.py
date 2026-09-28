"""Analyze fictional authentication events for repeated failed logins.

This beginner demonstration reads only the repository's sanitized training log.
It is educational and is not a production detection system.
"""

from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DEFAULT_THRESHOLD = 5

# Locate the repository root from this script, independent of the current folder.
REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SAMPLE_LOG = REPOSITORY_ROOT / "sample-data" / "authentication.log"


@dataclass(frozen=True)
class AuthenticationEvent:
    """One valid row from the fictional authentication log."""

    timestamp: datetime
    event_type: str
    username: str
    source_ip: str
    target_host: str
    result: str


def parse_log_line(line: str) -> AuthenticationEvent | None:
    """Parse a pipe-delimited event, returning None for invalid rows."""
    fields = line.strip().split("|")
    if len(fields) != 6:
        return None

    timestamp_text, event_type, username, source_ip, target_host, result = fields
    try:
        timestamp = datetime.fromisoformat(timestamp_text)
    except ValueError:
        return None

    if not all((event_type, username, source_ip, target_host)):
        return None
    if event_type != "authentication" or result not in {"Success", "Failed"}:
        return None

    return AuthenticationEvent(
        timestamp=timestamp,
        event_type=event_type,
        username=username,
        source_ip=source_ip,
        target_host=target_host,
        result=result,
    )


def analyze_events(events: list[AuthenticationEvent]) -> Counter[tuple[str, str, str]]:
    """Count failed events for each source, account, and target host."""
    failed_counts: Counter[tuple[str, str, str]] = Counter()
    for event in events:
        if event.result == "Failed":
            key = (event.source_ip, event.username, event.target_host)
            failed_counts[key] += 1
    return failed_counts


def print_summary(
    events: list[AuthenticationEvent],
    skipped_lines: int,
    threshold: int = DEFAULT_THRESHOLD,
) -> None:
    """Print event totals and groups that meet the failure threshold."""
    successful_count = sum(event.result == "Success" for event in events)
    failed_count = sum(event.result == "Failed" for event in events)
    failure_groups = analyze_events(events)

    print("Authentication Log Analysis")
    print("===========================")
    print(f"Total events: {len(events)}")
    print(f"Successful authentications: {successful_count}")
    print(f"Failed authentications: {failed_count}")
    print(f"Malformed lines skipped: {skipped_lines}")
    print(f"Alert threshold: {threshold} failed attempts")
    print()
    print("Potential Repeated Login Activity")
    print("---------------------------------")

    matching_groups = [
        (key, count) for key, count in failure_groups.items() if count >= threshold
    ]
    if not matching_groups:
        print("No source/account/host group met the threshold.")
    else:
        for (source_ip, username, target_host), count in sorted(matching_groups):
            print(f"Source IP: {source_ip}")
            print(f"Account: {username}")
            print(f"Target Host: {target_host}")
            print(f"Failed Attempts: {count}")
            print("Status: Threshold exceeded")
            print()

    print("A threshold match is a prompt for investigation, not proof of malicious activity.")


def main() -> None:
    """Read the bundled sample log and summarize its valid events."""
    try:
        log_lines = SAMPLE_LOG.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        print(f"Could not read the sample log at {SAMPLE_LOG}: {error}")
        return

    events: list[AuthenticationEvent] = []
    skipped_lines = 0

    for line in log_lines:
        # Blank lines and the explanatory comment are not event records.
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        event = parse_log_line(line)
        if event is None:
            skipped_lines += 1
        else:
            events.append(event)

    print_summary(events, skipped_lines)


if __name__ == "__main__":
    main()
