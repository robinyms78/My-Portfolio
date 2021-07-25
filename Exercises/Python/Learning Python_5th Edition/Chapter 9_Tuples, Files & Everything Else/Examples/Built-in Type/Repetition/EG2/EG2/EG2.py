L = [4, 5, 6]

# Embed a (shared) copy of L
Y = [list(L)] * 4
L[1] = 0
print(Y)

# App four copies are still the same
Y[0][1] = 99
print(Y)

