# Append reference to same object
L = ["grail"]

# Generates cycle in object: [...]
L.append(L)
print(L)
