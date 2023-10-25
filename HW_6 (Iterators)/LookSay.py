def LookSay():
    current = '1'
    sequence = ''
    count = 1
    yield count
    while True:
        current = current + ' '
        for ind in range(len(current) - 1):
            if current[ind] == current[ind + 1]:
                count += 1
            else:
                sequence += str(count) + current[ind]
                yield count
                yield int(current[ind])
                count = 1
        current = sequence
        sequence = ''
        count = 1


# for i, l in enumerate(LookSay()):
#     print(f"{i}: {l}")
#     if i > 10:
#         break
