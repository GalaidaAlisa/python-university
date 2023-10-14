import numpy as np

x = np.array([5, -2, 3])
A = np.array([[1, 0, 2], [3, -1, 0], [1, 1, -2]])
B = np.array([[2, 1, 0], [3, 0, 4], [1, -1, -2]])

y = (2 * A + 3 * B.dot(B)).dot(x)
print('(2A+3B^2).x=', y)

z = (A.dot(B) - B.dot(A)).dot(x)
print('(A.B-B.A).x=', z)

u = np.linalg.inv(A).dot(x)
print('A^(-1).x=', u)

print('max(B)=', B.max())