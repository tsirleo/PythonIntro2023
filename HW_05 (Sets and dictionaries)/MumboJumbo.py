checked_word = input()
first_lang = set(checked_word)
second_lang = set()
vowels = set(checked_word[0])
i = 0

while word := input():
    if i % 2 == 0:
        second_lang = second_lang | set(word)
    else:
        first_lang = first_lang | set(word)
    vowels.add(word[0])
    i += 1

print("Mumbo" if len(first_lang - vowels) > len(second_lang - vowels) else "Jumbo")
