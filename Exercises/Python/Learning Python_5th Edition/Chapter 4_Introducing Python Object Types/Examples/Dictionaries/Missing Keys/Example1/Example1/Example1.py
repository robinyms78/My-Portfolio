D = {"a": 1, "b": 2, "c": 3}

# Assigning new keys grows dictionaries
D["e"] = 99
print(D)

# Referencing a nonexistent key is an error
D["f"]
print(D)

