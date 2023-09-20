max_num = float('-inf')
second_max = float('-inf')

while cur_num := int(input()):
    if cur_num > max_num:
        second_max = max_num
        max_num = cur_num
    elif second_max < cur_num < max_num:
        second_max = cur_num

if second_max != float('-inf') and second_max != max_num:
    print(second_max)
else:
    print('NO')