D = {"a": 1, "b": 2, "c": 3}
print(D)

# Sorting a view object doesn't work
Ks = D.keys()
# print(Ks.sort())

# Force it to be a list and then sort
Ks = list(Ks)
Ks.sort()
print(Ks)
for k in Ks:
    print(k, D[k])

# Or you can use sorted on the keys
# sorted() accepts any iterable
# sorted() returns its result
Ks = D.keys()
for k in sorted(Ks):
    print(k, D[k])

# Better yet, sort the dict directly
# dict iterators return keys
for k in sorted(D):
    print(k, D[k])

