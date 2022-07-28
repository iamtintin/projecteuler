import math

max = 2540160
factorialDigits = []

for num in range(10, max+1):
    numList = [int(x) for x in str(num)]
    total = 0
    for digit in numList:
        total += math.factorial(digit)
    if total == num:
        factorialDigits.append(num)

print(factorialDigits)
print(len(factorialDigits))
print(sum(factorialDigits))