from inspect import getmembers, ismethod, signature
import numbers


def dumper(cls):
    class DumpedClass(cls):
        def __str__(self):
            attributes = []
            for name, value in getmembers(self):
                if not name.startswith("_"):
                    if isinstance(value, numbers.Number) or isinstance(value, str):
                        attributes.append(f"{name}={value}")
                    elif ismethod(value):
                        sig = signature(value)
                        params = ', '.join(str(param) for param in sig.parameters.values() if param.name != 'self')
                        attributes.append(f"{name}({params})")
                    else:
                        attributes.append(f"{name}: {type(value).__name__}")
            return "; ".join(attributes)
    return DumpedClass


# @dumper
# class C:
#     a = 1
#     def __init__(self):
#         self.b = "QQ"
#         self.c = [1,2,3]
#     def foo(self, d):
#         pass
# print(C())
