import random

word_list = [
    "apple", "banana", "orange", "grape", "kiwi",
    "pineapple", "strawberry", "watermelon", "blueberry", "peach",
    "carrot", "broccoli", "potato", "tomato", "cucumber",
    "pizza", "burger", "sandwich", "spaghetti", "sushi",
    "dog", "cat", "bird", "fish", "hamster",
    "tree", "flower", "grass", "sunflower", "rose",
    "book", "pen", "pencil", "notebook", "marker",
    "computer", "keyboard", "mouse", "monitor", "printer",
    "teacher", "student", "school", "classroom", "homework",
    "happy", "sad", "angry", "excited", "bored"
]

main_word = word_list[random.randint(0, 49)]
main_word_list = list(main_word)
alphabets = []
chances = 5
guessing_word = ""
letters_caught = 0

while chances > 0:
    letter = input(f"Enter letter in word which contains {len(main_word)} words : ")

    if letter == "end":
        quit()

    letter = letter[0]

    if letter in alphabets:
        print("You have used this letter. Try an another letter.")
    else:
        alphabets.append(letter)

        while letter in main_word_list:
                letters_caught += 1
                main_word_list.remove(letter)

        if letter in main_word:
            print(f"You got {letters_caught} letter!")

        else:
            print("You lost 1 chance!")
            chances -= 1

    for i in range(len(main_word)):
        if letter == main_word[i]:
            guessing_word += letter
        else:
            guessing_word += "_"
    print(guessing_word)

    letter = ""
    guessing_word = ""
    letters_caught = 0

    if main_word_list == []:
        print("You won!")
        quit()

print("You lost the game!")
