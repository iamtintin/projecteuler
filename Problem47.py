def findPrimeFactors(num):
    primeFactors = []
    quotient = 2

    while num > 1:
        while num % quotient == 0:
            primeFactors.append(quotient)
            num = num / quotient
        quotient = quotient + 1

    return primeFactors

counter = 100
while True:
    print("Counter value:", counter)
    primes1 = set(findPrimeFactors(counter))
    primes2 = set(findPrimeFactors(counter+1))
    primes3 = set(findPrimeFactors(counter+2))
    primes4 = set(findPrimeFactors(counter+3))

    if len(primes1) < 4:
        counter += 1
        continue
    elif len(primes2) < 4:
        counter += 1
        continue
    elif len(primes3) < 4:
        counter += 1
        continue
    elif len(primes4) < 4:
        counter += 1
        continue

    allPrimes = primes1|primes2|primes3|primes4
    uniquePrimes1 = allPrimes - primes2|primes3|primes4
    uniquePrimes2 = allPrimes - primes1|primes3|primes4
    uniquePrimes3 = allPrimes - primes1|primes2|primes4
    uniquePrimes4 = allPrimes - primes1|primes2|primes3
    if len(uniquePrimes1) >= 4 and len(uniquePrimes2) >= 4 and len(uniquePrimes3) >= 4 and len(uniquePrimes4) >= 4:
        print(counter)
        break

    counter += 1

