import math

def single_transposition(text, key):
    cols = len(key)
    rows = math.ceil(len(text) / cols)

    matrix = []
    index = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            if index < len(text):
                row.append(text[index])
                index += 1
            else:
                row.append('X')
        matrix.append(row)

    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])

    result = ""
    for col_index, _ in key_order:
        for row in matrix:
            result += row[col_index]

    return result


def double_transposition_encrypt(text, key):
    text = text.replace(" ", "").upper()
    first = single_transposition(text, key)
    second = single_transposition(first, key)
    return second


def double_transposition_decrypt(cipher, key):
    first = single_transposition_decrypt(cipher, key)
    second = single_transposition_decrypt(first, key)
    return second

def single_transposition_decrypt(cipher, key):
    cols = len(key)
    rows = math.ceil(len(cipher) / cols)

    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0
    for col_index, _ in key_order:
        for row in range(rows):
            if index < len(cipher):
                matrix[row][col_index] = cipher[index]
                index += 1

    result = ""
    for row in matrix:
        result += "".join(row)

    return result