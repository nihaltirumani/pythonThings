"""
    encryptionSoftware20.py
This project is the updated version (version 2.0) of encryptor.py and dencryptor.py
with merged and better encryption.
"""
import random

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
index = 0
randomiser = 0
encrypted_message = ""
decrypted_message = ""

encryption_or_decryption = input("Encryption (1) or decryption (0): ")

if encryption_or_decryption == "1":
    message = input("Enter the message: ")

    for i in range(len(message)):
        if message[index] in alphabet_list: 
            randomiser = random.randint(1, 99)
            encrypted_message += f"{randomiser:02}"
            encrypted_message += alphabet_list[(alphabet_list.index(message[index]) + randomiser) % 26]
            index += 1

        elif message[index] == " ":
            encrypted_message += "01b"
            index += 1
        
        else:
            index += 1

    print("Encrypted message:", encrypted_message)

elif encryption_or_decryption == "0":
    encrypted_message = input("Enter encrypted message: ")

    for i in range(int(len(encrypted_message) / 3)):
        if encrypted_message[index : index + 3] == "01b":
            decrypted_message += " "
            index += 3
        else:
            decrypted_letter = alphabet_list[int(alphabet_list.index(encrypted_message[index + 2]) - (int(encrypted_message[index : index + 2]) % 26))]
            decrypted_message = decrypted_message + decrypted_letter
            index += 3

    print("Decrypted message:", decrypted_message)