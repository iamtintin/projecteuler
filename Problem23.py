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
    factorList = list(set(factorList))
    factorList.remove(n)
    return sum(factorList)

abundantNumbers = []

for i in range(1, 28124):
    if sumOfFactors(i) > i:
        abundantNumbers.append(i)

print("Found abundant numbers")
#print(abundantNumbers)

abundantSums = []

for number in abundantNumbers:
    for other in abundantNumbers:
        sums = other + number
        abundantSums.append(sums)

print("Found abundant sums")

abundantSums = list(set(abundantSums))

unique = []

allNumbers = list(range(1, 28124))
unique = set(allNumbers) - set(abundantSums)
unique = list(unique)
unique.sort()

print(sum(unique))
