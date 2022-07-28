def findMaxPrimeFactor(num):
    primeFactors = []
    quotient = 2

    while num > 1:
        while num % quotient == 0:
            primeFactors.append(quotient)
            num = num / quotient
        quotient = quotient + 1

    return max(primeFactors)

print(findMaxPrimeFactor(600851475143))