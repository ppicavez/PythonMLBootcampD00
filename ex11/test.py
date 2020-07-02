import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt
from other_costs import mse_, rmse_, mae_, r2score_

# Example 1:
x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])

# Mean squared error
# your implementation
print("My MSE")
print(mse_(x, y))
print("sklearn MSE")
print(mean_squared_error(x, y))

# Root mean squared error
# your implementation
print("My RMSE")
print(rmse_(x, y))
# sklearn implementation not available: take the square root of MSE
print("sklearn MSE")
print(sqrt(mean_squared_error(x, y)))

# Mean absolute error
# your implementation
print("My MAE")
print(mae_(x, y))
# sklearn implementation
print("sklearn MAE")
print(mean_absolute_error(x, y))

# R2-score
# your implementation
print("My R2-Score")
print(r2score_(x, y))
# sklearn implementation
print("sklearn R2-Score")
print(r2_score(x, y))
