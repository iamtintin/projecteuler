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

primeNums = SieveOfEratosthenes(1000000)

counter = 0
total = 0
while total < 1000000:
    total += primeNums[counter]
    counter += 1

validPrimeSum = []

for i in range(counter+1, 1, -1):
    for x in range(0, i-1):
        subList = primeNums[x:i]
        if len(subList) < 480:
            break
        total = sum(subList)
        if checkIfPrime(total) and total < 1000000:
            validPrimeSum.append([total, abs(x-i)])
            found = True

numbers = [x[1] for x in validPrimeSum]
maxNumber = max(numbers)
maxValues = validPrimeSum[numbers.index(maxNumber)][0]
print(maxValues)

