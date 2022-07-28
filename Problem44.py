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

def isPentagon(num):
    if discriminant(3, -1, (-2*num)):
        tempN = solvePositiveQuadratic(3, -1, (-2*num))
        if tempN.is_integer():
            return True
        else:
            return False
    return False

#Estimated to be within first 5000 terms 

for x in range(1, 5000):
    xNum = (x * ((3 * x) - 1)) / 2 
    for y in range(x+1, 5000):
        yNum = (y * ((3 * y) - 1)) / 2 
        if isPentagon(xNum + yNum) and isPentagon(yNum - xNum):
            print(abs(xNum - yNum))
            break

