import ast
import keyword
import numpy as np


def build_tree_from_file(filename):
    f = open(filename, "r", encoding="utf-8")
    s = f.read()
    tree = ast.parse(s)
    return tree


class ASTListener (ast.NodeVisitor):
    curr_level = 0
    curr_parent = None
    max_depth_ast_node = 0
    ast_node_bigrams_terms_set = set()
    ast_node_bigrams_terms = []
    ast_node_bigrams_counts = []

    ast_node_types_counts = dict()
    ast_node_types_tfidf = dict()
    ast_node_type_avg_dep = dict()

    keywords = dict()

    code_in_ast_leaves_terms_counts = dict()
    code_in_ast_leaves_terms_tfidf = dict()
    code_in_ast_leaves_avg_dep = dict()

    def __init__(self):
        super()
        self.keywords = {k: 0 for k in keyword.kwlist}

    def visit(self, node):
        node.level = self.curr_level
        self.curr_level += 1

        # check and save max tree depth
        if self.max_depth_ast_node < node.level:
            self.max_depth_ast_node = node.level

        if len(list(ast.iter_child_nodes(node))) > 0:
            # node has children
            class_name = str(node.__class__).split(".")[-1][:-2]
            # update counts and levels
            if class_name not in self.ast_node_types_counts:
                self.ast_node_types_counts[class_name] = 1
                self.ast_node_type_avg_dep[class_name] = [node.level]
            else:
                self.ast_node_types_counts[class_name] += 1
                self.ast_node_type_avg_dep[class_name].append(node.level)
        else:
            code = ast.dump(node).split("(")[1].replace(")", "")
            if len(code) == 0:
                code = ast.dump(node).replace("()", "")
            print(code)

        """print(keyword.kwlist)
        if isinstance(node, ast.If):
            print(node.value)"""


        self.generic_visit(node)
        self.curr_level -= 1

    def finish(self):
        print("Types count:", self.ast_node_types_counts)
        for key in self.ast_node_type_avg_dep.keys():
            self.ast_node_type_avg_dep[key] = np.mean(self.ast_node_type_avg_dep[key])
        print("Avg node depth:", self.ast_node_type_avg_dep)
        print("Max depth:", self.max_depth_ast_node)

    def get_attrs(self):
        return None


# tree = build_tree_from_file("C:/Users/jonat/Documents/School/Uvod v raziskovanje 2/code-profiling/code/batch-1/vse-naloge-brez-testov/" + "DN3-M-1.py")
tree = ast.parse("if a == False:"
                 "    a = 4 + 2")
ast_listener = ASTListener()
ast_listener.visit(tree)
ast_listener.finish()
ast_listener.get_attrs()

