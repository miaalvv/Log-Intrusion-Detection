def parse_logs(file_path):
    logs = []

    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 4:
                continue  # input validation (security point)

            timestamp = parts[0] + " " + parts[1]
            user = parts[2]
            action = parts[3]

            logs.append({
                "timestamp": timestamp,
                "user": user,
                "action": action
            })

    return logs
