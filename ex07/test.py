import numpy as np
from cost import cost_elem_, cost_
from prediction import predict_


x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
y_hat1 = predict_(x1, theta1)
y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
print("Example 1:")
print(cost_elem_(y1, y_hat1))

print("# Example 2:")
print(cost_(y1, y_hat1))

x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
theta2 = np.array([[0.05], [1.], [1.], [1.]])
y_hat2 = predict_(x2, theta2)
y2 = np.array([[19.], [42.], [67.], [93.]])

print("Example 3:")
print(cost_elem_(y2, y_hat2))

print(" Example 4:")
print(cost_(y2, y_hat2))

x3 = np.array([0, 15, -9, 7, 12, 3, -21])
theta3 = np.array([[0.], [1.]])
y_hat3 = predict_(x3, theta3)
y3 = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
print(" Example 5:")
print(cost_(y3, y_hat3))

print(" Example 6:")
print(cost_(y3, y3))
