import numpy as np
from tools import add_intercept

print("Example 1 :")

x = np.arange(1, 6)
print(add_intercept(x))


print("Example 2 :")
y = np.arange(1, 10).reshape((3, 3))
print(add_intercept(y))
