import math

def elem(n):
    return ((-1) ** n) / math.factorial(2 * n + 1)

alph = 0.0001
n = 1
a = elem(n)
suma = 0.0
while abs(a) > alph:
    suma += a 
    n += 1
    a = elem(n)
print('Сума ряду =', round(suma, 4))
