matrixSize = eval(input())

M = matrixSize[0]
N = matrixSize[1]

# empty matrix with zeros
matrix = [[0] * M for _ in range(N)]
i, j = 1, 0
value = 1

for coordinates_sum in range(1, N + M - 1):
    if not (coordinates_sum % 2):
        while j >= 0:
            matrix[i][j] = value % 10
            value += 1
            if i >= N-1:
                break
            i += 1
            j -= 1
        j += 1
    else:
        while i >= 0:
            matrix[i][j] = value % 10
            value += 1
            if j >= M-1:
                break
            j += 1
            i -= 1
        i += 1

for row in matrix:
    print(' '.join(map(str, row)))
