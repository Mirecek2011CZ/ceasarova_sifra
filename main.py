def encode(key, message):
    
    final_text = " "
    
    for i in message:
        final_text = final_text + chr((ord(i) - 65 + key) % 26 + 65)
    return final_text

def decode(key, message):
    return encode(-key, message)

print(encode(1, "AZB"))