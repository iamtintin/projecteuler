digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 9
panNums = []

while True:
    if str(num)[0] != "9":
        if len(str(num)) < 5:
            num = 9 * (10 ** (len(str(num))- 1))
        else:
            break
    concatPanNum = ""
    multiplier = 1
    while len(concatPanNum) < 9:
        concatPanNum += str(num * multiplier)
        multiplier += 1
    if len(concatPanNum) == 9:
        numList = [int(x) for x in concatPanNum]
        numList.sort()
        if numList == digits:
            panNums.append(int(concatPanNum))
    num += 1

print(panNums)
print(max(panNums))
        