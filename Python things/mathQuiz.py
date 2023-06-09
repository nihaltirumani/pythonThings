import random
import time
index = 1

print("Welcome to maths quiz!")
time.sleep(1)
print("There are ten equations.")
time.sleep(1)
print("You have to answer them correctly.")
time.sleep(1)
print("The more the correct, the more the points!")
time.sleep(1)
print("Get ready in...")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!")

while index < 11:

    random_number = random.randint(1, 4)

    if random_number == 1:
        operator = "+"
    elif random_number == 2:
        operator = "-"
    elif random_number == 3:
        operator = "*"
    elif random_number == 4:
        operator = "/"

    num1 = str(random.randint(1, 25))
    num2 = str(random.randint(1, 25))
    question = "Answer the equation: " + num1 + " " + operator + " " + num2 + " " + "=" + " "

    num1 = int(num1)
    num2 = int(num2)

    print("Q."+str(index))
    try:
        user_answer = int(input(question))
    except ValueError:
        print("Enter a number, not letters")
        quit()

    if operator == "+":
        answer = num1 + num2
    if operator == "-":
        answer = num1 - num2
    if operator == "*":
        answer = num1 * num2
    if operator == "/":
        answer = num1 / num2

    if operator == "/":
        user_answer = float(user_answer)

    correct_answers = 0
    if answer == user_answer:
        print("Correct answer!")
        correct_answers += 1
    else:
        print("Wrong answer.")
        print(answer,"is the correct answer.")
    
    index += 1

print("You got", correct_answers, "point!")