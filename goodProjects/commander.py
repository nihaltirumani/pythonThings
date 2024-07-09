# Varibles
run = True
index = 0
commands_list = ["help", "end", "run", "print", "var"]
command_log = []
version = 1.3
variables = {}

# Welcoming the user
print("Welcome to commander", version, ". Type commands to make an action. Type \"help\" for more.")

# Definitions
def add(item):
    global command_log
    command_log.append(item)

def outprint(secval):
    global index
    print(command_log[index + secval])
    index += secval + 1

def checkcolon(text):
    i = 0
    while not text[i] == ":":
        i += 1
    return i

# Main code
while run:
    command = input("")

    if command == commands_list[0]:# help
        print("Here is the list of all commands", commands_list)

    elif command == commands_list[1]:# end
        run = False

    elif command == commands_list[2]: # run
        while not index == len(command_log):
            if command_log[index] == "print":
                outprint(1)

        # Reseting the commander code
        command_log.clear()
        index = 0

    elif command[:5] == commands_list[3]:# print
        add("print")
        add(command[6:])

    elif command[:3] == commands_list[4]:# var
        if command == "var":
            print(variables)

        else:
            colon_number = checkcolon(command) + 2

            temp = command[colon_number:]
            command = command[:colon_number]
            command = command.replace(" ", "")
            command += temp  

            colon_number = checkcolon(command)
            variables.update({command[3:colon_number]: command[colon_number + 1:]})
    else:
        print("Invalid command")
