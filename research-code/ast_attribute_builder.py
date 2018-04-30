import ast
import keyword
import numpy as np
import os
import codecs
from math import log
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
        self.num_literals = 0

        self.ast_node_bigrams_counts = dict()

        self.avg_branhing_factor = []

        self.avg_params = []
        self.std_num_params = []

        self.ast_node_types_counts = dict()
        self.ast_node_types_tfidf = dict()
        self.ast_node_type_avg_dep = dict()

        self.code_in_ast_leaves_terms_counts = dict()
        self.code_in_ast_leaves_terms_tfidf = dict()
        self.code_in_ast_leaves_avg_dep = dict()

    def visit(self, node):
        node.level = self.curr_level
        self.curr_level += 1

        self.avg_branhing_factor.append(len(list(ast.iter_child_nodes(node))))

        # check and save max tree depth
        if self.max_depth_ast_node < node.level:
            self.max_depth_ast_node = node.level

        if len(list(ast.iter_child_nodes(node))) > 0:
            self.avg_branhing_factor.append(len(list(ast.iter_child_nodes(node))))
            # node has children
            class_name = str(node.__class__).split(".")[-1][:-2]
            # update counts and levels
            if class_name not in self.ast_node_types_counts:
                self.ast_node_types_counts[class_name] = 1
                self.ast_node_type_avg_dep[class_name] = [node.level]
            else:
                self.ast_node_types_counts[class_name] += 1
                self.ast_node_type_avg_dep[class_name].append(node.level)

            if class_name == "Name":
                self.num_literals += 1
            if class_name == "FunctionDef":
                self.avg_params.append(len(node.args.args))
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

        self.avg_branhing_factor = np.mean(self.avg_branhing_factor)
        # print(self.avg_branhing_factor)
        # print(self.num_literals)
        self.std_num_params = np.std(self.avg_params) if len(self.avg_params) > 0 else 0
        self.avg_params = np.mean(self.avg_params) if len(self.avg_params) > 0 else 0

        # print("Types count:", self.ast_node_types_counts)
        for key in self.ast_node_type_avg_dep.keys():
            self.ast_node_type_avg_dep[key] = np.mean(self.ast_node_type_avg_dep[key])
        # print("Avg node depth:", self.ast_node_type_avg_dep)

        # print("Leaf counts:", self.code_in_ast_leaves_terms_counts)
        for key in self.code_in_ast_leaves_avg_dep.keys():
            self.code_in_ast_leaves_avg_dep[key] = np.mean(self.code_in_ast_leaves_avg_dep[key])
        # print("Avg leaf depth:", self.code_in_ast_leaves_avg_dep)

    def get_attrs(self):
        return self.max_depth_ast_node, self.avg_branhing_factor, self.ast_node_bigrams_counts, self.ast_node_types_counts, self.ast_node_type_avg_dep, self.code_in_ast_leaves_terms_counts, self.code_in_ast_leaves_avg_dep, self.num_literals, self.avg_params, self.std_num_params


def create_attrs(path):
    tree = build_tree_from_file(path)
    if tree is None:
        return 0, 0, dict(), dict(), dict(), dict(), dict(), 0, 0, 0
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


def file_length(file):
    return sum((len(line)) for line in open(file, encoding="utf-8"))


def pickle_save(X, Y, groups):
    path = "../research-code/pickle-data/"
    f = open(path + "batch-2-ast-X.pickle", "wb")
    pickle.dump(X, f)
    f.close()
    f = open(path + "batch-2-ast-Y.pickle", "wb")
    pickle.dump(Y, f)
    f.close()
    f = open(path + "batch-2-ast-groups.pickle", "wb")
    pickle.dump(groups, f)
    f.close()


attrs = []
node_bigrams_keys = set()
node_types_keys = set()
leaf_terms_keys = set()
lenghts = []

for filename in os.listdir("../code/batch-2/vse-naloge-brez-testov"):
    lenghts.append(file_length("../code/batch-2/vse-naloge-brez-testov/" + filename))
    code_attrs = create_attrs("../code/batch-2/vse-naloge-brez-testov/" + filename)
    node_bigrams_keys = node_bigrams_keys.union(code_attrs[2])
    node_types_keys = node_types_keys.union(code_attrs[3])
    leaf_terms_keys = leaf_terms_keys.union(code_attrs[5])
    attrs.append((filename, code_attrs))

attrs = sorted(attrs, key=lambda x: x[0])

Y = []
groups = []
for filename, _ in attrs:
    Y.append(0 if filename.split("-")[1] == "M" else 1)
    groups.append(int(filename.split("-")[-1].split(".")[0]))

node_bigrams_labels = {k: v for k, v in zip(node_bigrams_keys, list(range(len(node_bigrams_keys))))}
node_bigrams_matrix = create_matrix(attrs, node_bigrams_labels, 2)

node_types_labels = {k: v for k, v in zip(node_types_keys, list(range(len(node_types_keys))))}
node_types_matrix = create_matrix(attrs, node_types_labels, 3)
node_types_tfidf_matrix = TfidfTransformer().fit_transform(node_types_matrix)
node_avg_dep_matrix = create_matrix(attrs, node_types_labels, 4)

leaf_terms_labels = {k: v for k, v in zip(leaf_terms_keys, list(range(len(leaf_terms_keys))))}
leaf_terms_matrix = create_matrix(attrs, leaf_terms_labels, 5)
leaf_terms_tfidf_matrix = TfidfTransformer().fit_transform(leaf_terms_matrix)
leaf_avg_dep_matrix = create_matrix(attrs, leaf_terms_labels, 6)

max_depth = np.zeros((len(attrs), 1))
avg_branching_factor = np.zeros((len(attrs), 1))
num_literals = np.zeros((len(attrs), 1))
avg_params = np.zeros((len(attrs), 1))
std_num_params = np.zeros((len(attrs), 1))
for i in range(len(attrs)):
    max_depth[i, 0] = attrs[i][1][0]
    avg_branching_factor[i, 0] = attrs[i][1][1]
    num_literals[i, 0] = log(attrs[i][1][7]/lenghts[i]) if attrs[i][1][7] != 0 else 0
    avg_params[i, 0] = attrs[i][1][8]
    std_num_params[i, 0] = attrs[i][1][9]
max_depth = sparse.csr_matrix(max_depth)
avg_branching_factor = sparse.csr_matrix(avg_branching_factor)
num_literals = sparse.csr_matrix(num_literals)
avg_params = sparse.csr_matrix(avg_params)
std_num_params = sparse.csr_matrix(std_num_params)

X = sparse.hstack([max_depth, avg_branching_factor, node_bigrams_matrix, node_types_matrix, node_types_tfidf_matrix, node_avg_dep_matrix, leaf_terms_matrix, leaf_terms_tfidf_matrix, leaf_avg_dep_matrix, num_literals, avg_params, std_num_params])
print(X.shape)

# only call once
pickle_save(X, Y, groups)

