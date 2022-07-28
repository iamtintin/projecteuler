def sumOfSquares(start, finish):
    total = 0
    for i in range(start, finish+1):
        total += (i*i)
    return total

def squareOfSum(start, finish):
    total = 0
    for i in range(start, finish+1):
        total += i
    return total*total

def differenceOfSquares(start, finish):
    sumOf = sumOfSquares(start, finish)
    squareOf = squareOfSum(start, finish)
    return abs(sumOf-squareOf)
    
print(differenceOfSquares(1,100))