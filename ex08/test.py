import numpy as np
from vect_cost import cost_
from prediction import predict_


X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(" Example 1:")
print(cost_(X, Y))

print("Example 2:")
print(cost_(X, X))
