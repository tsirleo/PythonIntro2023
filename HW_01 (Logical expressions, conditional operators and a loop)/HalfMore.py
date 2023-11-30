import sys

major_obj = None
count = 0

for cur_object in sys.stdin:
    cur_object = cur_object.strip()
    if not cur_object:
        break
    if count == 0:
        major_obj = cur_object
        count = 1
    elif major_obj == cur_object:
        count += 1
    else:
        count -= 1

print(eval(major_obj))
