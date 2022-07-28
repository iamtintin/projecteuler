def shift(number):
    return [number[-1]] + number[:-1]

def toNumber(numList):
    strList = [str(x) for x in numList]
    strList = int("".join(strList))
    return strList

def rotate(num):
    originalNum = num
    rotations = []
    numList = [int(x) for x in str(num)]
    for i in range(len(numList)-1):
        numList = shift(numList)
        rotations.append(toNumber(numList))
    return rotations

def checkIfPrime(num):
    prime = True
    if num > 1:
        upperValue = int(num ** 0.5) + 1
        for i in range(2,upperValue):
            if num % i == 0:
                prime = False
    else:
        prime = False
    return prime

def createPrimeList(num):
    primeNumbers = []
    lastNumber = 0
    count = 2

    while True:
        if count > num:
            break
        if checkIfPrime(count):
            primeNumbers.append(count)
        count += 1
        print(len(primeNumbers))

    return primeNumbers

primeNumbers = createPrimeList(1000000)

circularPrimes = []

for primeNum in primeNumbers:
    if primeNum < 10:
        circularPrimes.append(primeNum)
    else:
        rotations = rotate(primeNum)
        circular = True
        for rotation in rotations:
            if not checkIfPrime(rotation):
                circular = False
        if circular:
            circularPrimes.append(primeNum)
    
print(len(circularPrimes))