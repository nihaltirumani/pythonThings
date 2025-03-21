import random

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
index = 0
randomiser = 0
decode_key = ""
encoded_message = ""

print("Welcome to encoder.")

message = input("Enter the message that you what to encode: ")

while not index == len(message):
    if message[index] in alphabet_list: 
        randomiser = random.randint(1,9)
        decode_key = decode_key + str(randomiser)
        encoded_message = encoded_message + alphabet_list[(alphabet_list.index(message[index]) + randomiser) % 26]
        index += 1
    elif message[index] == " ":
        decode_key = decode_key + "0"
        encoded_message = encoded_message + alphabet_list[random.randint(0, 25)]
        index += 1
    else:
        index += 1

print("Encrypted message:", encoded_message)
print("decryption key:", decode_key)