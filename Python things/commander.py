print("Welcome to commander. Type commands to make an action. Type \'help\" for more.")

run = True
command_list = ["help", "end", "print"]

while run:
    command = input("")
    if command in command_list:
        if command == command_list[0]:
            print("Here is the list of all commands", command_list)
        elif command == command_list[1]:
            run = False
        elif command == command_list[2]:
            command = input("input: ")
            print(command)
    else:
        print("Invlid command")

