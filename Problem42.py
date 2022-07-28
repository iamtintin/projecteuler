alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def discriminant(a, b, c):
    value = (b ** 2) - (4 * a * c)
    if value >= 0:
        return value
    else:
        return None

def solvePositiveQuadratic(a, b, c):
    discValue = discriminant(a, b, c)
    top = (-b) + ((discValue)**0.5)
    btm = 2 * a
    value = top/btm
    return value

with open("Problem42.txt") as txtFile:
    lines = txtFile.readlines()[0].strip("\n").split(",")

for i in range(len(lines)):
    lines[i] = lines[i][1:-1]

triangleWords = []

for word in lines:
    value = 0
    for character in word:
        
        value += (alphabet.index(character.lower()) + 1)
    n = solvePositiveQuadratic(1, 1, (-2 * value))
    if n.is_integer():
        triangleWords.append(word)

print(len(triangleWords))
    
