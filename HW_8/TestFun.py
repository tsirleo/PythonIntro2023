class Tester:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, suite, allowed=[]):
        ex_flag = False
        not_allowed_flag = False
        for params in suite:
            try:
                self.fun(*params)
            except Exception as e:
                if not any([isinstance(type(e), errClass) or issubclass(type(e), errClass) for errClass in allowed]):
                    not_allowed_flag = True
                ex_flag = True

        return 0 if not ex_flag else 1 if not_allowed_flag else -1


# T = Tester(int)
# print(T([(12,), ("12", 16)], []))
# print(T([(12,), ("12", 16), ("89", 8)], [ValueError, IndexError]))
# print(T([(12,), ("12", 16), ("89", 8), (1, 1, 1)], [ValueError, IndexError]))
