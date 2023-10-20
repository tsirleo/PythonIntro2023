def find_substring_by_pattern(source_str, pattern):
    for i in range(len(source_str) - len(pattern) + 1):
        flag = True
        for j in range(len(pattern)):
            if pattern[j] != '@' and pattern[j] != source_str[i + j]:
                flag = False
                break
        if flag:
            return i
    return -1


print(find_substring_by_pattern(input(), input()))
