from math import factorial
from decimal import Decimal, getcontext


# def PiGen():
#     _sum = k = 0
#     getcontext().prec = 1200
#     const = Decimal(426880) * Decimal(10005).sqrt()
#
#     while True:
#         _sum += Decimal(((-1) ** k) * factorial(6 * k) * (545140134 * k + 13591409)) / Decimal(factorial(3 * k) * (factorial(k) ** 3) * (640320 ** (3 * k)))
#         if k > 0:
#             yield from str(const / _sum)[14 * k + 1:14 * (k + 1) + 1]
#         else:
#             yield from str(const / _sum)[0:15]
#         k += 1


# This one is optimized by used operations which are minimized
def PiGen():
    _sum = k = 0
    getcontext().prec = 1200
    const = Decimal(426880) * Decimal(10005).sqrt()
    sign = (-1) ** k
    facto_1 = factorial(6 * k)
    facto_2 = factorial(3 * k)
    facto_3 = factorial(k)
    expr_1 = (545140134 * k + 13591409)
    expr_2 = facto_3 ** 3
    expr_3 = 640320 ** (3 * k)
    _sum += Decimal(sign * facto_1 * expr_1) / Decimal(facto_2 * expr_2 * expr_3)
    yield from str(const / _sum)[0:15]

    while True:
        k += 1
        sign *= (-1)
        for num in range(6 * k - 5, 6 * k + 1):
            facto_1 *= num
        for num in range(3 * k - 2, 3 * k + 1):
            facto_2 *= num
        facto_3 *= k
        expr_1 += 545140134
        expr_2 = facto_3 ** 3
        expr_3 *= 262537412640768000
        _sum += Decimal(sign * facto_1 * expr_1) / Decimal(facto_2 * expr_2 * expr_3)
        yield from str(const / _sum)[14 * k + 1:14 * (k + 1) + 1]

# print(*(c[0] for c in zip(PiGen(), range(30))))
# from itertools import islice
# print("".join(islice(PiGen(), n := 500, n + 10)))
# print("".join(islice(PiGen(), n := 1000, n + 10)))
