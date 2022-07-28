def isPyTriplet(num1, num2, num3):
    triplet = False
    numList = [num1, num2, num3]
    numList.sort()
    for i in range(0, 3):
        numList[i] = numList[i] * numList[i]
    if numList[0] + numList[1] == numList[2]:
        triplet = True
    return triplet

goal = 1000
valid = []

for a in range(1, goal):
    for b in range(1, 1001-a):
        c = 1000 - a - b
        if c == 0:
            continue
        if isPyTriplet(a, b, c):
            valid.append([a,b,c])

for nums in valid:
    print(nums[0]*nums[1]*nums[2])
