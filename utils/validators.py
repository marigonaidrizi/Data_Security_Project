from .text_utils import normalize_alpha


def validate_running_key(text: str, key: str) -> str | None:
    """Return an error message string, or ``None`` if the input is valid."""
    t = normalize_alpha(text)
    k = normalize_alpha(key)
    if not t:
        return "Text is empty after normalization."
    if not k:
        return "Key is empty after normalization."
    if len(k) < len(t):
        return f"Key too short: need >= {len(t)} letters, got {len(k)}."
    return None


def validate_double_transposition(text: str, key: str) -> str | None:
    t = normalize_alpha(text)
    k = normalize_alpha(key)
    if not t:
        return "Text is empty after normalization."
    if not k:
        return "Key is empty after normalization."
    return None
