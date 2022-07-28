def createDigits(numDigits, copyOfDigits):
    combos = []
    for x in range(len(copyOfDigits)):
        firstDigit = copyOfDigits[x]
        temp = copyOfDigits.copy()
        temp.remove(firstDigit)
        if numDigits > 1:
            restOfNumber = createDigits(numDigits - 1, temp)
        else:
            restOfNumber = [""]
        for y in range(len(restOfNumber)):
            number = str(firstDigit) + str(restOfNumber[y])
            combos.append(number)

    return combos

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

factors = createDigits(5, digits)

validCombos = [[2, 3], [1, 4]]

pandigitalProducts = []

for a in range(len(validCombos)):
    for i in range(len(factors)):
        factorList = list(map(int, list(factors[i])))
        difference = list(set(digits) - set(factorList))
        firstNum = int(factors[i][:validCombos[a][0]])
        secondNum = int(factors[i][validCombos[a][0]:])
        product = firstNum * secondNum
        productDigits = [int(x) for x in str(product)]
        productDigits.sort()
        difference.sort()
        if productDigits == difference and product not in pandigitalProducts:
            pandigitalProducts.append(product)

print(sum(pandigitalProducts))

            
            
