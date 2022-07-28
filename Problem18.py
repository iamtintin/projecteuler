def findMaxTotals(triangle, x, y):
    total = triangle[x][y]
    if x != len(triangle) - 1:
        subtotal1 = findMaxTotals(triangle, x+1, y)
        subtotal2 = findMaxTotals(triangle, x+1, y+1)
        total += max(subtotal1, subtotal2)
    return total
   

with open("Problem18.txt") as txtFile:
    lines = txtFile.readlines()

for x in range(0, len(lines)):
    lines[x] = lines[x].strip("\n").split(" ")
    for y in range(0, len(lines[x])):
        lines[x][y] = int(lines[x][y])

totals = findMaxTotals(lines, 0, 0)
print(totals)