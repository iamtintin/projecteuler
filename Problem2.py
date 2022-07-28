total = 0

sequence = [1, 2]

while True:
    value = sequence[len(sequence)-1] + sequence[len(sequence)-2]
    sequence.append(value)
    temp = sequence[len(sequence)-1]
    if temp >= 4000000:
        break

print(sequence)

for i in sequence:
    if i % 2 == 0:
        total += i

print(total)