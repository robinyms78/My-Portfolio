L = [1,2,1,3,2,4,5]
print(set(L))

# Remove duplicates
L = list(set(L))
print(L)

# But order may change
print(list(set(["yy", "cc", "aa", "xx", "dd", "aa"])))

# Find list differences
print(set([1,3,5,7]) - set([1,2,4,5,6]))

# Find string diffrences
print(set("abcdefg") - set("abdghij"))

# Find differences, mixed
print(set("spam") - set(["h", "a", "m"]))

# In bytes but not in bytearray
print(set(dir(bytes)) - set(dir(bytearray)))

# In bytearrat but not in bytes
print(set(dir(bytearray)) - set(dir(bytes)))

# Order matters in sequence
L1, L2 = [1,3,5,2,4], [2,5,3,4,1]
print(L1 == L2)

# Order-neutral equality
print(set(L1) == set(L2))

# Similar but results ordered
print(sorted(L1) == sorted (L2))
print("spam" == "asmp", set("spam") == set("asmp"), sorted("spam") == sorted("asmp"))









