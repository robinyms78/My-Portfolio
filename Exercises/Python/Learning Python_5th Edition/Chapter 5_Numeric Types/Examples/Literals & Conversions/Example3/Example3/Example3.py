# Number => digit strings
print(oct(64), hex(64), bin(64))

# Digits => numbers in scripts and strings
print(64, 0o100, 0x40, 0b1000000)

print(int("64"), int("100", 8), int("40", 16), int("1000000", 2))

# Literal forms supported too
print(int("0x40", 16), int("0b1000000", 2))