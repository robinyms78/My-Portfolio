class If_Statements():
    # Basic example
    def example1(self):
        if 1:
            print("true")

    # Basic example
    def example2(self):
        if not 1:
            print("true")
        else:
            print("false")

    # Multiway branching
    def example3(self):
        x = "killer rabbit"
        if x == "roger":
            print("shave and a haircut")
        elif x == "bugs":
            print("what's up doc?")
        else:
            print("Run away! Run away!")

    # Multiway branching
    def example4(self):
        choice = "ham"
        print({"spam": 1.25,                # A dictionary-based "switch"
               "ham": 1.99,                 # Use has_key or get for default
               "eggs": 0.99,
               "bacon": 1.10}[choice])

    # Multiway branching
    def example5(self):
        choice = "ham"
        if choice == "spam":
            print(1.25)
        elif choice == "ham":
            print(1.99)
        elif choice == "eggs":
            print(0.99)
        elif choice == "bacon":
            print(1.10)
        else:
            print("Bad choice")

    # Handling switch defaults
    def example6(self):
        branch = {"spam": 1.25,
                  "ham": 1.99,
                  "eggs": 0.99}
        print(branch.get("spam", "Bad choice"))
        print(branch.get("bacon", "Bad choice"))

    # Handling switch defaults
    def example7(self):
        branch = {"spam": 1.25,
                  "ham": 1.99,
                  "eggs": 0.99}
        choice = "bacon"
        if choice in branch:
            print(branch[choice])
        else:
            print("Bad choice")

    # Handling switch defaults
    def example8(self):
        branch = {"spam": 1.25,
                  "ham": 1.99,
                  "eggs": 0.99}
        choice = "bacon"
        try:
            print(branch[choice])
        except KeyError:
            print("Bad choice")




