













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