import math
from itertools import permutations


class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = float(a), float(b), float(c)
        if 0 < a < b + c and 0 < b < a + c and 0 < c < a + b:
            self.valid = True
        else:
            self.valid = False

    def __bool__(self):
        return self.valid

    def __abs__(self):
        if self.valid:
            p = (self.a + self.b + self.c) / 2
            return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        else:
            return float(0)

    def __eq__(self, other):
        for perm in permutations([other.a, other.b, other.c], 3):
            if math.isclose(self.a, perm[0]) and math.isclose(self.b, perm[1]) and math.isclose(self.c, perm[2]):
                return True
        else:
            return False

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __ne__(self, other):
        return abs(self) != abs(other)

    def __str__(self):
        return f"{self.a}:{self.b}:{self.c}"


tri = Triangle(3, 4, 5), Triangle(5, 4, 3), Triangle(7, 1, 1), Triangle(5, 5, 5), Triangle(7, 4, 4)
for a, b in zip(tri[:-1], tri[1:]):
    print(a if a else b)
    print(f"{a}={abs(a):.2f} {b}={abs(b):.2f}")
    print(a == b)
    print(a >= b)
    print(a < b)
