# Make a new file in putput mode ("w" is write)
f = open("data.txt", "w")

# Write strings of characters to it
f.write("Hello\n")
f.write("world\n")

# Close to flush output buffers to disk
f.close()

# "r"(read) is the default processing mode
f = open("data.txt")

# Read entire file into a string
text = f.read()

# Print interprets control characters
print(text)

# File content is always a string
text.split()
for line in open("data.txt"):
    print(line)
