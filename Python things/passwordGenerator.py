# importing modules
import random


# varibles of different characters

lowercase_alphabets = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=\"{ }'[]:;\<>,.?/"


# other varibles for generating password

index = 0
password = ""


# Merge all the characters into one list

all_characters = list(lowercase_alphabets + uppercase_alphabets + numbers + symbols)


#asking the user for character limit and generating the output

character_range = int(input("Character range for password (limitations from 29) : "))

while index < character_range:
    password = password + all_characters[random.randint(0, len(all_characters))]
    index += 1

print("Your password is:", password)
