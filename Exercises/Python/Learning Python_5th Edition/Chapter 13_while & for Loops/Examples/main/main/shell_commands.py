import os
from urllib.request import urlopen

class Shell():
    def example1(self):
        F = os.open("dir") # Read line by line
        F.readline()

    def example2(self):
        F = os.popen("dir")
        F.read(50)              # Read by sized blocks
        print(F)

    def example3(self):
        F1 = os.popen("dir").readlines()[0]  # Read all lines: index
        F2 = os.popen("dir").read()[:50]     # Read all at once: slice
        print(F1)
        print(F2)

    def example4(self):
        for line in os.popen("dir"):        # File ine iterator loop
            print(line.rstrip())

    def example5(self):
        os.system("systeminfo")
        for line in os.popen("systeminfo"):
            print(line.rstrip())

    def example6(self):
        for (i, line) in enumerate(os.popen("systeminfo")):
            if i == 4:   # Formatted, limited display 
                break
            print("%05d) %s" %(i, line.rstrip())) 

    def example7(self):
        # Parse for specific lines, case neutral
        for line in os.popen("systeminfo"):
            parts = line.split(":")
            if parts and parts[0].lower() == "system type":
                print(parts[1].strip())

    def example8(self):
        # awk emulation: extract column 1 from whitespace-delimited file
        for val in [line.split()[0] for line in open("Test/test.txt")]:
            print(val)

    def example9(self):
        # Same, but more explicit code that retains result
        col1 = []
        for line in open("Test/test.txt"):
            cols = line.split()
            col1.append(cols[0])
        for item in col1:
            print(item)

    def example10(self):
        # Same, but a reusable function
        def awker(file, col):
            return [line.strip().split()[col - 1] for line in open(file)]

        print(awker("Test/test.txt", 1)) # list of strings
        print(",".join(awker("Test/test.txt", 1))) # Put commas between

    def example11(self):
        for line in urlopen("http://www.sony-global-mo.co.jp/index.html"):
            print(line)
















