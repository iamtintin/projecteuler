import math
def findFactors(n):
    factorList = []
    i = 1
    while i <= math.sqrt(n):
        if(n%i==0):
            if(n%i==i):
                factorList.append(i)
            else:
                factorList.append(i)
                factorList.append(int(n/i))
        i += 1
    return factorList
        
def createNthTri(n):
    triNum = int((n * (n + 1))/2)
    return triNum

counter = 1
factors = 0
while factors <= 500:
    triNum = createNthTri(counter)
    factorList = findFactors(triNum)
    factors = len(factorList)
    print(triNum, factors)
    counter += 1

print(triNum)
