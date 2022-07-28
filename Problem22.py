def findValue(name):
    total = 0
    for character in str(name):
        subTotal = alphabet.index(character.lower()) + 1
        total += subTotal
    return total

with open("Problem22.txt") as txtFile:
    lines = txtFile.readlines()

lines = lines[0].split(",")

for i in range(0, len(lines)):
    lines[i] = lines[i].strip("\"")

lines.sort()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

total = 0

for i in range(0, len(lines)):
    subTotal = findValue(lines[i])
    subTotal = subTotal * (i+1)
    total += subTotal

print(total)
