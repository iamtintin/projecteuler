with open("Problem8.txt") as txtFile:
    lines = txtFile.readlines()

line = lines[0].strip("\n")
line = [int(x) for x in line]

adjacent = 13
totals = []

for i in range(0, len(line)-adjacent+1):
    total = 1
    for x in range(0, adjacent):
        total = total * line[i+x]
    totals.append(total)

print(max(totals))
