index = 0
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
decrypted_message = ""

print("Welcome to decryptor.")

encrypted_message = input("Enter encrypted message: ")#"ropft"
decryption_key = input("Enter decryption key: ")#'46858'

while not index == len(encrypted_message):
    decrypted_letter = alphabet_list[int(alphabet_list.index(encrypted_message[index]) - int(decryption_key[index]))]
    if decryption_key[index] != "0":
        decrypted_message = decrypted_message + decrypted_letter
        index += 1
    elif decryption_key[index] == "0":
        decrypted_message = decrypted_message + " "
        index += 1

print("Decrypted message:", decrypted_message)