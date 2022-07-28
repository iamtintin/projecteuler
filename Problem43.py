import itertools as it

primeNums = [2, 3, 5, 7, 11, 13, 17]

def checkSubDivise(num, primes):
    num = str(num)
    for i in range (1, 8):
        subNum = int(num[i:i+3])
        primeNum = primes[i-1]
        if subNum % primeNum != 0:
            return False
    return True

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

panNumList = list(it.permutations(digits))

panNums = []

for panNum in panNumList:
    pNum = list(panNum)
    if pNum[0] == 0:
        continue
    num = "".join([str(x) for x in pNum])
    if checkSubDivise(num, primeNums):
        panNums.append(int(num))

print(panNums)
print(sum(panNums))
