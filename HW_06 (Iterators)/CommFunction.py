import itertools


def checkcomm(fun, *args):
    result = fun(*args)
    for perm in itertools.permutations(args):
        if fun(*perm) != result:
            return False

    return True


# print(checkcomm(max, 1, 9, 2, 7, 3, 6))
