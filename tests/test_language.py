from app.language import detect_language


def test_detect_python():
    code = "def hello(name):\n    return f'hi {name}'"
    assert detect_language(code) == "python"


def test_detect_sql():
    code = "SELECT id, name FROM users WHERE active = 1"
    assert detect_language(code) == "sql"
