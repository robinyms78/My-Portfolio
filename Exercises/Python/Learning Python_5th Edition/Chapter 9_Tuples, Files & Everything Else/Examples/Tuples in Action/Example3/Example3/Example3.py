T = ("cc", "aa", "dd", "bb")

# Make a list from a tuple's items
tmp = list(T)

# Sort the list
tmp.sort()

# Make a tuple from the list's items
T = tuple(tmp)
print(T)

# Or use the sorted built-in, and save two steps
print(sorted(T))

T = (1,2,3,4,5)
L = [x + 20 for x in T]
print(L)

# Tuple methods in 2.6, 3.0 and later
# Offset of first appearance of 2
T = (1, 2, 3, 2, 4, 2)
print(T.index(2))

# Offset at appearance after offset 2
print(T.index(2,2))

# How many 2s are there?
print(T.count(2))

# This fails: can't change tuple itself
T = (1, [2, 3], 4)
# T[1] = "spam"
print(T)

# This works: can change mutables inside
T[1][0] = "spam"
print(T)














