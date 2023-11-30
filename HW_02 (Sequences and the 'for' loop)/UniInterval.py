sections_tuple = eval(input())

length = len(sections_tuple)
x = sorted([(sections_tuple[i][0], False) for i in range(length)] + [(sections_tuple[i][1], True) for i in range(length)])

result_length_sum = 0
counter = 0
for i in range(length * 2):
    if counter and i:
        result_length_sum += x[i][0] - x[i - 1][0]
    if x[i][1]:
        counter += 1
    else:
        counter -= 1

print(result_length_sum)
