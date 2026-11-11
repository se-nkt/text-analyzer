from analyzer import get_read_time


def test_basic():
    assert get_read_time("") == 0
    assert get_read_time("word " * 200, "general") == 2
    assert get_read_time("word " * 100, "math") == 2
