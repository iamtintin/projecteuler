def checkIfPrime(num):
    prime = True
    if num > 1:
        upper = int((num ** 0.5) + 1)
        for i in range(2,upper):
            if num % i == 0:
                prime = False
    else:
        prime = False
    return prime

def checkIfTruncPrime(num):
    num = str(num)
    allPrimes = True
    for i in range(1, len(num)):
        if not checkIfPrime(int(num[:i])):
            return False

    for i in range(len(num)-1, 0, -1):
        if not checkIfPrime(int(num[i:])):
            return False
    return True

truncPrimes = []
counter = 10
while len(truncPrimes) != 11:
    if checkIfPrime(counter % 10) and checkIfPrime(int(str(counter)[:1])):
        if checkIfPrime(counter):
            if checkIfTruncPrime(counter):
                truncPrimes.append(counter)

    counter += 1

print(truncPrimes)
print(sum(truncPrimes))