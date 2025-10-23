print("##########################################") 
print("") 
print("         🧙 Welcome to Cypherax 🧙") 
print("") 
print("##########################################") 
print("") 
#prompting the user for their choice 
choice1 = int(input("State thy desire, my lord \n \n 1: to Encrypt the runes \n 2: to Decrypt their secrets? \n \n")) 
if choice1 == 1: 
     plaintext = input("Whisper thy sacred words, that I may seal them within the cryptic runes: \n") 
else: ciphertext = input("Whisper the runes of secrecy, that I may decipher their hidden wisdom, my lord: \n")

def shift_letter(char, shift): 
     if char.isupper(): 
          base = ord('A') 
     elif char.islower(): 
          base = ord('a') 
     else: 
          return char 
     return chr((ord(char) - base + shift) % 26 + base)



def caesar_encrypt(plaintext, shift):
     encrypted_text = ""
     for char in plaintext:
          encrypted_text += shift_letter(char, shift)
     return encrypted_text
   


print(caesar_encrypt(plaintext, -7))
