
import math

from utils.text_utils import normalize_alpha
from .running_key import CipherError


def _key_order(key: str):
    return [
        index
        for index, _ in sorted(enumerate(key), key=lambda item: (item[1], item[0]))
    ]


def _single_encrypt(text: str, key: str) -> str:
    cols = len(key)
    rows = math.ceil(len(text) / cols) if text else 0
    padded = text.ljust(rows * cols, "X")

    matrix = [list(padded[r * cols:(r + 1) * cols]) for r in range(rows)]

    out = []
    for col_index in _key_order(key):
        for r in range(rows):
            out.append(matrix[r][col_index])
    return "".join(out)


def _single_decrypt(cipher: str, key: str) -> str:
    cols = len(key)
    rows = math.ceil(len(cipher) / cols) if cipher else 0

    matrix = [["" for _ in range(cols)] for _ in range(rows)]

    index = 0
    for col_index in _key_order(key):
        for r in range(rows):
            if index < len(cipher):
                matrix[r][col_index] = cipher[index]
                index += 1

    return "".join("".join(row) for row in matrix)


def double_transposition_encrypt(text: str, key: str) -> str:
    text = normalize_alpha(text)
    key = normalize_alpha(key)

    if not text:
        raise CipherError("Plaintext is empty.")
    if not key:
        raise CipherError("Key is empty.")

    return _single_encrypt(_single_encrypt(text, key), key)


def double_transposition_decrypt(cipher: str, key: str) -> str:
    cipher = normalize_alpha(cipher)
    key = normalize_alpha(key)

    if not cipher:
        raise CipherError("Ciphertext is empty.")
    if not key:
        raise CipherError("Key is empty.")

    return _single_decrypt(_single_decrypt(cipher, key), key)
