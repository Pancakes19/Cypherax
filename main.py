print("##########################################")
print("")
print("         🧙 Welcome to Cypherax 🧙")
print("")
print("##########################################")
print("")

def shift_letter(char, key):
    if char.isupper():
        base = ord('A')
    elif char.islower():
        base = ord('a')
    else:
        return char
    return chr((ord(char) - base + key) % 26 + base)

def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += shift_letter(char, key)
    return encrypted_text

def caesar_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        decrypted_text += shift_letter(char, -key)
    return decrypted_text

choice1 = int(input(
    "State thy desire, my lord\n\n"
    "1: to Encrypt the runes\n"
    "2: to Decrypt their secrets?\n\n"
))

if choice1 == 1:
    plaintext = input("Whisper thy sacred words my liege:\n")
    key = int(input("Now chant the sealing spell:\n"))
    print("\nHere is your encrypted text bro:\n")
    print(caesar_encrypt(plaintext, key))

else:
    ciphertext = input("Whisper the runes of secrecy:\n")
    key = int(input("Now chant the sealing spell:\n"))
    print("\nHere is your decrypted text bro:\n")
    print(caesar_decrypt(ciphertext, key))
   










