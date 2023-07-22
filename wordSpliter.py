index = 0

def split(string):
    global index
    while index != len(string):
        print(string[index])
        index += 1

split("Hi! My name is nihal.")
