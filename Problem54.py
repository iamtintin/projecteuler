allCards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def checkRoyalFlush(cards):
    royalFlush = ['T', 'J', 'Q', 'K', 'A']
    values = [x[0] for x in cards]
    if sorted(values) == royalFlush:
        return True
    else:
        return False

def checkConsecutiveValues(cards):
    values = [x[0] for x in cards]
    indices = [allCards.index(x) for x in values]
    small = min(indices)
    for i in range(len(indices)):
        indices[i] -= small
    if sorted(indices) == list(range(5)):
        return True
    else:
        return False

def countValues(cards):
    values = [x[0] for x in cards]
    distinct = list(set(values))
    valueDict = {
        "1": [],
        "2": [],
        "3": [],
        "4": []
    }
    for value in distinct:
        count = values.count(value)
        valueDict[str(count)].append(value)
    return valueDict


def checkSameSuit(cards):
    suits = [x[1] for x in cards]
    if all(x == suits[0] for x in suits):
        return True
    else:
        return False

def decideRank(cards):
    if checkSameSuit(cards):
        if checkRoyalFlush(cards):
            return 10, "0"
        elif checkConsecutiveValues(cards):
            return 9, ["0"]
        else:
            return 6, ["0"]
    else:
        if checkConsecutiveValues(cards):
            return 5, ["0"]
        else:
            valueDict = countValues(cards)
            if len(valueDict["4"]) != 0:
                return 8, valueDict["4"]
            elif len(valueDict["3"]) == 1 and len(valueDict["2"]) == 1:
                return 7, valueDict["3"]
            elif len(valueDict["3"]) == 1:
                return 4, valueDict["3"]
            elif len(valueDict["2"]) == 2:
                return 3, valueDict["3"]
            elif len(valueDict["2"]) == 1:
                return 2, valueDict["2"]
            else:
                return 1, ["0"]

def decideWin(rank1, rankValues1, card1, rank2, rankValues2, card2):
    if rank1 > rank2:
         return True
    elif rank1 == rank2:
        if rankValue1[0] != "0":
            rankValues1 = sorted([allCards.index(x) for x in rankValues1], reverse=True)
            rankValues2 = sorted([allCards.index(x) for x in rankValues2], reverse=True)
            for i in range(len(rankValues1)):
                if rankValues1[i] > rankValues2[i]:
                    return True
                elif rankValues1[i] < rankValues2[i]:
                    return False
        card1 = sorted([allCards.index(x[0]) for x in card1], reverse=True)
        card2 = sorted([allCards.index(x[0]) for x in card2], reverse=True)
        for i in range(len(card1)):
            if card1[i] > card2[i]:
                return True
            elif card1[i] < card2[i]:
                return False
    else:
         return False

counter = 0

with open("Problem54.txt") as txtFile:
    cardtxt = txtFile.readlines()

for i in range(len(cardtxt)):
    cards = [list(x) for x in cardtxt[i].strip("\n").split(" ")]

    card1 = cards[:5]
    card2 = cards[5:]

    rank1, rankValue1 = decideRank(card1)
    rank2, rankValue2 = decideRank(card2)

    if decideWin(rank1, rankValue1, card1, rank2, rankValue2, card2):
        counter += 1

print(counter)