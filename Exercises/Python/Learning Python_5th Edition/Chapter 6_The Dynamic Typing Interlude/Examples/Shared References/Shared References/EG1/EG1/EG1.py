# A mutable object
L1 = [2,3,4]

# Make a reference to the same object
L2 = L1

# An in-place change
L1[0] = 24

# L1 is different
print(L1)

# But so is L2!
print(L2)