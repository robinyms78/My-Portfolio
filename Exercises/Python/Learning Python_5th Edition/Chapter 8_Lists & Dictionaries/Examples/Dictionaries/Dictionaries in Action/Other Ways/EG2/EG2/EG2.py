# List-based "record"
L = ["Bob", 40.5, ["dev", "mgr"]]
print(L[0])

# Positions/numbers for fields
print(L[1])
print(L[2][1])

# Dictionary-based "record"
D = {"name": "Bob", "age": 40.5, "jobs": ["dev", "mgr"]}
print(D["name"])
print(D["age"])

# Names mean more than numbers
print(D["jobs"][1])

D = dict(name = "Bob", age = 40.5, jobs = ["dev", "mgr"])
print(D["name"])
D["jobs"].remove("mgr")
print(D)

# A visited-state dictionary
D = {}
D["state1"] = True
print("state1" in D)

# Same, but in sets
S = set()
S.add("state1")
print("state1" in S)




