def checkIfPrime(num):
    prime = True
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                prime = False
    else:
        prime = False
    return prime

def createPrimeList(a, b):
    sequence = []
    while True:
        n = len(sequence)
        nTerm = (n**2) + (a*n) + b
        if checkIfPrime(nTerm):
            sequence.append(nTerm)
        else:
            break
    return len(sequence)

totalMaxValue = 0
totalMaxA = 0
totalMaxB = 0

for a in range(1, 1000, 2):
    print("a value:", a)
    for b in range(1, 1001, 2):
        values = []

        absA = a
        absB = b

        values.append(createPrimeList(absA, absB))
        values.append(createPrimeList(absA, -absB))
        values.append(createPrimeList(-absA, absB))
        values.append(createPrimeList(-absA, -absB))

        maxValue = max(values)
        maxIndex = values.index(maxValue)

        if maxValue > totalMaxValue:
            totalMaxValue = maxValue
            if maxIndex == 0:
                totalMaxA = absA
                totalMaxB = absB
            elif maxIndex == 1:
                totalMaxA = absA
                totalMaxB = -absB
            elif maxIndex == 2:
                totalMaxA = -absA
                totalMaxB = absB
            elif maxIndex == 3:
                totalMaxA = -absA
                totalMaxB = -absB            

print(totalMaxValue)
print(totalMaxA)
print(totalMaxB)
print(totalMaxA * totalMaxB)