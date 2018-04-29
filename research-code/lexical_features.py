"""
    Feature	                Definition	Count
✓   WordUnigramTF	        Term frequency of word unigrams in source code
✓   ln(numkeyword/length)	Log of the number of occurrences of keyword divided by file length in characters, where keyword is one of do, else-if, if, else, switch, for or while
✓   ln(numTernary/length)	Log of the number of ternary operators divided by file length in characters
✓   ln(numTokens/length)	Log of the number of word tokens divided by file length in characters
✓   ln(numComments/length)	Log of the number of comments divided by file length in characters
✓   ln(numLiterals/length)	Log of the number of string, character, and numeric literals divided by file length in characters
✓   ln(numKeywords/length)	Log of the number of unique keywords used divided by file length in characters
✓   ln(numFunctions/length)	Log of the number of functions divided by file length in characters
    ln(numMacros/length)	Log of the number of preprocessor directives divided by file length in characters       DONT NEED THIS SHIET
✓   nestingDepth	        Highest degree to which control statements and loops are nested within each other
✓   branchingFactor	        Branching factor of the tree formed by converting code blocks of files into nodes
✓   avgParams	            The average number of parameters among all functions
✓   stdDevNumParams	        The standard deviation of the number of parameters among all functions
✓   avgLineLength	        The average length of each line
✓   stdDevLineLength	    The standard deviation of the character lengths of each line
"""

from math import log
import os
import pickle
from scipy import sparse


# Vrne število znakov v datoteki (šteje tudi prelome)
def file_length(file):
    return sum((len(line)) for line in open(file, encoding="utf-8"))

# Term frequency of word unigrams in source code
def word_unigram_tf(file):
    import re
    import collections
    unigrams = collections.defaultdict(int)
    for line in open(file, encoding="utf-8"):
        for word in re.split('\W+', line):
            unigrams[word] += 1
    return unigrams

# Number of occurrences of keyword (do, else-if, if, else, switch, for, while)
def num_keyword(file):
    keywords = {"if": 0, "else:": 0, "elif": 0, "with": 0, "try": 0, "for": 0, "while": 0}
    for line in open(file, encoding="utf-8"):
        for word in line.split():
            if word in keywords:
                keywords[word] += 1
    return keywords

# ln(numTernary/length)	Log of the number of ternary operators divided by file length in characters
# Ne rabimo
# Fele: ko že delam, bom implementiral še to. Ne vem, če rabimo, ampak morda so različni ljudje uporabljali različna števila le-teh.

def num_ternary(file):
    f = open(file, encoding="utf-8")
    ternary_count = 0
    for line in file:
        if "if" in line and "else" in line:
            ternary_count += 1
    f.close()
    return ternary_count

# Number of word tokens
def num_tokens(file):
    return sum((len(line.split())) for line in open(file, encoding="utf-8"))

# Number of comments
def num_comments(file):
    comment_count = 0
    for line in open(file, encoding="utf-8"):
        for character in line:
            if character == "#":
                comment_count += 1
                break
    return comment_count

# ln(numLiterals/length)	Log of the number of string, character, and numeric literals divided by file length in characters
# Python tu ni najbolj prijazen...
# Fele: DONE

# Number of unique keywords used
def num_keywords(file):
    keywords = num_keyword(file)
    return sum((bool(keywords[key]) for key in keywords))

# Number of functions
# Tega pri nalogah najbrž ne bomo rabili, ker je število funkcij že vnaprej dano
def num_functions(file):
    return sum("def" in line.split() for line in open(file, encoding="utf-8"))

# ln(numMacros/length)	Log of the number of preprocessor directives divided by file length in characters
# Tega v Pythonu ne rabimo?

# Highest degree to which control statements and loops are nested within each other
#Na to rešitev nisem najbolj ponosen, ampak pomoje naredi svoje
def nesting_depth(file):
    max_depth = 0
    for line in open(file, encoding="utf-8"):
        depth = 0
        for ch in line:
            if ch == " ":
                depth += 1
            else:
                break
        if depth > max_depth and depth % 4 == 0:
            max_depth = depth
    return int(max_depth / 4)

# Branching factor of the tree formed by converting code blocks of files into nodes
# Wat is dis?
# Fele: nevermind, sem implementiral v ast_attribute_builder.py

# avgParams	            The average number of parameters among all functions
# Tudi tukaj se mi ne zdi smiselno pisat funkcije, glede na nalogo...
# Fele: pomojem res ni smiselno, but its done anyway

# stdDevNumParams	    The standard deviation of the number of parameters among all functions
# Enako kot zgoraj
# Fele: enako kot zgoraj

# The average length of each line
def avg_line_lenght(file):
    from statistics import mean
    lines = [len(line) for line in open(file, encoding="utf-8")]
    return mean(lines) if len(lines) > 0 else 0

# The standard deviation of the character lengths of each line
def sd_line_lenght(file):
    from statistics import stdev
    lines = [len(line) for line in open(file, encoding="utf-8")]
    return stdev(lines) if len(lines) > 1 else 0


# Zapis podatkov

def pickle_save(X):
    path = "../research-code/pickle-data/"
    f = open(path + "batch-1-lexical-X.pickle", "wb")
    pickle.dump(X, f)
    f.close()

path = '../code/batch-1/vse-naloge-brez-testov/'
attrs = []

for filename in os.listdir(path):

    file = path + filename

    # Length
    length = file_length(file)

    # Dicts
    unigrams = dict(word_unigram_tf(file))
    keyword = num_keyword(file)

    # Logs
    ternaries = log(num_ternary(file) / length) if num_ternary(file) > 0 else 0
    tokens = log(num_tokens(file) / length) if num_tokens(file) > 0 else 0
    comments = log(num_comments(file) / length) if num_comments(file) > 0 else 0
    keywords = log(num_keywords(file) / length) if num_keywords(file) > 0 else 0
    functions = log(num_functions(file) / length) if num_functions(file) > 0 else 0

    # Misc
    nestingdepth = nesting_depth(file)
    avglinelength = avg_line_lenght(file)
    sdlinelength = sd_line_lenght(file)

    attrs.append((filename, [ternaries, tokens, comments, keywords, functions, nestingdepth, avglinelength, sdlinelength]))
    # ! manjkata "word_unigram_tf" in "num_keyword"

attrs = sorted(attrs, key=lambda x: x[0])
X = None
for filename, attributes in attrs:
    if X is None:
        X = sparse.csr_matrix(attributes)
    else:
        X = sparse.vstack([X, attributes])

pickle_save(X)