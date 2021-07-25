L = [1, 2, 3]
D = {"a": 1, "b": 2}

# Instead of A = L (or list(L))
A = L[:]

# Instead of B = D (ditto for sets)
B = D.copy()
A[1] = "Ni"
B["c"] = "spam"
print(L, D)
print(A, B)



