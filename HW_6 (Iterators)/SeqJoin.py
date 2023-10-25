def joinseq(*iter_args):
    iter_args = [iter(seq) for seq in iter_args]
    first_chars = [next(_iter, -1) for _iter in iter_args]
    not_none_chars = [char for char in first_chars if char != -1]
    while len(not_none_chars):
        char = min(not_none_chars)
        yield char
        first_chars[first_chars.index(char)] = next(iter_args[first_chars.index(char)], -1)
        not_none_chars = [char for char in first_chars if char != -1]


# print("".join(joinseq("abs", "qr", "azt")))
# import random
# random.seed(42)
# L, W, M = 666, 20, 100
# S = (iter(random.sample(range(M), random.randint(1, W))) for i in range(L))
# print(*joinseq(*S))
