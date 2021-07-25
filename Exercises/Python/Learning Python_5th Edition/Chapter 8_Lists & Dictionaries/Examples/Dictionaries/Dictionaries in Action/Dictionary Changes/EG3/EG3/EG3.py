D = {"a":1, "b":2, "c":3}
del D["b"]
K = D.keys()
V = D.values()
print(K)
print(V)

# Keys (and some items) views are set-like
print(K | {"x": 4})
# print(V & {"x": 4})
# print(V & {"x": 4}.values())

# Intersect key values
D = {"a": 1, "b": 2, "c": 3}
print(D.keys() & D.keys())

# Intersect keys and set
print(D.keys() & {"b"})

# Intersect keys and dictionary
print(D.keys() & {"b": 1})

# Union keys and set
print(D.keys() | {"b", "c", "d"})

# Items set-like if hashable
D = {"a": 1}
print(list(D.items()))

# Union view and view
print(D.items() | D.keys())

# dict treated same as its keys
print(D.items() | D)

# Set of key/value pairs
print(D.items() | {("c", 3), ("d", 4)})

# dict accepts iterable sets too
print(dict(D.items() | {("c", 3), ("d", 4)}))
