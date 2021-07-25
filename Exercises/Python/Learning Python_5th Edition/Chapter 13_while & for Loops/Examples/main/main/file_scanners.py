class Files():
    def example1(self):
        file = open("Test/test.txt", "r")        # Let Python collect results
        print(file.read())

    def example2(self):
        file = open("Test/test.txt")
        while True:
            char = file.read(1)   # Read by character
            if not char:          # Empty string means end-of-file
                break
            print(char)

        for char in open("Test/test.txt").read():
            print(char)

    # File scanners
    def example3(self):
        file = open("Test/test.txt")
        while True:
            line = file.readline()      # Read line by line
            if not line:
                break
            print(line.rstrip())        # Line already has a \n

        file = open("Test/test.txt", "rb")
        while True:
            chunk = file.read(10)       # Read byte chunks up to 10 bytes
            if not chunk:
                break
            print(chunk)

    # File scanners
    def example4(self):
        for line in open("Test/test.txt").readlines():
            print(line.rstrip())

        for line in open("Test/test.txt"):  # Use iterators best for text input
            print(line.rstrip())






