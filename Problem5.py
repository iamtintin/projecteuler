def findPrimeFactors(num):
    primeFactors = []
    quotient = 2

    while num > 1:
        while num % quotient == 0:
            primeFactors.append(quotient)
            num = num / quotient
        quotient = quotient + 1
    
    return primeFactors

def createDict(arrayList):
    arrayDict = {}
    for i in arrayList:
        if i in arrayDict:
            arrayDict[i] += 1
        else:
            arrayDict[i] = 1
    return arrayDict

def smallestCumulativeMultiple(start, finish):

    factDictList = []

    for i in range(start, finish+1):
        factors = findPrimeFactors(i)
        factDict = createDict(factors)
        factDictList.append(factDict)

    uniqueFactors = {}

    for i in range(0, len(factDictList)):
        for x in factDictList[i]:
            if x not in uniqueFactors:
                uniqueFactors[x] = 0
    
    for i in range(0, len(factDictList)):
        for x in factDictList[i]:
            if factDictList[i][x] > uniqueFactors[x]:
                uniqueFactors[x] = factDictList[i][x]

    multiple = 1

    for x in uniqueFactors:
        multiple *= (x**uniqueFactors[x])


    return multiple

print(smallestCumulativeMultiple(1, 20))
print(list(range(2, 2)))


