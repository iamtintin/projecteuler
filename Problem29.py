lowera = 2
uppera = 100

lowerb = 2
upperb = 100

exponentials = []
for a in range(lowera, uppera+1):
    for b in range(lowerb, upperb+1):
        exponentials.append(a**b)

exponentials = list(set(exponentials))

print(len(exponentials))