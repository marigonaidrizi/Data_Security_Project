import math


def _normalize_text(text):
    return text.replace(" ", "").upper()


def _key_order(key):
    return [index for index, _ in sorted(enumerate(key), key=lambda item: (item[1], item[0]))]


def single_transposition_encrypt(text, key):
    text = _normalize_text(text)
    key = _normalize_text(key)

    if not key:
        return "Key nuk mund te jete bosh!"

    cols = len(key)
    rows = math.ceil(len(text) / cols) if text else 0
    padded_text = text.ljust(rows * cols, "X")

    matrix = [list(padded_text[row * cols:(row + 1) * cols]) for row in range(rows)]

    result = ""
    for col_index in _key_order(key):
        for row in range(rows):
            result += matrix[row][col_index]

    return result


def single_transposition_decrypt(cipher, key):
    cipher = _normalize_text(cipher)
    key = _normalize_text(key)

    if not key:
        return "Key nuk mund te jete bosh!"

    cols = len(key)
    rows = math.ceil(len(cipher) / cols) if cipher else 0

    matrix = [["" for _ in range(cols)] for _ in range(rows)]

    index = 0
    for col_index in _key_order(key):
        for row in range(rows):
            if index < len(cipher):
                matrix[row][col_index] = cipher[index]
                index += 1

    result = ""
    for row in matrix:
        result += "".join(row)

    return result


def double_transposition_encrypt(text, key):
    first_pass = single_transposition_encrypt(text, key)
    if first_pass == "Key nuk mund te jete bosh!":
        return first_pass
    return single_transposition_encrypt(first_pass, key)


def double_transposition_decrypt(cipher, key):
    first_pass = single_transposition_decrypt(cipher, key)
    if first_pass == "Key nuk mund te jete bosh!":
        return first_pass
    return single_transposition_decrypt(first_pass, key)
