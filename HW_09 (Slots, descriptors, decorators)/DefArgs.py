import inspect


def DefArgs(*args):
    def decorator(func):
        signature = inspect.signature(func)
        func_params = list(signature.parameters)

        if len(args) < len(func_params):
            raise TypeError("Too few constants for the function parameters")

        def wrapper(*func_args):
            if len(func_args) > len(func_params):
                raise TypeError("Too many parameters")

            for i in range(len(func_args)):
                if not isinstance(func_args[i], type(args[i])):
                    raise TypeError("Parameter type does not match constant type")

            new_args = list(func_args) + list(args[len(func_args):len(func_params)])

            return func(*new_args)

        return wrapper

    return decorator


# @DefArgs(2, 3, 4)
# def mult(a, b):
#     return a * b
#
#
# for args in (), (4,), (7, 8), (7, 8, 9), ("q", "w"):
#     try:
#         print(mult(*args))
#     except TypeError:
#         print("Nope")
#
# try:
#     @DefArgs(2)
#     def mult(a, b):
#         return a * b
# except TypeError:
#     print("Nope")
