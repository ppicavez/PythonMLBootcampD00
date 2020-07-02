import matplotlib.pyplot as plt
import numpy as np


def cost_(y, y_hat):
    """Computes the mean squared error of two non-empty numpy.ndarray,
    without any for loop. The
    two arrays must have the same dimensions.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    The mean squared error of the two vectors as a float.
    None if y or y_hat are empty numpy.ndarray.
    None if y and y_hat does not share the same dimensions.
    Raises:
    This function should not raise any Exceptions.
    """

    if y.shape != y_hat.shape:
        return None
    return np.sum(np.power(y_hat - y, 2) / (2 * y.shape[0]))


def plot_with_cost(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exception.
    """
    y_hat = np.dot(np.c_[np.ones((len(x), 1)), x], theta)
    cost = cost_(y, y_hat) * 2
    plt.plot(x, y, 'o')
    plt.plot(x, y_hat)
    i = 0
    while i < len(x):
        plt.plot([x[i], x[i]], [y[i], y_hat[i]], 'r--')
        i = i + 1
    plt.title("Cost : {}".format(cost))
    plt.show()
