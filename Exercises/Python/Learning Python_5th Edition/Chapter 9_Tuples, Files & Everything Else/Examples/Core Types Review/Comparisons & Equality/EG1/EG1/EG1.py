# Same value, unique object
L1 = [1, ("a",3)]
L2 = [1, ("a",3)]

# Equivalent? Same object?
print(L1 == L2, L1 is L2)
