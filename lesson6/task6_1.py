import numpy as np

a=np.array([1, 4, -2])
b=np.array([1, 1, -1])
c1 = a + b
c2 = 4 * a + 2 * b
dc = c1 / c2
if dc[0] == dc[1] and dc[0] == dc[2]:
    print('Вектори c1 і c2 колінеарні')
else:
    print('Вектори c1 і c2 не колінеарні')

va = np.sqrt(a.dot(a))
vb = np.sqrt(b.dot(b))
print('|a|=', va, '|b|=', vb)

ab = np.dot(a,b) / va / vb
angle = np.arccos(ab)
print(angle * 180 / np.pi) 
