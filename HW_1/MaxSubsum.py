from math import fabs

max_subsum = 0
cur_sum = int(input())

if cur_sum > 0:
    max_subsum = cur_sum
elif cur_sum < 0:
    max_subsum = cur_sum
    while number := int(input()):
        if number < 0:
            max_subsum = -int(min(fabs(max_subsum), fabs(number)))
        elif number > 0:
            max_subsum = number
            cur_sum = number
            break
    if cur_sum < 0:
        print(max_subsum)
        exit(0)

while number := int(input()):
    cur_sum += number
    if cur_sum < 0:
        cur_sum = 0
    if cur_sum > max_subsum:
        max_subsum = cur_sum

print(max_subsum)
