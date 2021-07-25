# Expression (only) binary format code
print("{0:b}".format((2**16) - 1))
#print("%b" %((2**16) - 1))

# But other more general options work too
print(bin((2**16) - 1))

# Usable with both method and % expression
print("%s" %bin((2**16) - 1))

# With 2.7/3.1+ relative numbering
print("{}".format(bin((2**16) - 1)))

# Slice off 0b to get exact equivalent
print("%s" %bin((2**16) - 1)[2:])

# New str.format method feature in 3.1/2.7
print("{:,d}".format(999999999999))

# But % is same as simple 8-line function
# print("%s" % commas(999999999999))