import inspect


class checker(type):
    def __new__(cls, name, bases, namespace):
        annotations = {}
        for field, value in namespace.items():
            if field != '__annotations__' and field in namespace['__annotations__']:
                anno_type = namespace['__annotations__'][field]
                if not isinstance(value, anno_type):
                    raise TypeError(f"Field '{field}' must have type {anno_type}")

                annotations[field] = anno_type

        for field, value in namespace.items():
            if field != '__annotations__' and not field in annotations:
                if isinstance(value, (int, float)):
                    namespace['__annotations__'][field] = type(value)

        return super().__new__(cls, name, bases, namespace)


# class C(metaclass=checker):
#     a: str = "QQ"
#     b = 2
#     s = "QKRQ"
#
#
# print(inspect.get_annotations(C))
#
# try:
#     class E(metaclass=checker):
#         a: str = 1
# except TypeError:
#     print("NOPE")
