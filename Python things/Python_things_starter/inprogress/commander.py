# Welcoming the user
print("Welcome to commander. Type commands to make an action. Type \"help\" for more.")

# Varibles
run = True
index = 0
commands_list = ["help", "end", "run", "print",]
command_log = []

# Definitions
def add(item):
    command_log.append(item)
def outprint(secval):
    global index
    print(command_log[index + secval])
    index += secval + 1

# Main code
while run:
    command = input("")
    if command in commands_list:
        if command == commands_list[0]:#help
            print("Here is the list of all commands", commands_list)
        elif command == commands_list[1]:#end
            run = False
        elif command == commands_list[3]:#print
            add("print")
            command = input("input: ")
            add(command)
        #"run" command operation
        elif command == commands_list[2]:
            while not index == len(command_log):
                if command_log[index] == "print":
                    outprint(1)
                    
            command_log.clear()
            index = 0

    else:
        print("Invalid command")
    

#inprogress. needed to be worked.
