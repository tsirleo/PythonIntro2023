from math import ceil

N = int(input())
B = ceil(N ** (1 / 3))
A = 1
count_pairs = 0

while A < B:
    if A ** 3 + B ** 3 > N:
        B -= 1
    elif A ** 3 + B ** 3 < N:
        A += 1
    else:
        count_pairs += 1
        A += 1

print(count_pairs)
