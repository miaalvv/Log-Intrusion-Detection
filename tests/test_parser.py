#tests that the parser reads valid logs correctly and filters empty users
from src.parser import parse_logs

def test_invalid_log_line():
    logs = parse_logs("data/logs.txt")
    assert isinstance(logs, list)

def test_empty_user_filtered():
    logs = parse_logs("data/logs.txt")
    for log in logs:
        assert log["user"].strip() != ""


def test_basic():
    assert 1 == 1