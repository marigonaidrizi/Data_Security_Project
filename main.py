from running_key import running_key_encrypt, running_key_decrypt
from double_transposition import double_transposition_encrypt, double_transposition_decrypt

while True:
    print("\n------ MENU -----")
    print("1. Running Key Encrypt")
    print("2. Running Key Decrypt")
    print("3. Double Transposition Encrypt")
    print("4. Double Transposition Decrypt")
    print("5. Exit")

    choice = input("Zgjedh: ")

    if choice == "1":
        text = input("Text: ")
        key = input("Key: ")
        print("Encrypted:", running_key_encrypt(text, key))

    elif choice == "2":
        cipher = input("Cipher: ")
        key = input("Key: ")
        print("Decrypted:", running_key_decrypt(cipher, key))

    elif choice == "3":
        text = input("Text: ")
        key = input("Key: ")
        print("Encrypted:", double_transposition_encrypt(text, key))

    elif choice == "4":
        cipher = input("Cipher: ")
        key = input("Key: ")
        print("Decrypted:", double_transposition_decrypt(cipher, key))

    elif choice == "5":
        print("Exit...")
        break

    else:
        print("Zgjedhje e pavlefshme!")

