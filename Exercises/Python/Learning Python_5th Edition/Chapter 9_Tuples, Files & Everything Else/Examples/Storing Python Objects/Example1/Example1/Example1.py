# Native Python objects
X, Y, Z = 43, 44, 45

# Must be strings to store in file
S = "Spam"
D = {"a": 1, "b":2}
L = [1, 2, 3]

# Create output text file
F = open("datafile.txt", "w")

# Terminate lines with \n
F.write(S + "\n")

# Convert numbers to string
F.write("%s, %s, %s\n" %(X, Y, Z))

# Convert and separate with $
F.write(str(L) + "$" + str(D) + "\n")
F.close()

# Raw string display
chars = open("datafile.txt").read()

# User-friendly display
print(chars)

# Open again
F = open("datafile.txt")
# Read one line
line = F.readline()
# Remove end-of-line
print(line.rstrip())


# Next line from file
line = F.readline()
# It's a string here
# Split(parse) on commas
parts = line.split(",")
print(parts)
# Convert from string to int
print(int(parts[1]))
# Convert all in list at once
numbers = [int(P) for P in parts]
print(numbers)

# Next line from file
line = F.readline()
print(line)

# Split(parse) on $
parts = line.split("$")
print(parts)

# Convert to any object type
print(eval(parts[0]))

# Do the same for all in list
objects = [eval(P) for P in parts]
print(objects)






































