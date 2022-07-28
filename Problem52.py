def isPermutedMultiple(num, x):
    newNum = num * x
    num = [int(x) for x in str(num)]
    newNum = [int(x) for x in str(newNum)]

    if len(num) != len(newNum):
        return False
    else:
        if sorted(num) == sorted(newNum):
            return True
        else:
            return False

num = 1
while True:
    found = False

    for i in range(2, 7):
        if isPermutedMultiple(num, i):
            found = True
        else:
            found = False
            break

    if found:
        print(num)
        break

    num += 1 
