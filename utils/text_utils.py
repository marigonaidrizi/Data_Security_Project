def normalize_alpha(text: str) -> str:
    """Strip non-letter characters and uppercase the result.

    Mirrors the behaviour of the original CLI implementation: spaces are
    removed and the input is uppercased. Anything that is not an A-Z letter
    after that is also stripped to keep the cipher math safe.
    """
    if text is None:
        return ""
    cleaned = text.replace(" ", "").upper()
    return "".join(ch for ch in cleaned if "A" <= ch <= "Z")
