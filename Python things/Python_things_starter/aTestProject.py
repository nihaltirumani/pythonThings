# This is "a test project".
import math
column = 6
innerSpaceIndex = 0
spaceIndex = 0

def spacex():
    global column, spaceIndex, innerSpaceIndex
    if spaceIndex < math.floor(column / 2):
        innerSpaceIndex += 1
        spaceIndex += 1
        print(spaceIndex)
    if innerSpaceIndex == math.floor(column / 2):
        spaceIndex += 1
        innerSpaceIndex += 1
    if math.floor(column / 2) < innerSpaceIndex:
        print(spaceIndex)
        spaceIndex -= 1
for i in range(math.floor(column / 2)):            
    pass

