import math


# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    sum = 0.0
    for x in map(lambda y, p: (1 - y) * math.log(1 - p) + y * math.log(p), Y, P):
        sum += x
    return -sum / len(Y)


if __name__ == "__main__":
    true_n90 = [1, 0.5, 0.1, 0, 0, 0, 0, 0, 0, 0.1, 0.5]
    true_p89 = [0.5, 0.1, 0, 0, 0, 0, 0, 0, 0.1, 0.5, 1]
    true_0 = [0, 0, 0, 0.1, 0.5, 1, 0.5, 0.1, 0, 0, 0]

    pred_n90 = [0.8, 0.45, 0.1, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.1, 0.45]
    pred_p89 = [0.45, 0.1, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.1, 0.45, 0.8]
    pred_1 = [0.01, 0.01, 0.01, 0.01, 0.1, 0.45, 0.8, 0.45, 0.1, 0.01, 0.01]
    print(cross_entropy(true_0, pred_1))
    print(cross_entropy(true_0, pred_n90))

    print(cross_entropy(true_p89, pred_n90))
