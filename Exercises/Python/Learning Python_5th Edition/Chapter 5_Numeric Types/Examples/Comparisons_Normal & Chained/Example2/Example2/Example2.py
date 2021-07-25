X = 2
Y = 4
Z = 6

# Chained comparisons: range tests
print(X < Y < Z)
print(X < Y and Y < Z)
print(X < Y > Z)
print(X < Y and Y > Z)
print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)

# Same as: 1 == 2 and 2 < 3
# Not same as: False < 3
print(1 == 2 < 3)

