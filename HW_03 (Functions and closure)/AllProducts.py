from math import ceil


def factorize(n, start, cur_factor, factor_list):
    _breakpoint = ceil(n**0.5)
    _breakpoint += 1 if n == _breakpoint ** 2 else 0
    for i in range(start, _breakpoint):
        if n % i == 0:
            factorize(n // i, i, cur_factor + [i], factor_list)
    factor_list.append(cur_factor + [n])


def print_factorizations(n):
    factor_list = []
    factorize(n, 2, [], factor_list)
    for elem in factor_list:
        print('*'.join(map(str, elem)))


print_factorizations(int(input()))
