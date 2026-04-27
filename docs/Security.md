## Security Considerations
- Input validation for malformed log entries
- Threshold-based detection to reduce false positives
- No sensitive data stored
- All processing is done on structured, sanitized input

## Security Invariants
- Invalid log entries are rejected during parsing — any line that does not follow the
  expected 4-part format (timestamp date, timestamp time, user, action) is skipped with a warning
- Only predefined actions are accepted (LOGIN_SUCCESS, LOGIN_FAILED) — any other
  action value is rejected before it reaches the detection engine
- No sensitive data (e.g., passwords, IP addresses) is stored or logged at any point
- All processing is done on structured, sanitized input — raw log lines are never
  passed directly to detection logic
- Plaintext log data is never written back to disk after processing
- Detection threshold is enforced server-side and cannot be bypassed by log content
- Output files (results.csv, summary.json) contain only aggregated counts and flags,
  never raw log lines or user credentials