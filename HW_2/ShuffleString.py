data = [input(), input(), "No", []]
for step in range(len(data[0])):
    for i in range(step):
        data[3].append(data[0][i::step])
    data[2] = step if (data[1] == "".join(data[3]) and str(data[2]) == "No") else data[2]
    data[3].clear()
print(data[2])
