import csv
from parser import parse_logs
from detector import detect_suspicious_activity
from alert import generate_alerts
from summarizer import save_summary

def evaluate(detected_users, ground_truth):
    true_positives = len(set(detected_users) & set(ground_truth))
    false_positives = len(set(detected_users) - set(ground_truth))
    false_negatives = len(set(ground_truth) - set(detected_users))

    detection_rate = true_positives / len(ground_truth) if ground_truth else 0
    false_positive_rate = false_positives / (true_positives + false_positives) if (true_positives + false_positives) else 0

    return {
        "detection_rate": detection_rate,
        "false_positive_rate": false_positive_rate
    }

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
    print("[INFO] Loading logs from file & starting log analysis...")
    logs = parse_logs("data/logs.txt")
    print(f"[INFO] Counting failed login attempts... Parsed {len(logs)} log entries")

    fail_counts = count_failures(logs) 
    ground_truth = ["user2"]
    print("[INFO] Running detection engine")

    suspicious_users = detect_suspicious_activity(logs)
    detected_users = [user["user"] for user in suspicious_users]
    metrics = evaluate(detected_users, ground_truth)
    print(f"[INFO] Metrics: {metrics}")
    print("[INFO] Saving CSV summary")
    save_csv_summary(fail_counts)

    if suspicious_users:
        print("[INFO] Suspicious activity detected")
        generate_alerts(suspicious_users)
    else:
        print("[INFO] No suspicious activity found")

    summary = {
    "alerts": suspicious_users,
    "metrics": metrics
    }
    print("[INFO] Saving final summary JSON")
    save_summary(summary)

if __name__ == "__main__":
    main()
