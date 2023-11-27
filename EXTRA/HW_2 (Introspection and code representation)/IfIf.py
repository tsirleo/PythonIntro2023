import ast
import sys


def check_syntax(text):
    try:
        ast.parse(text)
        for node in ast.walk(ast.parse(text)):
            if isinstance(node, ast.If):
                return True
        return False
    except SyntaxError:
        return False


print(check_syntax(sys.stdin.read()))
