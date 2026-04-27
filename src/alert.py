def generate_alerts(suspicious_users):
    alerts = []

    for user_data in suspicious_users:
        message = f"User {user_data['user']} has {user_data['failed_attempts']} failed login attempts"
        print(f"[ALERT] {message}")
        alerts.append(message)

    return alerts
