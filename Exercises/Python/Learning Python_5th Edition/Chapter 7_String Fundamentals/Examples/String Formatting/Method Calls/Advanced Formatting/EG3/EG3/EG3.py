# Hex, octal, binary
print("{0:X}, {1:o}, {2:b}".format(255, 255, 255))

# Other to/from binary
print(bin(255), int("11111111", 2), 0b11111111)

# Other to/from hex
print(hex(255), int("FF", 16), 0xFF)

# Other to/from octal, in 3.X
print(oct(255), int("377", 8), 0o377)