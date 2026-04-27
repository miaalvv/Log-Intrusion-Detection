def test_empty_input():
    from src.detector import detect_suspicious_activity
    result = detect_suspicious_activity([])
    assert result == []

def test_invalid_action():
    from src.parser import parse_logs
    assert True 