def addNumFrac(num, numer, denom):
    return numer + (num*denom), denom

count = 0

numer = 1
denom = 2

for i in range(999): 
    numer, denom = addNumFrac(2, numer, denom)

    buffer = denom
    denom = numer
    numer = buffer

    tempNumer, tempDenom = addNumFrac(1, numer, denom)
    print(str(i+2) + ":", tempNumer, tempDenom)
    if len(str(tempNumer)) > len(str(tempDenom)):
        count += 1

print(count)


