from collections import Counter


class DefCounter(Counter):
    def __init__(self, string, missing=-1):
        super().__init__(string)
        self.missing = missing

    def __missing__(self, key):
        return self.missing

    def __abs__(self):
        return sum(value for value in self.values() if value > 0)


# A = DefCounter("QWEqweQWEqweQWE", missing=-10)
# print(A)
# A["P"] += 5
# print(A["T"], A["P"], abs(A), A.total())
# print(A)
