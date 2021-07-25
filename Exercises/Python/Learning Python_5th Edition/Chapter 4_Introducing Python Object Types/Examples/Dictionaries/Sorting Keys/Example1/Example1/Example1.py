D = {"a": 1, "b": 2, "c": 3}

# Unordered keys list
Ks = list(D.keys())
print(Ks)

# Sorted keys list
Ks.sort()
print(Ks)

# Iterate through sorted keys
for key in Ks:
    print(key, "=>", D[key])

