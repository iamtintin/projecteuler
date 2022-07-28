import math

size = 20

permutations = math.factorial(size * 2)
uniquePaths = permutations / ((math.factorial(size)) ** 2)

print(int(uniquePaths))