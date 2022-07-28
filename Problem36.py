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

def denary_binary(x):
        x = int(x)
        binary = ''
        while x > 0:
            rem = x % 2
            binary += str(rem)
            x = x//2
        return binary[::-1]

palindromeDoubles = []


for num in range(1,1000000):
    if isPalindrome(num):
        binaryNum = int(denary_binary(num))
        if isPalindrome(binaryNum):
            palindromeDoubles.append(num)

print(sum(palindromeDoubles))
