import pickle
import numpy as np
from sklearn.metrics import recall_score, precision_score, accuracy_score, roc_auc_score
from matplotlib import pyplot as plt


def load_pickles():
    path = "../research-code/pickle-data/"
    f = open(path + "batch-2-probabilities-500-balanced-10.pickle", "rb")
    probabilities = pickle.load(f)
    f.close()
    f = open(path + "batch-2-ast-Y.pickle", "rb")
    Y = pickle.load(f)
    f.close()
    f = open(path + "batch-2-ast-groups.pickle", "rb")
    groups = pickle.load(f)
    f.close()
    return Y, probabilities.tolist(), groups


def calc_Y_pred(probabilities, threshold=0.5):
    Y_pred = []
    for p in probabilities:
        # y = 0 if p[0] * (2-weight) > p[1] * weight else 1
        y = 1 if p[1] > threshold else 0
        Y_pred.append(y)
    return Y_pred


def get_cumulative_probabilities(probabilities, groups, Y_true):
    Y_group_true = dict()
    Y_group_pred = dict()

    for p, group, y in zip(probabilities, groups, Y_true):
        if group not in Y_group_true:
            Y_group_true[group] = y
            Y_group_pred[group] = []
        Y_group_pred[group].append(p)

    _Y_group_true = []
    _Y_group_pred = []
    for key in Y_group_pred.keys():
        Y_group_pred[key] = np.mean(Y_group_pred[key], axis=0)
        _Y_group_true.append(Y_group_true[key])
        _Y_group_pred.append(Y_group_pred[key])

    return _Y_group_true, _Y_group_pred


def print_results(Y_true, Y_pred, type):
    print("Classification accuracy, ", type, ": ", accuracy_score(Y_true, Y_pred), sep="")
    print("Precision score, ", type, ": ", precision_score(Y_true, Y_pred), sep="")
    print("Recall score, ", type, ": ", recall_score(Y_true, Y_pred), sep="")
    print()
    return accuracy_score(Y_true, Y_pred), precision_score(Y_true, Y_pred), recall_score(Y_true, Y_pred), roc_auc_score(Y_true, Y_pred)


def weight_testing(group_probabilities, Y_group_true, type, graph=True):
    print("----------WEIGHT TESTING----------")
    recalls, precisions, CAs, AUCs = [], [], [], []
    thresholds = list(np.arange(0.01, 1.0, 0.02))
    for threshold in thresholds:
        print("THRESHOLD:", threshold)
        Y_group_pred = calc_Y_pred(group_probabilities, threshold)
        CA, precision, recall, AUC = print_results(Y_group_true, Y_group_pred, type)
        recalls.append(recall)
        precisions.append(precision)
        CAs.append(CA)
        AUCs.append(AUC)

    if graph:
        plt.plot(thresholds, CAs, label="CA")
        plt.plot(thresholds, precisions, label="Precision")
        plt.plot(thresholds, recalls, label="Recall")
        # plt.plot(thresholds, AUCs, label="AUC")
        plt.legend()
        plt.xlim(0.01, 0.99)
        plt.ylim(-0.01)
        plt.xlabel("Threshold")
        plt.ylabel("Value")
        plt.title("Scores at different thresholds")
        plt.show()


if __name__ == "__main__":
    Y_true, probabilities, groups = load_pickles()
    Y_pred = calc_Y_pred(probabilities)
    print("AUC score:", roc_auc_score(Y_true, [p0 for p0, p1 in probabilities]))
    print_results(Y_true, Y_pred, "single")

    Y_group_true, group_probabilities = get_cumulative_probabilities(probabilities, groups, Y_true)
    Y_group_pred = calc_Y_pred(group_probabilities)
    print_results(Y_group_true, Y_group_pred, "group")

    weight_testing(group_probabilities, Y_group_true, "group")

    exit()
