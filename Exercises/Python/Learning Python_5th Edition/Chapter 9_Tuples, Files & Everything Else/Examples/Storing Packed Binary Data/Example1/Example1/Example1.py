# Open binary output file
F = open("data.bin", "wb")

import struct
# Make packed binary data
data = struct.pack(">i4sh", 7, b"spam", 8)
print(data)

# Write byte string
F.write(data)
F.close()

F = open("data.bin", "rb")
# Get packed binary data
data = F.read()
print(data)

# Convert to Python objects
values = struct.unpack(">i4sh", data)
print(values)

