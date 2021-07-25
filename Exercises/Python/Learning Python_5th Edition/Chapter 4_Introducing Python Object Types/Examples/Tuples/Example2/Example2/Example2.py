# Tuples are immutable
T = (1, 2, 3, 4)

#T[0] = 2

# Make a new tuple for a new value
T = (2,) + T[1:]
print(T)