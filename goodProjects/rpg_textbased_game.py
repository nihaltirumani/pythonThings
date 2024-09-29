grid = []
length = 5
width = 8

class gameobject():
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
        self.oldx = x
        self.oldy = y

    def setpos(self, setx, sety):
        self.oldx = self.x
        self.oldy = self.y
        self.x = setx
        self.y = sety

    def draw(self):
        grid.pop((width * (self.oldy)) + (self.oldx % width))
        grid.insert(abs(((width * (self.oldy)) + (self.oldx % width))), " ")

        grid.pop((width * (self.y)) + (self.x % width))
        grid.insert(abs(((width * (self.y)) + (self.x % width))), self.char)

def createlevel():
    for i in range(length * width):
        grid.append(" ")

def drawscreen():
    drawline = ""
    for j in range(length):
        for i in range(1, width + 1):
            drawline += grid[(width * j) + i - 1]
        print(drawline)
        drawline = ""

def secreen():
    player.draw()
    drawscreen()

# creating level
createlevel()

# game objects
player = gameobject(0, 0, "0")

# main loop
while True:
    secreen()

    key = input("")[0]

    if key == "d":
        player.setpos(player.x + 1, player.y)
    elif key == "a":
        player.setpos(player.x - 1, player.y)
    elif key == "w":
        player.setpos(player.x, player.y - 1)
    elif key == "s":
        player.setpos(player.x, player.y + 1)
    else:
        quit()

    print(f"x: {player.x} y: {player.y}")