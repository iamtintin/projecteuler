solutions = []
for p in range (10,1001):
    sideLengths = []
    for side1 in range(1, int(p/2)):
        for side2 in range(1, p):
            side3 = (((side1**2) + (side2**2))**0.5)
            if side3.is_integer():
                side3 = int(side3)
                if side1 + side2 + side3 == p:
                    sides = [side1, side2, side3]
                    sides.sort()
                    if sides not in sideLengths:
                        sideLengths.append(sides)

    print(p)
    solutions.append(len(sideLengths))

maxValue = max(solutions)
maxIndex = solutions.index(maxValue) + 10
print(maxValue, maxIndex)
