from typing import List

Sortable = List


def bubble(sequence: Sortable) -> Sortable:
    n = len(sequence)
    for i in range(n):
        for j in range(0, n-i-1):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    return sequence


# c = [60, 66, 67, 64, 65, 68, 60, 63, 63, 67, 66, 66, 67, 64, 66, 68, 61, 67, 64, 65]
# for s in ( bubble(c),
#            bubble(list(map(float, c))),
#            bubble(list(map(str, c))),
#            bubble(list(map(list, map(str, c))))):
#     print(*s)
# bubble(list(map(complex, c)))
# bubble(tuple(map(float, c)))
