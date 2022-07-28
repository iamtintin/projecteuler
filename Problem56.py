buffer = 0

for a in range(2,100):
    for b in range(90, 100):
        num = (a ** b)
        num = [int(x) for x in str(num)]
        total = sum(num)
        if total > buffer:
            buffer = total
        print("Checking:", a, b)

print(buffer)
