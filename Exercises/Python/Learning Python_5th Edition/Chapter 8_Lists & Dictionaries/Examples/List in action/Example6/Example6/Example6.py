L = ["abc", "ABD", "aBe"]

# Sort with mixed case
L.sort()
print(L)

# Normalize to lowercase
L.sort(key = str.lower)
print(L)

# Change sort order
L.sort(key = str.lower, reverse = True)
print(L)

# Sorting built-in
print(sorted(L, key = str.lower, reverse = True))

# Pretransform items: differs
print(sorted([x.lower() for x in L], reverse = True))