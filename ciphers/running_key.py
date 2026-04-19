
from utils.text_utils import normalize_alpha


class CipherError(ValueError):
    """Raised when cipher input is invalid."""


def running_key_encrypt(text: str, key: str) -> str:
    text = normalize_alpha(text)
    key = normalize_alpha(key)

    if not text:
        raise CipherError("Plaintext is empty.")
    if not key:
        raise CipherError("Key is empty.")
    if len(key) < len(text):
        raise CipherError(
            f"Key must be at least as long as the text "
            f"(key={len(key)}, text={len(text)})."
        )

    out = []
    for i, ch in enumerate(text):
        p = ord(ch) - ord("A")
        k = ord(key[i]) - ord("A")
        out.append(chr((p + k) % 26 + ord("A")))
    return "".join(out)


def running_key_decrypt(cipher: str, key: str) -> str:
    cipher = normalize_alpha(cipher)
    key = normalize_alpha(key)

    if not cipher:
        raise CipherError("Ciphertext is empty.")
    if not key:
        raise CipherError("Key is empty.")
    if len(key) < len(cipher):
        raise CipherError(
            f"Key must be at least as long as the cipher "
            f"(key={len(key)}, cipher={len(cipher)})."
        )

    out = []
    for i, ch in enumerate(cipher):
        c = ord(ch) - ord("A")
        k = ord(key[i]) - ord("A")
        out.append(chr((c - k + 26) % 26 + ord("A")))
    return "".join(out)
