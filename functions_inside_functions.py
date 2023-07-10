userInput = input("Enter your name: ")


def thing1(name):
    print("Welcome to thing1", name)

    def thing2():
        print("Welcome to thing2", name)
    thing2()


thing1(userInput)
