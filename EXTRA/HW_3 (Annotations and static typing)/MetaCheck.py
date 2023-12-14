import inspect


class checker(type):
    anno = {}

    def __new__(cls, name, bases, namespace):
        annotations = {}

        if '__annotations__' in namespace:
            for field, value in namespace['__annotations__'].items():
                if field in cls.anno.keys():
                    if value != cls.anno[field]:
                        raise TypeError(f"Field '{field}' must have type {cls.anno[field]}")

            for field, value in namespace.items():
                if field != '__annotations__' and field in namespace['__annotations__']:
                    anno_type = namespace['__annotations__'][field]
                    if not isinstance(value, anno_type):
                        raise TypeError(f"Field '{field}' must have type {anno_type}")

                    annotations[field] = anno_type

            for field, value in namespace.items():
                if not (field.startswith('__') and field.endswith('__')) and field not in annotations \
                        and "function" not in str(value) and not isinstance(value, str):
                    annotations[field] = type(value)
                    namespace['__annotations__'][field] = type(value)

            cls.anno = annotations
        else:
            for field, value in namespace.items():
                if not (field.startswith('__') and field.endswith('__')) and "function" not in str(value):
                    annotations[field] = type(value)

            namespace['__annotations__'] = annotations

        cls.anno = annotations
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
