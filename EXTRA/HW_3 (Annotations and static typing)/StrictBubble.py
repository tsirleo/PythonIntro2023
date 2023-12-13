from typing import TypeVar, cast

Sortable = TypeVar('Sortable', list, tuple)


def bubble(seq: Sortable) -> Sortable:
    n = len(seq)
    for i in range(n):
        for j in range(0, n-i-1):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq


# c = [60, 66, 67, 64, 65, 68, 60, 63, 63, 67, 66, 66, 67, 64, 66, 68, 61, 67, 64, 65]

# for s in (bubble(cast(Sortable, c)),
#           bubble(list(map(float, c))),
#           bubble(list(map(str, c))),
#           bubble(list(map(list, map(str, c))))):
#     print(*s)

# bubble(list(map(complex, c)))
# bubble(tuple(map(float, c)))
