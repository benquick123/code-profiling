import pickle
from sklearn.model_selection import cross_val_score, GroupKFold
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from collections import Counter
from scipy import sparse


def pickle_load():
    path = "../research-code/pickle-data/"
    f = open(path + "batch-2-ast-X.pickle", "rb")
    X1 = pickle.load(f)
    f.close()
    f = open(path + "batch-2-layout-X.pickle", "rb")
    X2 = pickle.load(f)
    f.close()
    f = open(path + "batch-2-lexical-X.pickle", "rb")
    X3 = pickle.load(f)
    f.close()
    X = sparse.hstack([X1, X2, X3])
    f = open(path + "batch-2-ast-Y.pickle", "rb")
    Y = pickle.load(f)
    f.close()
    f = open(path + "batch-2-ast-groups.pickle", "rb")
    groups = pickle.load(f)
    f.close()
    return X, Y, groups


if __name__ == "__main__":
    model = RandomForestClassifier(n_estimators=500, max_features=None, n_jobs=3, verbose=5)
    cv = GroupKFold(n_splits=10)
    X, Y, groups = pickle_load()

    print(X.shape)
    print(Counter(Y))

    scores = cross_val_score(estimator=model, X=X, y=Y, cv=cv, groups=groups, verbose=5)
    print("avg score:", np.mean(scores), "(+/-", np.std(scores), ")")
    print("majority:", Counter(Y)[0] / len(Y))
    exit()
