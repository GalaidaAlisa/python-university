import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.linspace(-1, 1, n + 1)
y = np.linspace(-1, 1, n + 1)
[X, Y] = np.meshgrid(x, y)

x0 = -0.75
y0 = -0.75

x1 = -0.75
y1 = 0.5

x2 = 0.0
y2 = 0.5

x3 = 0.75
y3 = -0.5

q1 = X > x1
q2 = Y < y1
q3 = Y < y2 + (y3 - y2) / (x3 - x2) * (X - x2)
q4 = Y > y3
q = q1 & q2 & q3 & q4
B = np.zeros([n + 1, n + 1])
B[np.flipud(q)] = 255

cc = 128
w = 5
B[0:w, :] = cc
B[-w:, :] = cc
B[:, :w] = cc
B[:, -w:] = cc
ext = [-1, 1, -1, 1]
plt.imshow(B, cmap='gray', extent=ext)
plt.savefig('my_image.png', dpi=1000)
plt.show()