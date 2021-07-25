D = {"a": 1, "b": 2, "c": 3}

# Index but with a default
value = D.get("x", 0)
print(value)

# if/else expression form
value = D["x"] if "x" in D else 0
print(value)