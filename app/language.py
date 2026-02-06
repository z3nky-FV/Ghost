import re


def detect_language(code: str) -> str:
    snippet = code.strip().lower()
    if not snippet:
        return "plain text"

    patterns = [
        ("python", [r"\bdef\b", r"\bimport\b", r"\bself\b", r":\s*$"]),
        ("javascript", [r"\bfunction\b", r"\bconst\b", r"\blet\b", r"=>", r"console\.log"]),
        ("typescript", [r"\binterface\b", r"\btype\b", r":\s*(string|number|boolean)\b"]),
        ("java", [r"\bpublic\s+class\b", r"\bstatic\s+void\s+main\b", r"system\.out\.println"]),
        ("c#", [r"\bnamespace\b", r"\busing\s+system\b", r"\bpublic\s+class\b"]),
        ("go", [r"\bpackage\s+main\b", r"\bfunc\b", r"fmt\.print"]),
        ("sql", [r"\bselect\b", r"\binsert\b", r"\bupdate\b", r"\bdelete\b", r"\bfrom\b"]),
        ("html", [r"<html", r"<div", r"<body", r"<!doctype\s+html"]),
        ("css", [r"\.[a-z0-9_-]+\s*\{", r"#[a-z0-9_-]+\s*\{", r"\bcolor\s*:"])
    ]

    best_lang = "plain text"
    best_score = 0

    for lang, regexes in patterns:
        score = sum(1 for pattern in regexes if re.search(pattern, snippet, re.MULTILINE))
        if score > best_score:
            best_lang = lang
            best_score = score

    return best_lang
