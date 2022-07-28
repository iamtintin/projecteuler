total = 0
end = 1000

for i in range(1, end+1):
    total += (i ** i)

print(str(total)[-10:])
