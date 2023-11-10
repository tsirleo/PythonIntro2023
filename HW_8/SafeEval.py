def safeval(expression, _globals=None, _locals=None):
    try:
        return eval(expression, _globals, _locals) if "globals()" not in expression else None
    except NameError:
        return expression
    except Exception as e:
        return e


# print(safeval("1+2"))
# print(safeval("a+b"))
# print(safeval("bin[12]"))
# print(safeval("globals().__delitem__('safeval')"))
# print(safeval("safeval.__name__"))
