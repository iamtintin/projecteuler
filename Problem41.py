import itertools as it

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

panPrimes = []

for noOfDigits in range(2, 9):
    digits = [int(x) for x in range(1, noOfDigits+1)] 
    orders = list(it.permutations(digits))
    for order in orders:
        number = list(order)
        number = [str(x) for x in number]
        number = int("".join(number))
        if checkIfPrime(number):
            panPrimes.append(number)

print(max(panPrimes))