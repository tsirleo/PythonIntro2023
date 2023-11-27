import sys
import itertools

# text = (b"\x20\x20\x20\x20\x20\x2D\x20\xBD\xC8\xE1\x20\xC8\x96\x20\xE4\x9F\x20\x20\xE0\xE4\x9F"
#         b"\x20\x20\xF2\xE3\xE5\xE0\xE1\x96\xE4\x2C\x20\x20\xC8\x9F\x20\x20\x93\xE4\xE1\x20\x20"
#         b"\xC8\x96\x9F\x90\x91\x96\xF6\x96\x83\x96\xC8\xC8\x9F\xF2\xE4\xE2\x2C\x20\x20\xC8\x96"
#         b"\x91\x96\xE6\xF4\xE4\x96\x83\xE2\xC8\x9F\xF2\xE4\xE2\x0A\x90\x9F\x83\x9F\x81\x96\xC8"
#         b"\xF4\xF1\x2C\x20\x2D\x20\xF2\x83\xFC\xE6\xE1\x83\x20\xBA\x96\x9C\xF4\xC8\x20\x20\xF4"
#         b"\x20\x20\x85\x9F\xE4\x96\x83\x20\x20\x90\x9F\xF2\x90\x96\xE6\xC8\x9F\x20\x20\x9F\xE4"
#         b"\x9F\x94\xE4\xF4\x3B\x20\x20\xC8\x9F\x20\x20\xCB\xE4\x96\x90\xE1\xC8\x20\x20\xAF\x91"
#         b"\xE3\xE1\xF6\xE2\xF4\xE0\x0A\x90\x9F\xF6\x9F\xDC\x9C\xE1\x83\x20\x96\x86\x9F\x2E\x0A"
#         b"\x20\x20\x20\x20\x20\x2D\x20\xBA\x96\x9C\xF4\xC8\x21\x20\x2D\x20\xF2\xE3\xE1\xDC\xE1"
#         b"\x83\x20\xCB\xE4\x96\x90\xE1\xC8\x20\xAF\x91\xE3\xE1\xF6\xE2\xF4\xE0\x2C\x20\xF4\x20"
#         b"\x20\xBA\x96\x9C\xF4\xC8\x20\x20\xDC\xE1\xC7\x96\xE4\xF4\x83\x2C\x20\x20\xE0\xE4\x9F"
#         b"\x20\x20\xE5\x20\x20\xC8\x96\x86\x9F\x20\x20\xC8\xE1\x0A")

text = sys.stdin.buffer.read()
text_set = set(text)

lang = "".join(
    ['h', 'ж', 'y', 'Z', 'V', 'E', ';', 'А', 'л', '!', 'Д', 'ы', 'N', 'c', 'O', 'J', 'э', '1', 'e', ' ', 'j', 'В', 'o',
     'Х', 'F', 'B', '7', 'x', 'Y', 'Е', '(', 'у', 'я', 'X', 'w', 'C', 'ч', '4', 'Н', '-', 'H', '0', 'f', 'ш', '.', 'b',
     'д', '2', 'q', 'U', 'О', 'к', 'Ш', 'р', ')', 'П', 'Л', 'k', 'z', 'н', 'с', '8', 'a', 'R', 'D', 't', 'm', 'а', 'P',
     '\n', 'Ж', 'T', 'W', 'С', 'Т', ':', 'Ц', 'п', 'L', 'p', ',', 'K', 'M', 'v', 'и', 'о', 'd', 'З', '9', 'g', 'n', 'е',
     'Р', 'У', 'Я', '"', 'т', "'", 'г', 'I', '5', 'ъ', 'щ', 'м', 'ф', 'i', '3', 'М', 'И', 'Q', 'Ю', 'в', 'з', 'Б', 'ю',
     'х', 'б', 'ц', 'Щ', '6', 'Ч', 's', 'A', 'й', 'u', 'l', 'Ф', 'К', 'Г', 'ь', 'r', 'Э', '?', 'S'])

target_word = "Левин"
encodings = ['koi8_r', 'cp1251', 'cp866', 'mac_cyrillic', 'iso8859_5', 'cp855']
encoding_pairs = list(itertools.permutations(encodings, 2))
enc_dict = {lang.encode(enc): [enc] for enc in encodings}


prev_length = 0
while prev_length != len(enc_dict):
    prev_length = len(enc_dict)
    prev_dict = enc_dict.copy()
    for key in prev_dict:
        for dec, enc in encoding_pairs:
            try:
                newkey = key.decode(dec).encode(enc)
                if newkey not in enc_dict.keys():
                    enc_dict[newkey] = prev_dict[key] + [dec, enc]
            except Exception:
                continue

for key in enc_dict:
    if text_set.issubset(set(key)):
        encode = 0
        tmp_text = text
        for codec in reversed(enc_dict[key]):
            tmp_text = tmp_text.encode(codec) if encode else tmp_text.decode(codec)
            encode = (encode + 1) % 2
        if target_word in tmp_text:
            print(tmp_text)
            exit(0)
    else:
        continue
