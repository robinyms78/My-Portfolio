print(ord("s"))
print(chr(115))

S = "5"
S = chr(ord(S) + 1)
print(S)
S = chr(ord(S) + 1)
print(S)

print(int("5"))
print(ord("5") - ord("0"))

# Convert binary digits to integer with ord
B = "1101"
I = 0

while B != "":
    I = I * 2 + (ord(B[0]) - ord("0"))
    B = B[1:]

print(I)

# Convert binary to integer: built-in
print(int("1101", 2))

# Convert integer to binary: built-in
print(bin(13))

