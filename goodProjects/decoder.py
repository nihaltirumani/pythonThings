index = 0
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
decoded_message = ""

print("Welcome to decoder.")

encoded_message = input("Enter encoded message: ")#"ropft"
decode_key = input("Enter decode key: ")#'46858'

while not index == len(encoded_message):
    decoded_letter = alphabet_list[int(alphabet_list.index(encoded_message[index]) - int(decode_key[index]))]
    if decode_key[index] != "0":
        decoded_message = decoded_message + decoded_letter
        index += 1
    elif decode_key[index] == "0":
        decoded_message = decoded_message + " "
        index += 1

print("Decoded message:", decoded_message)# nihal