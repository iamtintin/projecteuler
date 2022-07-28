ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

hundred = "hundred"

thousand = "thousand"

exceptions = [11, 12, 13, 14, 15, 16, 17, 18, 19]
exceptionsWords = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

total = 0

for i in range(1, 1001):
    letters = 0
    thousandths = str(i)[-4:-3]
    hundredths = str(i)[-3:-2]
    tenths = str(i)[-2:-1]
    units = str(i)[-1:]

    if tenths == '':
        tenths = "0"
    if hundredths == '':
        hundredths = "0"
    if thousandths == '':
        thousandths = "0"

    if int(tenths+units) in exceptions:
        temLetters = len(exceptionsWords[exceptions.index(int(tenths+units))])
        letters += temLetters
    else:
        temLetters = len(tens[int(tenths)]) + len(ones[int(units)])
        letters += temLetters

    if hundredths != "0":
        temLetters = len(ones[int(hundredths)]) + len(hundred)
        if i % 100 != 0:
            temLetters += len("and")
        letters += temLetters
    
    if thousandths != "0":
        temLetters = len("onethousand")
        letters += temLetters
    
    print(i, letters)
    total += letters

print(total)