## Security Considerations
- Input validation for malformed log entries  
- Threshold-based detection to reduce false positives  
- No sensitive data stored  

## Security Invariants

- Invalid log entries are rejected during parsing
- Only predefined actions are accepted (LOGIN_SUCCESS, LOGIN_FAILED)
- No sensitive data (e.g., passwords) is stored
- All processing is done on structured, sanitized input