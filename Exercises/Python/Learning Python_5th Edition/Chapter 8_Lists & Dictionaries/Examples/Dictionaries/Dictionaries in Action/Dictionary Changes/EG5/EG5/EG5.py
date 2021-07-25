D = {"a": 1, "b": 2, "c": 3}

# 2.X only: True/False
# print(D.has_key("c"))

# Required in 3.X
print("c" in D)

# Preferred in 2.X today
print("x" in D)

# Branch on result
if "c" in D:
    print("present", D["c"])

# Fetch with default
print(D.get("c"))
print(D.get("x"))

# Another option
if D.get("c") != None:
    print("present", D["c"])



