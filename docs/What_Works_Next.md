## What Works
- End-to-end pipeline execution — the full ingest → parse → detect → alert → summarize
  pipeline runs with a single `make up && make demo` command
- Log parsing with input validation — malformed entries and invalid actions are
  rejected before reaching the detector
- Accurate detection of failed logins — users with 5 or more failed login attempts
  are correctly flagged using a configurable threshold
- Alert generation — flagged users trigger printed alerts in the terminal output
- CSV output — results.csv is generated under artifacts/release/ with per-user
  failed attempt counts and flagged status
- JSON summary output — summary.json is exported with alerts, metrics, and total
  logs processed
- Evaluation metrics — detection rate and false positive rate are calculated and
  included in the summary
- Fully testable modular system — all core modules have unit tests covering happy
  path, negative, and edge cases
- CI pipeline — GitHub Actions builds the project, runs all tests, and reports
  coverage on every push
- Network capture analysis — sample.pcap is loaded and processed by the pipeline,
  with total packet count exported to summary.json

## What's Next
- Time-based detection windows — currently all failed logins are counted globally;
  future work would flag users who hit the threshold within a rolling time window
  (e.g., 5 failures in 60 seconds)
- Real-time monitoring — extend the pipeline to tail live log files instead of
  processing a static input file
- Dashboard visualization — build a simple web dashboard to display alerts and
  metrics in real time rather than only exporting to JSON/CSV
- Larger and real-world datasets — test against real syslog or auth.log data to
  validate detection accuracy beyond the sample dataset
- Multi-user and IP-based detection — correlate failed logins across multiple
  usernames from the same source to catch credential stuffing attacks