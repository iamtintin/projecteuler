
upperLimit = 354294
# Upper Limit calculated by finding the number of digits, 
# where the max. sum of the digits to the power of 5, 
# is less than the max number with that many number of digits

validValues = []

for x in range(10, upperLimit):
    number = str(x)
    total = 0

    for num in number:
        subTotal = int(num) ** 5
        total += subTotal
    
    if total == x:
        validValues.append(x)

print(sum(validValues))
