L = [1, 2, 3]

# Embed a copy of L (or list(L), or L.copy())
# Changes only L, not M
M = ["X", L[:], "Y"]
L[1] = 0
print(L)
print(M)



