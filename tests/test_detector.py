from src.detector import detect_suspicious_activity

def test_no_suspicious_activity():
    logs = [
        {"user": "user1", "action": "LOGIN_SUCCESS"},
        {"user": "user2", "action": "LOGIN_FAILED"},
    ]
    result = detect_suspicious_activity(logs, threshold=5)
    assert result == []

def test_detect_suspicious_user():
    logs = [{"user": "user2", "action": "LOGIN_FAILED"} for _ in range(5)]
    result = detect_suspicious_activity(logs, threshold=5)
    assert len(result) == 1
    assert result[0]["user"] == "user2"
    assert result[0]["failed_attempts"] == 5

def test_edge_case_exact_threshold():
    logs = [{"user": "user3", "action": "LOGIN_FAILED"} for _ in range(5)]
    result = detect_suspicious_activity(logs, threshold=5)
    assert len(result) == 1
    assert result[0]["user"] == "user3"

def test_below_threshold():
    logs = [{"user": "user4", "action": "LOGIN_FAILED"} for _ in range(3)]
    result = detect_suspicious_activity(logs, threshold=5)
    assert result == []

def test_negative_invalid_input():
    logs = [{"user": "user1"}]  
    result = detect_suspicious_activity(logs, threshold=5)
    assert result == []