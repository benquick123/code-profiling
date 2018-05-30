import pickle
from sklearn.model_selection import cross_val_score, GroupKFold, cross_val_predict
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
    weights = "balanced"
    model = RandomForestClassifier(n_estimators=500, max_features=None, n_jobs=3, verbose=2, class_weight=weights)
    cv = GroupKFold(n_splits=10)
    X, Y, groups = pickle_load()
    # Y = np.random.choice(2, size=len(Y), p=[0.88, 0.12])
    # pickle.dump(Y, open("../research-code/pickle-data/batch-2-ast-Y-random-class.pickle", "wb"))

    # save X, Y and groups to .csv.
    X = X.toarray()
    np.savetxt("X.csv", X, delimiter=",")
    np.savetxt("Y.csv", Y, delimiter=",")
    np.savetxt("groups.csv", groups, delimiter=",")

    # exit
    exit()

    print(X.shape)
    print(Counter(Y))

    # scores = cross_val_score(estimator=model, X=X, y=Y, cv=cv, groups=groups, verbose=5)
    scores = cross_val_predict(estimator=model, X=X, y=Y, cv=cv, groups=groups, verbose=5, method="predict_proba")
    # scores are now probabilities for each class. i save them for later analysis.

    f = open("../research-code/pickle-data/batch-2-probabilities-500-balanced-10.pickle", "wb")
    pickle.dump(scores, f)
    f.close()

    """print("avg score:", np.mean(scores), "(+/-", np.std(scores), ")")
    print("majority:", Counter(Y)[0] / len(Y))"""
    exit()
