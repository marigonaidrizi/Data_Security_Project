def running_key_encrypt(text, key):
    text = text.replace(" ", "").upper()
    key = key.replace(" ", "").upper()

    if len(key) < len(text):
        return "Key duhet me qenë më i gjatë se text!"

    result = ""

    for i in range(len(text)):
        p = ord(text[i]) - ord('A')
        k = ord(key[i]) - ord('A')

        c = (p + k) % 26
        result += chr(c + ord('A'))

    return result


def running_key_decrypt(cipher, key):
    cipher = cipher.upper()
    key = key.upper()

    result = ""

    for i in range(len(cipher)):
        c = ord(cipher[i]) - ord('A')
        k = ord(key[i]) - ord('A')

        p = (c - k + 26) % 26
        result += chr(p + ord('A'))

    return result
