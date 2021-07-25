class Exercise():
    def exercise1(self):
        print("Exercise1\n")
        X = "Spam"
        def func():
            print(X)

        func()

    def exercise2(self):
        print("Exercise2\n")
        X = "Spam"
        def func():
            X = "NI!"

        func()
        print(X)

    def exercise3(self):
        print("Exercise3\n")
        X = "Spam"
        def func():
            X = "NI"
            print(X)

        func()
        print(X)

    X = "Spam"
    def exercise4(self):
        print("Exercise4\n")    
        def func():
            global X
            X = "NI"

        func()
        print(X)

    def exercise5(self):
        print("Exercise5\n")
        X = "Spam"
        def func():
            X = "NI"
            def nested():
                print(X)
            nested()

        func()
        print(X)

    def exercise6(self):
        print("Exercise6\n")
        def func():
            X = "NI"
            def nested():
                nonlocal X
                X = "Spam"
            nested()
            print(X)

        func()

