#space detection
input = "nihal nihal nihal"
index = 0
def detect_space(string):
    global index
    while not index == len(string):
        if string[index] == " ":
            print(index)
            print("Space detected!!!!")
        index += 1

print(input)
detect_space(input)