class Application():
    def example1(self):
        print("Example1\n") 
        for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
            print(a, b, c)                             # b gets [2, 3]
            
        print("\n")
        for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
            print(a, b, c)

        print("\n")
        for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
            a, b, c = all[0], all[1:3], all[3]
            print(a, b, c)

