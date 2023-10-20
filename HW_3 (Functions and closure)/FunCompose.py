from math import *


def compose(f, g):
    def h(*args):
        g_func_res = g(*args)
        g_func_res_reversed = g(*reversed(args))
        return f(g_func_res, g_func_res_reversed)

    return h


# print(compose(max, pow)(5, 6))
