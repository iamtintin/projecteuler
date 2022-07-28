def returnAdjacent(file, x, y, consec):
    translations = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    adjacentNumbers = []
    for move in translations:
        tempList = []
        for i in range(consec):
            tempx = x + (i*move[0])
            tempy = y + (i*move[1])
            tempList.append(file[tempx][tempy])
        adjacentNumbers.append(tempList)
    return adjacentNumbers

def product(pList):
    total = 1
    for i in pList:
        total *= i
    return total

with open("Problem11.txt") as txtFile:
    lines = txtFile.readlines()

for i in range(0, len(lines)):
    lines[i] = lines[i].strip("\n").split(" ")
    for x in range(0, len(lines[i])):
        lines[i][x] = int(lines[i][x])


numbers = 4

xstart = numbers - 1
xfinish = len(lines) - numbers + 1
ystart = numbers - 1

adjacentList = []

for x in range(xstart, xfinish):
    for y in range(ystart, len(lines[x])-numbers+1):
        tempList = returnAdjacent(lines, x, y, numbers)
        for bunch in tempList:
            adjacentList.append(product(bunch))

print(max(adjacentList))
        
