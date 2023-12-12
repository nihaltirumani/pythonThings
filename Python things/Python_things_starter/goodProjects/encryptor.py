import random

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
index = 0
randomiser = 0
decyption_key = ""
encrypted_message = ""

print("Welcome to encyrptor.")

message = input("Enter the message that you what to encrypt: ")

while not index == len(message):
    if message[index] in alphabet_list: 
        randomiser = random.randint(1,9)
        decyption_key = decyption_key + str(randomiser)
        encrypted_message = encrypted_message + alphabet_list[(alphabet_list.index(message[index]) + randomiser) % 26]
        index += 1
    else:
        index += 1

print("Encrypted message:", encrypted_message)
print("decryption key:", decyption_key)