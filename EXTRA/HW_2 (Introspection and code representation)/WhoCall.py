import inspect
import types


def whocall(depth=1):
    stack = inspect.stack()

    try:
        caller_frame = stack[depth]
    except IndexError:
        return '<UNIVERSE>', ''

    caller_code = caller_frame[0].f_code
    caller_globals = caller_frame[0].f_globals

    caller_function = types.FunctionType(caller_code, caller_globals)

    signature = inspect.signature(caller_function)
    parameters = ' '.join(str(param) for param in signature.parameters)
    return caller_function.__name__, parameters


# class C:
#     def fun(self, arg, *args, kw="KW", **kwargs):
#         return whocall(arg)
#
#     lfun = lambda self, arg: whocall(arg)
#
#
# def fun():
#     return whocall(1)
#
#
# print(C().fun(0), C().lfun(0), fun())
# print(C().fun(1), C().lfun(1))
# print(C().fun(2, 3, 4, kw=123), C().lfun(2))
# print(C().fun(3), C().lfun(42))

