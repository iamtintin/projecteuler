import itertools as it

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

def replaceDigits(num, index, replacement):
    num = [int(x) for x in str(num)] 
    for pos in index:
        num[pos] = replacement
    num = int(''.join(map(str,num)))
    return num

def findOccurrences(string, char):
    return [i for i, letter in enumerate(string) if letter == char]

primeNums = SieveOfEratosthenes(1000000)

for i in range(len(primeNums)):
    if primeNums[i] > 10000:
        primeNums = primeNums[i:]
        break

for i in range(len(primeNums)):
    numberFound = False
    prime = primeNums[i]
    print(prime)

    digitCount = {}
    for num in str(prime):
        if num in digitCount:
            digitCount[num] += 1
        else:
            digitCount[num] = 1

    repeatedDigits = []
    for digit in digitCount:
        if digitCount[digit] > 1:
            repeatedDigits.append(digit)

    for digit in repeatedDigits:
        indices = findOccurrences(str(prime), digit)

        for x in range(2, len(indices)+1):
            combos = it.combinations(indices, x)

            for combo in combos:
                primeSuccess = []

                for num in range(0, 10):
                    currentPrime = replaceDigits(prime, combo, num)

                    if checkIfPrime(currentPrime):
                        primeSuccess.append(currentPrime)

                print("Count:", str(primeSuccess))

                if len(primeSuccess) == 8:
                    numberFound = True
                    print("Success!!!!", str(prime))
                    break
                else:
                    for num in primeSuccess:
                        if num in primeNums:
                            primeNums.remove(num)

            if numberFound:
                break  
        if numberFound:
            break   
    if numberFound:
        break       
