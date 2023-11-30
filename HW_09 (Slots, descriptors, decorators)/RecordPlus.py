def Record(slots_str, **field_values):
    def decorator(cls):
        for name, value in field_values.items():
            setattr(cls, name, value)

        class WrappedClass(cls):
            __slots__ = sorted(set(cls.__slots__ + slots_str.split()))

            def __iter__(self):
                return iter(sorted(set(self.__slots__ + [_name for _name in dir(cls) if not _name.startswith("_")])))

            def __str__(self):
                parts = []
                for attr in sorted(set(self.__slots__ + [_name for _name in dir(cls) if not _name.startswith("_")])):
                    _value = getattr(self, attr, None)
                    if _value is None:
                        parts.append(attr)
                    else:
                        parts.append(f"{attr}={_value}" if attr in self.__slots__ else f"{attr}:{_value}")
                return "|".join(parts)

        return WrappedClass

    return decorator


# @Record("b c", d=11, e=12)
# class C:
#     __slots__ = ["a", "b"]
#     c = 8
#     d = 9
#
#
# c = C()
# c.a, c.c = 42, 100500
# print(c, "//", "".join(c.__slots__))
# print(*(getattr(c, attr, "<NOPE>") for attr in c))
# for i, attr in enumerate(c):
#     try:
#         setattr(c, attr, i)
#     except AttributeError:
#         pass
# print(c, "//", *(getattr(c, attr, "<NOPE>") for attr in c))
