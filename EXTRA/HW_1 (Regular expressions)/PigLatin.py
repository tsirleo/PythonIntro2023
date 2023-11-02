import re


def translate_word(word):
    if re.fullmatch(r"[aeiou]+[b-df-hj-np-tv-z']+[aeiou]+[a-z']*", word):
        return re.sub(r"([aeiou]+[b-df-hj-np-tv-z']+)([aeiou]+[a-z']*)", r"\2\1ay", word)
    elif re.fullmatch(r"[aeiou]+[b-df-hj-np-tv-z']*", word):
        return word + "yay"
    elif re.fullmatch(r"[b-df-hj-np-tv-z']+", word):
        return word
    else:
        return re.sub(r"([b-df-hj-np-tv-z']+)([aeiou]+[a-z']*)", r"\2\1ay", word)


def translate_sentence(sentence):
    words = re.findall(r"[a-zA-Z']+|[0-9]+|[^a-zA-Z0-9']+", sentence)
    translated_sentence = ''
    for word in words:
        if word.isalpha() or "'" in word:
            translated_word = translate_word(word.lower())
            if re.match(r"[A-Z]", word[0]):
                translated_word = translated_word.capitalize()
            translated_sentence += translated_word
        else:
            translated_sentence += word
    return translated_sentence


input_lines = []
while line := input():
    input_lines.append(line)

for line in input_lines:
    print(translate_sentence(line))
