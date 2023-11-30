class Smile:
    def __init__(self, size):
        self.size = size

    def __abs__(self):
        return abs(self.size)

    def __neg__(self):
        return Smile(-self.size)

    def __add__(self, other):
        return Smile(self.size + other.size)

    def __sub__(self, other):
        return Smile(self.size - other.size)

    def __mul__(self, num):
        return Smile(self.size * num)

    def __str__(self):
        _size = abs(self.size)
        if _size == 0:
            return ""
        elif _size == 1:
            return '/1\\\n|"|\n\\-/'
        else:
            smiley = []
            distance = _size // 4
            mouth_len = (_size * 2 - 1) - (distance + 1) * 2
            smiley.append("/" + str(_size) + ("-" * (_size * 2 - 1 - len(str(_size)))) + "\\")
            for _ in range(_size):
                smiley.append("|" + " " * (_size * 2 - 1) +"|")
            smiley.append("\\" + ("-" * (_size * 2 - 1)) + "/")
            eyes = "|" + (" " * distance) + "O" + (" " * mouth_len) + "O" + (" " * distance) + "|"
            mouth = "|" + (" " * (distance + 1)) + ("-" * mouth_len) + (" " * (distance + 1)) + "|"
            smiley[distance + 1] = eyes if self.size > 0 else mouth
            smiley[_size - distance] = mouth if self.size > 0 else eyes
            return "\n".join(smiley)


# print(abs(Smile(-2)))
# print(Smile(1))
# print(Smile(1) - Smile(4))
# print(-Smile(2) + Smile(-2))
# print(Smile(6) * 3 - Smile(1))
