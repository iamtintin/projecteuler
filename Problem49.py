import itertools as it

def checkIfPrime(num):
    if num > 1:
        upperValue = int(num ** 0.5) + 1
        for i in range(2,upperValue):
            if num % i == 0:
                return False
    else:
        return False
    return True

primes = []

for i in range(1000, 10000):
    if checkIfPrime(i):
        perms = list(it.permutations([int(x) for x in str(i)]))
        primePerms = []
        completedPerms = []

        for order in perms:
            num = int("".join([str(x) for x in order]))
            if num < 1000 or num in completedPerms:
                continue
            completedPerms.append(num)
            if checkIfPrime(num):
                primePerms.append(num)

        if len(primePerms) >= 3:
            differences = []
            for x in range(len(primePerms)):
                for y in range(x+1, len(primePerms)):
                    temp = primePerms.copy()
                    temp.remove(primePerms[x])
                    temp.remove(primePerms[y])
                    difference = abs(primePerms[x] - primePerms[y])
                    for z in range(len(temp)):
                        difference1 = abs(primePerms[x] - temp[z])
                        difference2 = abs(primePerms[y] - temp[z])
                        if difference1 == difference or difference2 == difference:
                            series = [primePerms[x], primePerms[y], temp[z]]
                            series.sort()
                            if series not in primes:
                                primes.append(series)
                    differences.append(difference)

for prime in primes:
    print("".join([str(x) for x in prime]))

