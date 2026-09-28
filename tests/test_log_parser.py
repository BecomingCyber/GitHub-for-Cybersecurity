"""Tests for the fictional defensive authentication-log training project."""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import log_parser


class LogParserTests(unittest.TestCase):
    """Check parsing, grouping, thresholds, and the bundled training data."""

    def test_parse_valid_authentication_event(self) -> None:
        line = (
            "2026-09-28T09:00:00+00:00|authentication|lab-user|"
            "192.168.10.25|LAB-WKS-01|Failed"
        )

        event = log_parser.parse_log_line(line)

        self.assertIsNotNone(event)
        assert event is not None
        self.assertEqual(event.timestamp.isoformat(), "2026-09-28T09:00:00+00:00")
        self.assertEqual(event.result, "Failed")
        self.assertEqual(event.username, "lab-user")
        self.assertEqual(event.source_ip, "192.168.10.25")
        self.assertEqual(event.target_host, "LAB-WKS-01")

    def test_malformed_line_is_rejected(self) -> None:
        self.assertIsNone(log_parser.parse_log_line("not a valid event"))

    def test_failed_events_are_grouped_by_all_three_fields(self) -> None:
        base_event = log_parser.parse_log_line(
            "2026-09-28T09:00:00+00:00|authentication|lab-user|"
            "192.168.10.25|LAB-WKS-01|Failed"
        )
        self.assertIsNotNone(base_event)
        assert base_event is not None

        same_group = [base_event, base_event]
        different_source = log_parser.AuthenticationEvent(
            base_event.timestamp, base_event.event_type, base_event.username,
            "192.168.10.26", base_event.target_host, "Failed"
        )
        different_username = log_parser.AuthenticationEvent(
            base_event.timestamp, base_event.event_type, "analyst",
            base_event.source_ip, base_event.target_host, "Failed"
        )
        different_host = log_parser.AuthenticationEvent(
            base_event.timestamp, base_event.event_type, base_event.username,
            base_event.source_ip, "LAB-WKS-02", "Failed"
        )

        counts = log_parser.analyze_events(
            same_group + [different_source, different_username, different_host]
        )

        self.assertEqual(counts[("192.168.10.25", "lab-user", "LAB-WKS-01")], 2)
        self.assertEqual(counts[("192.168.10.26", "lab-user", "LAB-WKS-01")], 1)
        self.assertEqual(counts[("192.168.10.25", "analyst", "LAB-WKS-01")], 1)
        self.assertEqual(counts[("192.168.10.25", "lab-user", "LAB-WKS-02")], 1)

    def test_exactly_five_failures_meet_default_threshold(self) -> None:
        event = log_parser.parse_log_line(
            "2026-09-28T09:00:00+00:00|authentication|lab-user|"
            "192.168.10.25|LAB-WKS-01|Failed"
        )
        self.assertIsNotNone(event)
        assert event is not None
        events = [event] * log_parser.DEFAULT_THRESHOLD

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            log_parser.print_summary(events, skipped_lines=0)

        self.assertIn("Alert threshold: 5 failed attempts", output.getvalue())
        self.assertIn("Failed Attempts: 5", output.getvalue())
        self.assertIn("Status: Threshold exceeded", output.getvalue())

    def test_four_failures_do_not_meet_default_threshold(self) -> None:
        event = log_parser.parse_log_line(
            "2026-09-28T09:00:00+00:00|authentication|lab-user|"
            "192.168.10.25|LAB-WKS-01|Failed"
        )
        self.assertIsNotNone(event)
        assert event is not None

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            log_parser.print_summary([event] * 4, skipped_lines=0)

        self.assertIn("No source/account/host group met the threshold.", output.getvalue())

    def test_sample_data_totals_and_expected_pattern(self) -> None:
        sample_path = Path(log_parser.SAMPLE_LOG)
        lines = sample_path.read_text(encoding="utf-8").splitlines()
        events = []
        for line in lines:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            event = log_parser.parse_log_line(line)
            self.assertIsNotNone(event, msg=f"Invalid sample event: {line}")
            if event is not None:
                events.append(event)

        successful = sum(event.result == "Success" for event in events)
        failed = sum(event.result == "Failed" for event in events)
        counts = log_parser.analyze_events(events)

        self.assertEqual(len(events), 26)
        self.assertEqual(successful, 11)
        self.assertEqual(failed, 15)
        self.assertEqual(
            counts[("192.168.10.25", "lab-user", "LAB-WKS-01")], 12
        )

    def test_malformed_record_is_counted_and_valid_records_continue(self) -> None:
        valid_line = (
            "2026-09-28T09:00:00+00:00|authentication|lab-user|"
            "192.168.10.25|LAB-WKS-01|Failed"
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_log = Path(temporary_directory) / "training.log"
            temporary_log.write_text(
                "# fictional test header\n" + valid_line + "\nmalformed row\n",
                encoding="utf-8",
            )
            output = io.StringIO()
            with patch.object(log_parser, "SAMPLE_LOG", temporary_log):
                with contextlib.redirect_stdout(output):
                    log_parser.main()

        self.assertIn("Total events: 1", output.getvalue())
        self.assertIn("Malformed lines skipped: 1", output.getvalue())
        self.assertIn("Failed authentications: 1", output.getvalue())


if __name__ == "__main__":
    unittest.main()
