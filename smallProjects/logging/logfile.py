print("Welcome to logging!")
print("set on or off.")
print("Set \"state\" to show conditon of the state.")
print("Note: the command will be noted on the log.txt file")

running = True
user_input = ""
state = None
file = open("/Users/nihalTirumani/Desktop/pythonThings/smallProjects/logging/log.txt", "a")

file.write("{\n")
while running:
    user_input = input()
    if user_input.lower() == "on":
        state = True
        file.write("state = True\n")
        print("The state was set on.")

    elif user_input.lower() == "off":
        state = False
        file.write("state = False\n")
        print("The state was set off.") 

    elif user_input.lower() == "state":
        file.write("print(state)\n")
        print(state)

    elif user_input.lower() == "end":
        running = False
        file.write("program ended\n")
    else:
        file.write(f"error with invalid user input contains {user_input}\n")
        print(f"No command called {user_input}")

file.write("}\n")