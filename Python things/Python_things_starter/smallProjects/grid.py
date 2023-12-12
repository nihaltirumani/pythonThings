grid = []
row = ""
i1 = 0
index = -1

def generate():
    for i in range(10):
        for i1 in range(10): #i*io = 100
            grid.append(i)

def seperate():
    global row, index
    for i in range(10):
        for i1 in range(10):
            row += str(grid[i1 + index])
        print(row)
        row = ""
        index += 10

generate()
print(grid)
seperate()


#####FALURE:C