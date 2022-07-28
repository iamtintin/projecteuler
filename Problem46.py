def isOddComposite(n):
    if n <= 3:
        return False
    
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return True

    i = 5
    while (i ** 2) <= n:
        if n % i == 0 or n % (i+2) == 0:
            return True
        i += 6
    return False

def createOddCompositeList(n):
    oddComposites = []
    counter = 2
    while len(oddComposites) < n:
        num = (counter * 2) + 1
        if isOddComposite(num):
            oddComposites.append(num)
        counter += 1
    return oddComposites


def createSquareList(n):
    squareList = []
    for i in range(1, n+1):
        squareList.append(i**2)
    return squareList


def SieveOfEratosthenes(n): 
    primeNumbers = []
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    for p in range(2, n): 
        if prime[p]: 
            primeNumbers.append(p)
    return primeNumbers

primeNums = SieveOfEratosthenes(1000000)
squareNums = createSquareList(4000)
compositeNums = createOddCompositeList(4000)

allNumbers = []

for oddComposite in compositeNums:
    possible = False
    for prime in primeNums:
        if prime + 1 > oddComposite:
            break
        for square in squareNums:
            if prime + square > oddComposite:
                break
            temp = prime + (2 * square)
            if temp == oddComposite:
                possible = True
                #print(prime, "+ 2 x", square, "=", oddComposite)
                break
        if possible:
            break
    if not possible:
        print(oddComposite)
        break
