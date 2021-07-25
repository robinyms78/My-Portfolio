class Exercise():
    def exercise1(self):
        S = "spam"
        sum_list = []
        for character in S:
            print(ord(character))
            sum_list.append(ord(character))

        result = sum(sum_list)
        print("Sum is %d\n" %(result))

        ord_list = list(map(ord,S))
        print(ord_list)

    def exercise2(self):
        for i in range(50):
            print("hello %d\n\a" %i)

    def exercise4_1(self):
        L = [1, 2, 4, 8, 16, 32, 64]
        X = 5

        i = 0
        while i < len(L):
            if 2**X == L[i]:
                print("at index", i)
                break
            i += 1
        else:
            print(X, "not found")

    def exercise4_2(self):
        L = [1, 2, 4, 8, 16, 32, 64]
        X = 5

        for item in L:
            if 2**X in L:
                print("at index", L.index(2**X))
                break
        else:
            print(X, "not found")

    def exercise4_3(self):
        L = [1, 2, 4, 8, 16, 32, 64]
        X = 5

        if 2**X in L:
            print("at index", L.index(2**X))
        else:
            print(X, "not found")

    def exercise4_4(self):
        power_list = []
        for i in range(7):
            power_list.append(2**i)

        print(power_list)

    def exercise4_5(self):
        L = [1, 2, 4, 8, 16, 32, 64]
        X = 5

        i = [i for i in range(len(L)) if 2**X == L[i]]

        if i:
            print("at index", i)
        else:
            print(X, "not found")

    def exercise4_6(self):
        power_list = [2**x for x in range(7)]
        print(power_list)




