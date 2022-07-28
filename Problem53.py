import math

def factorial(upper, lower):
    buffer = 1
    for i in range(lower, upper+1):
        buffer = buffer * i
    return buffer

count = 0
for n in range(23, 101):
    subCount = 0 
    for r in range(2, math.floor(n/2)+1):
        nCr = factorial(n,r+1) / factorial(n-r, 1)
        if nCr > 1000000:
            subCount += 1
    if n % 2 == 0 and subCount != 0:
        subCount = (subCount * 2) - 1
    else:
        subCount = (subCount * 2)
    count += subCount

print(count)