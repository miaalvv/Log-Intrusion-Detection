#reads log.txt, parses it, and returns a list of log entries as dictionaries with keys: timestamp, user, action
def parse_logs(file_path):
    logs = []

    with open(file_path, "r") as f:
        for line in f:
            #Step 1 - Basic parsing with input validation (security point)
            parts = line.strip().split()
            if len(parts) != 4:
                print("[WARN] Invalid log entry skipped (wrong format)")
                continue
            
            timestamp = parts[0] + " " + parts[1]
            user = parts[2]
            action = parts[3]

            #Step 2 - Sanitize user input (security point)
            if not user.strip():
                print("[WARN] Invalid log entry skipped (empty user)")
                continue

            valid_actions = ["LOGIN_SUCCESS", "LOGIN_FAILED"]
            if action not in valid_actions:
                print(f"[WARN] Invalid action '{action}' skipped")
                continue

            logs.append({
                "timestamp": timestamp,
                "user": user,
                "action": action
            })
    print(f"[INFO] Parsed {len(logs)} valid log entries")
    return logs
