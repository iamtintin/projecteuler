dimensions = 1001

loop = (dimensions - 1) // 2

diagonals = [1]
addBuffer = 2

for i in range(loop):
    for x in range(4):
        newTerm = diagonals[len(diagonals)-1] + addBuffer
        diagonals.append(newTerm)
    addBuffer += 2

print(sum(diagonals))


