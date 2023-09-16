import math

suma = 0
for n in range(1, 101):
    suma = suma + (n + 5) / math.factorial(n) * math.sin(2 / (3 ** n))
print('Сума 100 членів =', suma)
