import random


def divrandom(a, b, s, p):
    possible_vals = []
    start = a if a <= b else b
    end = b if a <= b else a

    cur_num = start
    while cur_num <= end:
        rand_num = random.randrange(start, end + 1, s)
        if rand_num % p != 0:
            return rand_num
        if cur_num % p != 0:
            possible_vals.append(cur_num)
        cur_num += s

    if not possible_vals:
        return 0

    return random.choice(possible_vals)


# print(divrandom(10, 21, 5, 2))
