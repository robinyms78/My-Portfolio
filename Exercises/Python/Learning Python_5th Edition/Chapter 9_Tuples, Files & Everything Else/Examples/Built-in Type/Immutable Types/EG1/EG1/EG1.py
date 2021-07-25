T = (1, 2, 3)

# Error!
# T[2] = 4

# OK: (1, 2, 4)
T = T[:2] + (4,)
print(T)

