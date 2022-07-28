import math

def sumOfFactors(n):
    factorList = []
    i = 1
    while i <= math.sqrt(n):
        if(n%i==0):
            if(n%i==i):
                factorList.append(i)
            else:
                factorList.append(i)
                factorList.append(int(n/i))
        i += 1
    factorList.remove(n)
    return sum(factorList)

numbers = list(range(1,10000))
total = 0

for number in numbers:

    sum1 = sumOfFactors(number)
    sum2 = sumOfFactors(sum1)

    if sum2 == number and sum1 != number:
        if sum1 > 10000:
            print("Problem")

        total = total + number + sum1
        numbers.remove(number)
        numbers.remove(sum1)

print(total)