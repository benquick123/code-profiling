import ast


def read_file(filename):
    f = open(filename, "r", encoding="utf-8")
    s = f.read()
    return s


def build_ast(file_string):
    tree = ast.parse(file_string)
    print(tree)
    for node in ast.walk(tree):
        print(node)
    input()


def str_node(node):
    if isinstance(node, ast.AST):
        fields = [(name, str_node(val)) for name, val in ast.iter_fields(node) if name not in ('left', 'right')]
        rv = '%s(%s' % (node.__class__.__name__, ', '.join('%s=%s' % field for field in fields))
        return rv + ')'
    else:
        return repr(node)


def ast_visit(node, level=0):
    print('  ' * level + str_node(node))
    for field, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    ast_visit(item, level=level+1)
        elif isinstance(value, ast.AST):
            ast_visit(value, level=level+1)


s = read_file("C:/Users/jonat/Documents/School/Uvod v raziskovanje 2/code-profiling/code/batch-1/vse-naloge-brez-testov/" + "DN3-M-1.py")
# ast_visit("a = 5 + 3")
build_ast(s)

