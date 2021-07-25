L = [1, 2, 3]

# Embed a reference to L
M = ["X", L, "Y"]
print(M)

L[1] = 0

# Changes M too
print(M)

