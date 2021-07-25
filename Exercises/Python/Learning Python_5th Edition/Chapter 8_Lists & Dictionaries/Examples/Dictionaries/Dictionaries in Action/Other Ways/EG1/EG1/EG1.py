# Traditional literal expression
D = {"name": "Bob", "age": 40}
print(D)

# Assign by keys dynamically
D = {}
D["name"] = "Bob"
D["age"] = 40
print(D)

# dict keyword argument form
D = dict(name = "Bob", age = 40)
print(D)

# dict key/value tuples form
D = dict([("name", "Bob"), ("age", 40)])
print(D)

D = dict.fromkeys(["a", "b"], 0)
print(D)