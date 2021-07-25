# Membership
print(3 in [1,2,3])

# Iteration
for x in [1,2,3]:
    print(x, end = " ")

# List comprehension
res = [c * 4 for c in "SPAM"]
print(res)

# List comprehension equivalent
res = []
for c in "SPAM":
    res.append(c * 4)
print(res)

# Map a function across a sequence
x = list(map(abs, [-1, -2, 0, 1, 2]))
print(x)
