value1 = 1
value2 = 2
counter = 4

while True:
    value = value1 + value2
    value1 = value2
    value2 = value
    if len(str(value2)) == 1000:
        break
    counter += 1

print(counter)