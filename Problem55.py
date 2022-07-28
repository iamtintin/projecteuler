def isPalindrome(num):
    num = str(num)
    return num == num[::-1]

counter = 0

for i in range(1, 10000):
    found = False
    num = i
    iteration = 1
    while iteration < 90:
        reverse = int(str(num)[::-1])
        total = reverse + num
        if isPalindrome(total):
            found = True
            break
        else:
            num = total
        iteration += 1
    if not found:
        counter += 1
    print(str(i) + ": Completed")

print(counter)