# Open for text output: create/empty
myfile = open("myfile.txt", "w")

# Write a line of text: string
myfile.write("hello text file\n")
myfile.write("goodbye text file\n")

myfile.close()

# Open for text input: "r" is default
myfile = open("myfile.txt")

# Read the lines back
print(myfile.readline())
print(myfile.readline())

# Empty string: end-of-file
print(myfile.readline())


# Read all at once into a string
open("myfile.txt").read()

# User-friendly display
print(open("myfile.txt").read())

# Use file iterators, not reads
for line in open("myfile.txt"):
    print(line, end = "")






