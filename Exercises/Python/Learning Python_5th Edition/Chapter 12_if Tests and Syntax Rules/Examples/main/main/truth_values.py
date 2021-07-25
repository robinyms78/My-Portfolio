class Truth_Values():
    def example1(self):
        print(2 < 3, 3 < 2)   # Less than: return True or False

    def example2(self):
        print(2 or 3, 3 or 2)  # Return left operand if true
                               # Else, return right operand (true or false)

    def example3(self):
        print([] or 3)
        print([] or {})

    def example4(self):
        print(2 and 3, 3 and 2) # Return left operand if false
                                # Else, return right operand (true or false)

    def example5(self):
        print([] and {})
        print(3 and [])

