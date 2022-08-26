def decorator_function(func):
    def wrapper(*args):
        lenn = len(args) - 1
        lennn = lenn + 2
        sorted_args = sorted(args)
        print(func(), sorted_args)
        print('━' * 10, '━' * 14, '━' * 10)

        for i in range(lenn + 1):
            print("┃", str(sorted_args[i]).ljust(lenn), " ", "┃", "кратне 3".ljust(12, " ")
            if sorted_args[i] % 3 == 0 else "нe кратне 3".ljust(12, ' '), "┃", "парне".ljust(8, ' ')
                  if sorted_args[i] % 2 == 0 else "не парне".ljust(8, ' '), "┃")
            print("┃", "━" * lennn, "┃", "━" * 12, "┃", "━" * 8, "┃")

    return wrapper


@decorator_function
def my_func(*args):
    print(args)
    return args


my_func(99, 2, 9, 4, 6, 5)

my_func(333, 77, 3, 6, 9)