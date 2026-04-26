import csv
from parser import parse_logs
from detector import detect_suspicious_activity
from alert import generate_alerts
from summarizer import save_summary

def count_failures(logs):
    fail_counts = {}

    for log in logs:
        user = log["user"]
        status = log["action"]

        if user not in fail_counts:
            fail_counts[user] = 0

        if status == "LOGIN_FAILED":
            fail_counts[user] += 1

    return fail_counts

def save_csv_summary(user_fail_counts):
    with open("artifacts/release/results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["user", "failed_attempts", "flagged"])

        for user, count in user_fail_counts.items():
            flagged = count >= 5
            writer.writerow([user, count, flagged])

def main():
    print("[INFO] Starting log analysis...")

    logs = parse_logs("data/logs.txt")
    print(f"[INFO] Parsed {len(logs)} log entries")

    fail_counts = count_failures(logs) 
    suspicious_users = detect_suspicious_activity(logs)
    save_csv_summary(fail_counts)

    if suspicious_users:
        print("[INFO] Suspicious activity detected")
        generate_alerts(suspicious_users)
    else:
        print("[INFO] No suspicious activity found")

    save_summary(suspicious_users)

if __name__ == "__main__":
    main()
