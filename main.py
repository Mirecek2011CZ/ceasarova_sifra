def encrypt(message, key):
    encrypted_message = ""

    for i in message:
        if i.isalpha():
            if 'a' <= i <= 'z':
                encrypted_message += chr(((ord(i) - ord('a') + key) % 26) + ord('a'))
            elif 'A' <= i <= 'Z':
                encrypted_message += chr(((ord(i) - ord('A') + key) % 26) + ord('A'))
        else:
            encrypted_message += i

    return encrypted_message

def decrypt(encrypted_message, key):
    return encrypt(encrypted_message, -key)

key = 3

message = input("Zadej text, ktery chces zasifrovat: ")

encrypted_message = encrypt(message, key)
print("Zasifrovany kod je:", encrypted_message)

decrypted_text = decrypt(encrypted_message, key)
print("Desifrovany kod je:", decrypted_text)