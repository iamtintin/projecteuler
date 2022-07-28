import itertools

theList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

perms = itertools.permutations(theList)

perms = list(perms)

value = list(perms[999999])

value = "".join(str(x) for x in value)

print(value)