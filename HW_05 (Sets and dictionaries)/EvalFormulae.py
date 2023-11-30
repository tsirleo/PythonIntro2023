def extract_variables(source):
    for ch in [chr(i) for i in range(33, 64)]:
        source = source.replace(ch, ' ')
    return sorted(set(source.split()))


def evalform(formula, *args):
    var_dict = {var: val for var, val in zip(extract_variables(formula), args)}
    return eval(formula, var_dict)


# import math
# print(evalform("b*2 + a*3 + b//3 + c", 11, 3, 2))
# print(*evalform("f(x)", sorted, "blahblah"))
# print(sum(evalform("f(x) >> (g(f(x))-3)", math.factorial, int.bit_length, i) for i in range(10,200)))
