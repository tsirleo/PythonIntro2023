import inspect


def annodoc(obj):
    if isinstance(obj, type):
        doc_lines = [f"{obj.__name__}:"]
        if obj.__doc__:
            doc_lines.append(obj.__doc__)

        for name, value in obj.__annotations__.items():
            if isinstance(value, str):
                doc_lines.append(f"Variable {name}: {value}")

        obj.__doc__ = "\n".join(doc_lines)

        for attr_name, attr_value in obj.__dict__.items():
            annodoc(attr_value)

        return obj

    elif callable(obj):
        doc_lines = [f"{obj.__name__}:"]
        if obj.__doc__:
            doc_lines.append(obj.__doc__)

        for name, value in obj.__annotations__.items():
            if isinstance(value, str):
                if name == "return":
                    doc_lines.append(f"Returns: {value}")
                else:
                    doc_lines.append(f"Variable {name}: {value}")

        obj.__doc__ = "\n".join(doc_lines)

        for attr_name, attr_value in obj.__dict__.items():
            if hasattr(attr_value, "__annotations__"):
                annodoc(attr_value)

        return obj


# @annodoc
# class C:
#     """The class"""
#     const: "constant" = 1
#     var: "variable"
#     undoc = 42
#
#     def method(x: "parameter", y: int) -> "return value":
#         return y
#
#
# print(C.__doc__)
# print(C().method.__doc__)
