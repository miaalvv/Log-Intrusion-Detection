#It takes the parsed logs, counts LOGIN_FAILED events per user using a dictionary, and returns anyone who hits the threshold
from collections import defaultdict

def detect_suspicious_activity(logs, threshold=5):
    print("[INFO] Detecting suspicious activity...")
    failed_counts = defaultdict(int)

    for log in logs:
        if log.get("action") == "LOGIN_FAILED":
            user = log.get("user")
            if user:
                failed_counts[user] += 1

    suspicious_users = []

    for user, count in failed_counts.items():
        if count >= threshold:
            suspicious_users.append({
                "user": user,
                "failed_attempts": count
            })

    print(f"[INFO] Detected {len(suspicious_users)} suspicious users")
    
    return suspicious_users
    