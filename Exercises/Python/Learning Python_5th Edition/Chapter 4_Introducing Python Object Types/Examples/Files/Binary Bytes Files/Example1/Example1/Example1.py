import struct

# Create packed binary data
packed = struct.pack(">i4sh", 7, b"spam", 8)

# 10 bytes, not objects or text
print(packed)

# Open binary output file
file = open("data.bin", "wb")

# Write packed binary data
file.write(packed)

file.close()

# Open/read binary data file
data = open("data.bin", "rb").read()

# 10 bytes, unaltered
print(data)

# Slice bytes in the middle
print(data[4:8])

# A sequence of 8-bit bytes
print(list(data))

# Unpack into objects again
unpacked = struct.unpack(">i4sh", data)
print(unpacked)


