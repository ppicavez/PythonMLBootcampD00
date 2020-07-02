import numpy as np
import math


def mse_(y, y_hat):
    if y.shape != y_hat.shape:
        return None
    return np.mean(np.power(y_hat - y, 2))


def rmse_(y, y_hat):
    return math.sqrt(mse_(y, y_hat))


def mae_(y, y_hat):
    if y.shape != y_hat.shape:
        return None
    return np.mean(np.absolute(y_hat - y))


def r2score_(y, y_hat):
    if y.shape != y_hat.shape:
        return None
    return 1 - (np.sum(np.power(y_hat - y, 2)) /
                (np.sum(np.power(y_hat - np.mean(y), 2))))
