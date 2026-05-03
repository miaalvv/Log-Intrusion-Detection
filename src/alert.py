def generate_alerts(suspicious_users):
    alerts = []

    for user_data in suspicious_users:
        user = user_data['user']
        count = user_data['failed_attempts']
        message = (
            f"SUSPICIOUS USER DETECTED: '{user}' attempted to log in {count} times "
            f"and failed every time — this exceeds the threshold and has been flagged."
        )
        print(f"[ALERT] {message}")
        alerts.append(message)

    return alerts
