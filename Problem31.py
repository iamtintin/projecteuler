desiredValue = 200

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def numberOfCombinations(amount, values, index=0):
    if amount == 0:
        return 1
    elif amount < 0:
        return None
    else:
        subTotal = 0
        for i in range(index, len(values)):
            currentCoin = values[i]
            if amount - currentCoin < currentCoin:
                loopIndex = i + 1
            else:
                loopIndex = i

            subCombo = numberOfCombinations(amount - currentCoin, values, loopIndex)

            if subCombo:
                subTotal += subCombo

        return subTotal

print(numberOfCombinations(desiredValue, coins))