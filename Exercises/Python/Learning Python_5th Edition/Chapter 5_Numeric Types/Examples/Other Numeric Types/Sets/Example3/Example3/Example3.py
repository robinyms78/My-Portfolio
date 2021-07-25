# Built-in: same as in 2.6
print(set([1,2,3,4]))

# Add all items in an iterable
print(set("spam"))

# Set literals: new in 3.x (and 2.7)
print({1,2,3,4})

S = {"s", "p", "a", "m"}
print(S)

# Methods work as before
S.add("alot")
print(S)

S1 = {1,2,3,4}

# Intersection
print(S1 & {1,3})

# Union
print({1,5,3,6} | S1)

# Difference
print(S1 - {1,3,4})

# Superset
print(S1 > {1, 3})

# Empty sets print differently
print(S1 - {1,2,3,4})

# Because {} is an empty dictionary
print(type({}))

# Initialize an empty set
S = set()
S.add(1.23)
print(S)


















