validFraction = []

def hcf(num1, num2):
        while num2 != 0:
            temp = num2
            num2 = num1%num2
            num1 = temp
        return num1
    
def simplify(num, den):
    greatest = hcf(num, den)
    num = num / greatest
    den = den / greatest
    return num, den

for denr in range(11, 100):
    for numr in range(10, denr):
        denrList = [int(x) for x in str(denr)]
        numrList = [int(x) for x in str(numr)]
        common = list(set(numrList) & set(denrList))
        notDistinct = len(denrList) != len(set(denrList)) or len(numrList) != len(set(numrList))
        if len(common) == 1 and not notDistinct and common[0] != 0:
            fraction = numr/denr
            newNumr = list(set(numrList) - set(common))[0]
            newDenr = list(set(denrList) - set(common))[0]
            if newNumr == 0 or newDenr == 0:
                continue
            cancelledFraction = newNumr/newDenr
            if cancelledFraction == fraction:
                validFraction.append([numr, denr])

denom = [x[1] for x in validFraction]
numor = [x[0] for x in validFraction]

denProduct = 1
numProduct = 1

for fraction in validFraction:
    denProduct*=fraction[1]
    numProduct*=fraction[0]

print(simplify(numProduct, denProduct))

