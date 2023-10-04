def sign(perm):
    _sign = 1
    for i in range(len(perm) - 1):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                _sign *= -1
    return _sign


def permutations(ind):
    if len(ind) == 1:
        return [ind]

    _permutations = []
    for i in range(len(ind)):
        sub_perms = permutations(ind[:i] + ind[i + 1:])
        for sub_perm in sub_perms:
            _permutations.append([ind[i]] + sub_perm)

    return _permutations


def det4(r0, r1, r2, r3):
    matrix = [list(r0), list(r1), list(r2), list(r3)]
    ind = [0, 1, 2, 3]
    _permutations = permutations(ind)

    det = 0
    for perm in _permutations:
        comp = 1
        for i in range(len(matrix)):
            comp *= matrix[i][perm[i]]
        det += comp * sign(perm)

    return det


# print(det4((5, -4, 4, -7), (1, -2, 6, 0), (3, -8, -6, -4), (-1, 2, -9, 3)))
