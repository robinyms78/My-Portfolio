class Ternary():
    def example1(self):
        A = "t" if "spam" else "f" # For strings, nonempty means true
        print(A)

    def example2(self):
        A = "t" if "" else "f"
        print(A)

    def example3(self):
        A = ["f", "t"][bool("")]
        B = ["f", "t"][bool("spam")]
        print(A)
        print(B)

    def example4(self):
        L = [1, 0, 2, 0, "spam", "", "ham", []]
        A = list(filter(bool, L))  # Get true values
        B = [x for x in L if x]    # Comprehension
        C = [any(L), all(L)]       # Aggregate truth
        print(A)
        print(B)
        print(C)



    
