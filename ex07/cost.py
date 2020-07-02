import numpy as np


def cost_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (1/2*M)*(y_pred - y)^2 of the cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_elem: numpy.ndarray, a vector of dimension (number of
    the training examples,1).
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """

    if y.shape != y_hat.shape:
        return None
    elems = np.zeros(y.shape)
    for i in range(y.shape[0]):
        elems[i] = (y_hat[i] - y[i]) ** 2 / (y.shape[0] * 2) 
    return elems


def cost_(y, y_hat):
    """
    Description:
    Calculates the value of cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_value : has to be a float.
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
        """

    my_sum = 0
    cost_elem = cost_elem_(y, y_hat)
    for j in cost_elem:
        my_sum = my_sum + j
    return float(my_sum)
