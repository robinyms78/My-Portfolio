D = dict(a = 1, b = 2, c = 3)
print(D)

# Makes a view object in 3.X, not a list
K = D.keys()
print(K)

# Force a real list in 3.X if needed
print(list(K))

# Ditto for values and items views
V = D.values()
print(V)
print(list(V))

D.items()
print(list(D.items()))

# List operations fail unless converted
# print(K[0])
print(list(K)[0])

# Iterators used automatically in loops
for k in D.keys():
    print(k)

# Still no need to call keys() to iterate
for key in D:
    print(key)

D = {"a":1, "b":2, "c": 3}
print(D)

# Views maintain same order as dictionary
K = D.keys()
V = D.values()
print(list(K))
print(list(V))

# Change the dictionary in place
del D["b"]
print(D)

# Reflected in any current view objects
print(list(K))

# Not true in 2.X! - lists detached from dict
print(list(V))












