S = set()
S.add(1.23)

# Only immutable objects work in a set
#S.add([1,2,3])
#S.add({"a":1})

# No list or dict, but tuple OK
S.add((1,2,3))
print(S)

# Union: same as S.union(...)
print(S|{(4,5,6), (1,2,3)})

# Membership: by complete values
print((1,2,3) in S)
print((1,4,3) in S)


