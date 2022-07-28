with open("Problem13.txt") as txtFile:
    lines = txtFile.readlines()

numbers = []

for i in range(0, len(lines)):
    lines[i] = lines[i].strip("\n")
    numbers.append(int(lines[i]))

total = sum(numbers)

trunc = str(total)[:10]
print(trunc)