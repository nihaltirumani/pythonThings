# Checks palindrone words like "racecar" or "madam"

user_word = input("Enter a word to check if it is palindrome: ")
if user_word == user_word[::-1]:
    print("Your word is palindrome!!")
else:
    print("Your word is not palindrome.")