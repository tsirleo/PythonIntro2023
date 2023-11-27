import ast


def normalize_node(node):
    if isinstance(node, ast.Constant):
        return "CONSTANT_" + str(node.value)
    elif isinstance(node, ast.Call):
        return "CALL_" + normalize_node(node.func) + "(" + ", ".join(normalize_node(arg) for arg in node.args) + ")"
    elif isinstance(node, ast.BinOp):
        return "BIN_OP_" + normalize_node(node.op) + "_" + normalize_node(node.left) + "_" + normalize_node(node.right)
    elif isinstance(node, ast.UnaryOp):
        return "UNARY_OP_" + normalize_node(node.op) + "_" + normalize_node(node.operand)
    else:
        return ""


def copypaste(one, two):
    tree_one = "_".join([normalize_node(node) for node in ast.walk(ast.parse(one))])
    tree_two = "_".join([normalize_node(node) for node in ast.walk(ast.parse(two))])
    return tree_one == tree_two


# A = "a=3\nfor i in range(a): print(i*a)"
# B = """# The program
# var = 3  # The variable
# # The comment
# for idx in range(var):
#     print(var * idx)"""
#
# print(copypaste(A, B))
