# Make a set out of a sequence
X = set("spam")

# Make a set with set literals
Y = {"h", "a", "m"}

# A tuple of two sets without parentheses
print(X, Y)

# Intersection
print(X & Y)

# Union
print(X | Y)

# Difference
print(X - Y)

# Superset
print(X > Y)

# Set comprehensions
print({n ** 2 for n in [1, 2, 3, 4]})
