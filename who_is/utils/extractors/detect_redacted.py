def detect_redacted(search_string: str) -> bool:

    if "redacted" in search_string.lower():
        return True

    else:
        return False
