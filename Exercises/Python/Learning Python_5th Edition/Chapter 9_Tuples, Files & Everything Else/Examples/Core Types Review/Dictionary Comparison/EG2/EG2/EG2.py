D1 = {"a": 1, "b": 2}
D2 = {"a": 1, "b": 3}

print(list(D1.items()))
print(sorted(D1.items()))

# Magnitude test in 3.X
print(sorted(D1.items()) < sorted(D2.items()))
print(sorted(D1.items()) > sorted(D2.items()))