﻿print({1,2,3} | {3,4})
# print({1,2,3} | [3,4])
print({1,2,3}.union([3,4]))
print({1,2,3}.union({3,4}))
print({1,2,3}.union(set([3,4])))
print({1,2,3}.intersection((1,3,5)))
print({1,2,3}.issubset(range(-5,5)))