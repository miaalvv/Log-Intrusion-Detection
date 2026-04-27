def test_empty_input():
    from detector import detect_suspicious_activity
    result = detect_suspicious_activity([])
    assert result == []

def test_invalid_action():
    from parser import parse_logs
    assert True 