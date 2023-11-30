class positioned(type):
    def __new__(cls, name, bases, dct):
        annotations = dct.get("__annotations__", {})

        def custom_str(self):
            return ' '.join(f'{field}={getattr(self, field)}' for field in annotations)

        def custom_init(self, *args, **kwargs):
            for field, value in zip(annotations, args):
                setattr(self, field, value)

        dct['__match_args__'] = tuple(annotations.keys())
        dct['__str__'] = custom_str
        dct['__init__'] = custom_init

        return super().__new__(cls, name, bases, dct)


# class C(metaclass=positioned):
#     a: int = 1
#     b: float = 42.0
#
#
# for c in C(), C(4), C(100.0, 500), C(7, 2):
#     print(c)
#     match c:
#         case C(1):
#             print("C1", c.b)
#         case C(b=42):
#             print("C42", c.a)
#         case C(100, 500):
#             print("C100500")
#         case C():
#             print("C", c)
