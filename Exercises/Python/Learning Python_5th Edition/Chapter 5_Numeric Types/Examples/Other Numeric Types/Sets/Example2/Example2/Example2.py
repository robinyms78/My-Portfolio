for item in set("abc"): 
    print(item * 3)

S = set([1,2,3])

# Expressions require both to be sets
print(S | set([3,4]))
# print(S | [3,4])

# But their methods allow any iterable
print(S.union([3,4]))

print(S.intersection((1,3,5)))

print(S.issubset(range(-5,5)))

