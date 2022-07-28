def recurringDecimal(numr, denr):
    res = ""
    remainders = {}
    rem = numr % denr

    while (rem != 0) and (rem not in remainders):
        remainders[rem] = len(res)
        rem *= 10
        res += str(rem//denr)
        rem = rem % denr

    if rem == 0:
        res = "a"
    else:
        res = res[remainders[rem]:]

    return res

maxValue = 0
maxIndex = 0

for i in range(1,1000):
    value = recurringDecimal(1,i)
    if len(value) > maxValue:
        maxIndex = i
        maxValue = len(value)

print(maxIndex)
