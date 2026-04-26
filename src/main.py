from parser import parse_logs
from detector import detect_suspicious_activity
from alert import generate_alerts
from summarizer import save_summary

def main():
    print("[INFO] Starting log analysis...")

    logs = parse_logs("data/logs.txt")
    print(f"[INFO] Parsed {len(logs)} log entries")

    suspicious_users = detect_suspicious_activity(logs)

    if suspicious_users:
        print("[INFO] Suspicious activity detected")
        generate_alerts(suspicious_users)
    else:
        print("[INFO] No suspicious activity found")

    save_summary(suspicious_users)

if __name__ == "__main__":
    main()
