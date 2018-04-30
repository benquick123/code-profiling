import os
from math import log
from scipy import sparse
import pickle


def pickle_save(X):
    path = "../research-code/pickle-data/"
    f = open(path + "batch-2-layout-X.pickle", "wb")
    pickle.dump(X, f)
    f.close()


path = '../code/batch-2/vse-naloge-brez-testov/'
attrs = []

for filename in os.listdir(path):
    f = open(path + filename, encoding="utf-8")
    s = f.read()

    length = len(s)
    num_tabs = s.count("\t")
    num_spaces = s.count(" ")
    num_empty_lines = s.count("\n\n")
    num_new_lines = s.count("\n")
    white_space_ratio = (num_tabs + num_spaces + num_new_lines) / (length - (num_tabs + num_spaces + num_new_lines)) if (length - (num_tabs + num_spaces + num_new_lines)) > 0 else 0
    # new_line_before = NOPE

    num_tabs = log(num_tabs/length) if num_tabs > 0 else 0
    num_spaces = log(num_spaces/length) if num_spaces > 0 else 0
    num_empty_lines = log(num_empty_lines/length) if num_empty_lines > 0 else 0
    tabs_lead_lines = 1 if s.count("\n\t") > s.count("\n ") else -1
    # print(length, num_tabs, num_spaces, num_empty_lines, num_new_lines, white_space_ratio, tabs_lead_lines)
    attrs.append((filename, [length, num_tabs, num_spaces, num_empty_lines, num_new_lines, white_space_ratio, tabs_lead_lines]))

attrs = sorted(attrs, key=lambda x: x[0])
X = None
for filename, attributes in attrs:
    if X is None:
        X = sparse.csr_matrix(attributes)
    else:
        X = sparse.vstack([X, attributes])

pickle_save(X)
