S = "abcdefghijklmnop"

# Skipping items
print(S[1:10:2])
print(S[::2])

S = "hello"

# Reversing items
print(S[::-1])

# Bounds roles differ
S = "abccdfg"
print(S[5:1:-1])

# Slicing syntax
print("spam"[1:3])

# Slice objects with index syntax + object
print("spam"[slice(2,3)])
print("spam"[::-1])
print("spam"[slice(None, None, -1)])



