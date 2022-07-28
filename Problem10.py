def checkIfPrime(num):
    prime = True
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                prime = False
    else:
        prime = False
    return prime

def createPrimeList(num):
    primeNumbers = []
    count = 2
    lastDigit = 0

    while lastDigit <= num:
        prime = checkIfPrime(count)
        if prime:
            primeNumbers.append(count)
            print(lastDigit)
        count += 1
        lastDigit = primeNumbers[len(primeNumbers)-1]
    return primeNumbers[:-1]

primeList = createPrimeList(2000000)
 
total = 0
for i in primeList:
    total += i

print(total)