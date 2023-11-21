# Activity 2
message = input("Enter your message: ")
shift = int(input("Shift number: "))

def cipher(message):
    encryptedText = []
    decryptedText = []
    for char in message.upper():
        ascii_rep = ord(char)
        encryptedText.append(chr(ascii_rep + shift))
        decryptedText.append(chr(ascii_rep - shift))
    encodeMessage = "".join(encryptedText)
    decodeMessage = "".join(decryptedText)
    print(f"Encrypt: {encodeMessage}")
    print(f"Decrypt: {decodeMessage}")

cipher(message)

"""
print(ord("A") + 2) A = 65 + 2 = 67
print(chr(67)) = C
"""