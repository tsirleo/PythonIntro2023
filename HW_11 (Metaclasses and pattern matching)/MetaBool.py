class empty(type):
    def __new__(cls, name, bases, dct):
        dct['__bool__'] = lambda self: not any(not bool(value) for value in self.__dict__.values())
        return super().__new__(cls, name, bases, dct)


# class C(metaclass=empty):
#     cfield = 0
#
#     def __init__(self, val=0):
#         self.ofield = val
#
#
# print(not C(), not C(""), not C(123))
