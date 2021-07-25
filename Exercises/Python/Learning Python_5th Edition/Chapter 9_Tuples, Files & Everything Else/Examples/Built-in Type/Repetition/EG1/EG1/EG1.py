L = [4, 5, 6]

# Like [4,5,6] + [4,5,6] + ...
X = L * 4

# [L] + [L] + ... = [L, L, ...]
Y = [L] * 4
print(X)
print(Y)

# Impacts Y but not X
L[1] = 0
print(X)
print(Y)

