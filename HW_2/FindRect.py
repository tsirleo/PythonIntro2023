grid = []
rectangle_count = 0

while line := input():
    if not line:
        break
    grid.append(line)

line_length = len(grid[0])

for i in range(len(grid)):
    if i <= len(grid) - 2:
        for j in range(line_length - 1):
            if grid[i][j:j + 2] == "#.":
                if grid[i + 1][j] == ".":
                    rectangle_count += 1
        if grid[i][line_length - 1] == "#":
            if grid[i + 1][line_length - 1] == ".":
                rectangle_count += 1
    else:
        for j in range(line_length - 1):
            if grid[i][j:j + 2] == "#.":
                rectangle_count += 1
        if grid[i][line_length - 1] == "#":
            rectangle_count += 1

print(rectangle_count)
