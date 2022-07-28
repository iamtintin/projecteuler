def discriminant(a, b, c):
    value = (b ** 2) - (4 * a * c)
    if value >= 0:
        return value
    else:
        return None

def solvePositiveQuadratic(a, b, c):
    discValue = discriminant(a, b, c)
    top = (-b) + ((discValue)**0.5)
    btm = 2 * a
    value = top/btm
    return value

def isShapeNum(num, sides):
    if sides == 3:
        a = 1
        b = 1
        tM = -2
    elif sides == 5:
        a = 3
        b = -1
        tM = -2
    elif sides == 6:
        a = 2
        b = -1
        tM = -1
    else:
        print("Mode Error")
        return None

    if discriminant(a, b, (tM*num)):
        tempN = solvePositiveQuadratic(a, b, (tM*num))
        if tempN.is_integer():
            return True
        else:
            return False
    return False

n = 286
while True:
    triN = (n * (n + 1)) / 2
    if isShapeNum(triN, 5):
        if isShapeNum(triN, 6):
            print(int(triN))
            break
    n += 1