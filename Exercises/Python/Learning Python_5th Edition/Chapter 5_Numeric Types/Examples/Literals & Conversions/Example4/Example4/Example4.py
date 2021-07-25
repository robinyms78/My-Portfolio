print(eval("64"), eval("0o100"), eval("0x40"), eval("0b1000000"))

# Numbers => digits
print("{0:o}, {1:x}, {2:b}".format(64, 64, 64))

# Similar, in all Pythons
print("%o, %x, %x, %X" %(64, 64, 255, 255))

# New octal format in 2.6+
print(0o1, 0o20, 0o377)

X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
print(X)
print(oct(X))
print(bin(X))
