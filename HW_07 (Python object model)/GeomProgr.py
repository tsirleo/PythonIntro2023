class Geom:
    def __init__(self, base, denominator):
        self.base = base
        self.denominator = denominator

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        result = self.base * (self.denominator ** self.index)
        self.index += 1
        return result

    def generator(self, start=0, step=1, stop=0):
        _index = start
        while True:
            yield self.base * (self.denominator ** _index)
            _index += step
            if _index < stop and step < 0 or _index >= stop and stop:
                break

    def __getitem__(self, item):
        if isinstance(item, slice):
            start, stop, step = item.start, item.stop, item.step
            if start is None and stop is None and step is None:
                return self.generator()
            elif start is None and stop is None and step < 0:
                return []
            if start is None:
                start = 0
            if step is None:
                step = 1
            if stop is None or stop is Ellipsis:
                return self.generator(start, step)
            return self.generator(start, step, stop)
        elif item is Ellipsis:
            return self.generator()
        elif isinstance(item, tuple):
            if item[0] is Ellipsis:
                return self.generator(stop=item[1])
            elif len(item) == 2 and item[1] is Ellipsis:
                return self.generator(start=item[0])
            else:
                return self.generator(start=item[0], stop=item[2])
        else:
            if item < 0:
                return None
            else:
                return self.base * (self.denominator ** item)

    def __str__(self):
        return f"(base: {self.base}, denominator: {self.denominator})"


# g = Geom(3, 2)
# print(*zip("012345", g))
# print(*g[:6])
# print(*g[10::-2])
# print(*zip(g[...], "0123"))
# print(*g[3, ..., 11])
# print(*zip("012345", g[::]))
# print(*zip("012345", g[:]))
# print(*g[..., 11])
# print(*zip(g[20, ...], "0123"))
