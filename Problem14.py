def createCollatzSequence(start):
    num = start
    sequence = [start]

    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
            sequence.append(num)
        else:
            num = int((3 * num) + 1)
            sequence.append(num)

    return len(sequence)

lengths = []
for i in range(2, 1000000):
    lengths.append(createCollatzSequence(i))

print(lengths.index(max(lengths))+2)