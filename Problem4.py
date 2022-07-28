def isPalindrome(num):
    num = [int(x) for x in str(num)]
    palindrome = True

    if len(num) % 2 == 0:
        limit = int(len(num)/2)
    else:
        limit = int((len(num)-1)/2)

    for i in range(0,limit):
        if num[i] != num[len(num)-1-i]:
            palindrome = False
    return palindrome

palindromes = []

for i in range(100, 1000):
    for x in range(100, 1000):
        if isPalindrome(i*x):
            palindromes.append(i*x)

print(max(palindromes))
