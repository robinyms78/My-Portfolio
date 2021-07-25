L1 = [2,3,4]

# Make a copy of L1(or list(L1), copy.copy(L1), etc)
L2 = L1[:]
L1[0] = 24
print(L1)

# L2 is not changed
print(L2)

