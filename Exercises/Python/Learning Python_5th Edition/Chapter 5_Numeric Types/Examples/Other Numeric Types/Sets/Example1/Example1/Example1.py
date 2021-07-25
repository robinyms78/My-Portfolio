x = set("abcde")
y = set("bdxyz")
print(x)
print(y)

# Difference
print(x - y)

# Union
print(x | y)

# Intersection
print(x & y)

# Symmetric difference (XOR)
print(x ^ y)

# Superset, subset
print(x > y, x < y)

# Membership(sets)
print("e" in x)

# But works on other types too
print("e" in "Camelot", 22 in [11, 22, 33])

# Same as x & y
z = x.intersection(y)
print(z)

# Insert an item
z.add("SPAM")
print(z)

# Merge: in-place union
z.update(set(["X", "Y"]))
print(z)

# Delete one item
z.remove("b")
print(z)




