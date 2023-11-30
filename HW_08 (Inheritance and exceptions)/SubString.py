from collections import UserString


class SubString(UserString):
    def __sub__(self, other):
        from collections import Counter
        subtracted_simbols = Counter(other)

        result = []
        for char in self.data:
            if char in subtracted_simbols and subtracted_simbols[char] > 0:
                subtracted_simbols[char] -= 1
            else:
                result.append(char)

        del Counter
        return self.__class__("".join(result))


del UserString

# print(SubString("qwertyerty")-SubString("ttttr"))
