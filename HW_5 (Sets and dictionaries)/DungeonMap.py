def get_input():
    _dungeon = {}
    data = input().split()
    while len(data) > 1:
        if data[0] in _dungeon:
            _dungeon[data[0]].add(data[1])
            if data[1] in _dungeon:
                _dungeon[data[1]].add(data[0])
            else:
                _dungeon[data[1]] = {data[0]}
        else:
            _dungeon[data[0]] = {data[1]}
            if data[1] in _dungeon:
                _dungeon[data[1]].add(data[0])
            else:
                _dungeon[data[1]] = {data[0]}
        data = input().split()
    start = data[0]
    end = input()

    return _dungeon, start, end

# recursion don't work with big input data (max recursion depth error got caught)
# def explore_dungeon(_dungeon, start, in_path=None):
#     if in_path is None:
#         in_path = set()
#     in_path.add(start)
#     for entry in dungeon[start]:
#         if entry not in in_path:
#             explore_dungeon(dungeon, entry, in_path)
#
#     return in_path


def explore_dungeon(_dungeon, start):
    in_path = set()
    stack = [start]
    while stack:
        current_room = stack.pop()
        pre_length = len(in_path)
        in_path.add(current_room)
        if len(in_path) == pre_length:
            break
        for entry in _dungeon[current_room]:
            if entry not in in_path:
                stack.append(entry)

    return in_path


dungeon, startpoint, endpoint = get_input()
path_mult = explore_dungeon(dungeon, startpoint)
print("YES" if endpoint in path_mult else "NO")
