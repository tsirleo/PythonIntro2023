word_dict = {}

while string := input():
    words = string.split()
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))
dict_values = list(word_dict.values())
print(list(word_dict)[0] if len(dict_values) == 1 or dict_values[0] != dict_values[1] else "---")
