import re


def process_search_res(_search_res):
    substrings = []
    if value := _search_res.group():
        substrings.append(f"{_search_res.start()}: {value}")

    for group_num, group_value in enumerate(_search_res.groups(), start=1):
        if group_value:
            substrings.append(f"{group_num}/{_search_res.start(group_num)}: {group_value}")

    for group_name, group_value in _search_res.groupdict().items():
        if group_value:
            substrings.append(f"{group_name}/{_search_res.start(group_name)}: {group_value}")

    if substrings:
        for string in substrings:
            print(string)
    else:
        print("<NONE>")


input_lines = []
pattern = re.compile(input())
while line := input():
    input_lines.append(line)

for line in input_lines:
    if search_result := pattern.search(line):
        process_search_res(search_result)
    else:
        print("<NONE>")
