import ast
import keyword
import numpy as np
import os
import codecs
from scipy import sparse
from sklearn.feature_extraction.text import TfidfTransformer
import pickle


def build_tree_from_file(filename):
    f = codecs.open(filename, "r", "utf-8")
    s = f.read()
    try:
        tree = ast.parse(s, mode="exec", filename=filename)
    except SyntaxError as e:
        print(e)
        return None
    return tree


class ASTListener (ast.NodeVisitor):
    def __init__(self):
        super()
        self.keywords = {k: 0 for k in keyword.kwlist}
        self.curr_level = 0
        self.curr_parent = None
        self.max_depth_ast_node = 0

        self.ast_node_bigrams_counts = dict()

        self.ast_node_types_counts = dict()
        self.ast_node_types_tfidf = dict()
        self.ast_node_type_avg_dep = dict()

        self.code_in_ast_leaves_terms_counts = dict()
        self.code_in_ast_leaves_terms_tfidf = dict()
        self.code_in_ast_leaves_avg_dep = dict()

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

            if code not in self.code_in_ast_leaves_terms_counts:
                self.code_in_ast_leaves_terms_counts[code] = 1
                self.code_in_ast_leaves_avg_dep[code] = [node.level]
            else:
                self.code_in_ast_leaves_terms_counts[code] += 1
                self.code_in_ast_leaves_avg_dep[code].append(node.level)

        prev_parent = self.curr_parent
        self.curr_parent = node

        bigram = "None" if prev_parent is None else str(prev_parent.__class__).split("_ast.")[-1][:-2]
        bigram += "_" + str(self.curr_parent.__class__).split("_ast.")[-1][:-2]
        if bigram not in self.ast_node_bigrams_counts:
            self.ast_node_bigrams_counts[bigram] = 1
        else:
            self.ast_node_bigrams_counts[bigram] += 1

        self.generic_visit(node)
        self.curr_parent = prev_parent
        self.curr_level -= 1

    def finish(self):
        # print("Max depth:", self.max_depth_ast_node)

        # print("Node bigrams:", self.ast_node_bigrams_counts)

        # print("Types count:", self.ast_node_types_counts)
        for key in self.ast_node_type_avg_dep.keys():
            self.ast_node_type_avg_dep[key] = np.mean(self.ast_node_type_avg_dep[key])
        # print("Avg node depth:", self.ast_node_type_avg_dep)

        # print("Leaf counts:", self.code_in_ast_leaves_terms_counts)
        for key in self.code_in_ast_leaves_avg_dep.keys():
            self.code_in_ast_leaves_avg_dep[key] = np.mean(self.code_in_ast_leaves_avg_dep[key])
        # print("Avg leaf depth:", self.code_in_ast_leaves_avg_dep)

    def get_attrs(self):
        return self.max_depth_ast_node, self.ast_node_bigrams_counts, self.ast_node_types_counts, self.ast_node_type_avg_dep, self.code_in_ast_leaves_terms_counts, self.code_in_ast_leaves_avg_dep


def create_attrs(path):
    tree = build_tree_from_file(path)
    if tree is None:
        return 0, dict(), dict(), dict(), dict(), dict()
    ast_listener = ASTListener()
    ast_listener.visit(tree)
    ast_listener.finish()
    attrs = ast_listener.get_attrs()
    # print(attrs)
    return attrs


def create_matrix(data, labels, k):
    matrix = None
    for i in range(len(data)):
        line = np.zeros(len(labels))
        for bigram in data[i][1][k].keys():
            line[labels[bigram]] = data[i][1][k][bigram]
        if matrix is None:
            matrix = sparse.csr_matrix(line)
        else:
            matrix = sparse.vstack([matrix, sparse.csr_matrix(line)])
    return matrix


def pickle_save(X, Y, groups):
    path = "../research-code/pickle-data/"
    f = open(path + "batch-1-ast-X.pickle", "wb")
    pickle.dump(X, f)
    f.close()
    f = open(path + "batch-1-ast-Y.pickle", "wb")
    pickle.dump(Y, f)
    f.close()
    f = open(path + "batch-1-ast-groups.pickle", "wb")
    pickle.dump(groups, f)
    f.close()


attrs = []
node_bigrams_keys = set()
node_types_keys = set()
leaf_terms_keys = set()
for filename in os.listdir("../code/batch-1/vse-naloge-brez-testov"):
    code_attrs = create_attrs("../code/batch-1/vse-naloge-brez-testov/" + filename)
    node_bigrams_keys = node_bigrams_keys.union(code_attrs[1])
    node_types_keys = node_types_keys.union(code_attrs[2])
    leaf_terms_keys = leaf_terms_keys.union(code_attrs[4])
    attrs.append((filename, code_attrs))

attrs = sorted(attrs, key=lambda x: x[0])

Y = []
groups = []
for filename, _ in attrs:
    Y.append(0 if filename.split("-")[1] == "M" else 1)
    groups.append(int(filename.split("-")[-1].split(".")[0]))

node_bigrams_labels = {k: v for k, v in zip(node_bigrams_keys, list(range(len(node_bigrams_keys))))}
node_bigrams_matrix = create_matrix(attrs, node_bigrams_labels, 1)

node_types_labels = {k: v for k, v in zip(node_types_keys, list(range(len(node_types_keys))))}
node_types_matrix = create_matrix(attrs, node_types_labels, 2)
node_types_tfidf_matrix = TfidfTransformer().fit_transform(node_types_matrix)
node_avg_dep_matrix = create_matrix(attrs, node_types_labels, 3)

leaf_terms_labels = {k: v for k, v in zip(leaf_terms_keys, list(range(len(leaf_terms_keys))))}
leaf_terms_matrix = create_matrix(attrs, leaf_terms_labels, 4)
leaf_terms_tfidf_matrix = TfidfTransformer().fit_transform(leaf_terms_matrix)
leaf_avg_dep_matrix = create_matrix(attrs, leaf_terms_labels, 5)

max_depth = np.zeros((len(attrs), 1))
for i in range(len(attrs)):
    max_depth[i, 0] = attrs[i][1][0]
max_depth = sparse.csr_matrix(max_depth)

X = sparse.hstack([max_depth, node_bigrams_matrix, node_types_matrix, node_types_tfidf_matrix, node_avg_dep_matrix, leaf_terms_matrix, leaf_terms_tfidf_matrix, leaf_avg_dep_matrix])

# only call once
pickle_save(X, Y, groups)

