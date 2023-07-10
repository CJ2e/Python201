# args are returned as a tuple


def add_numbers(*args):
    print(args)
    print(type(args))


add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
