import math
import cmath

xr = int(input("Enter real part of complex number: "))
xi = int(input("Enter imaginary part of complex number: "))
x = complex(xr, xi)

a = math.sin(math.cos(3))
b = cmath.cos(2 * x) ** 2
c = 4 * cmath.sin(4 * x)
result = a * b / c
y = complex(round(result.real, 4), round(result.imag, 4))

print(f'y = {y}')
print(f'x + y = {x + y}')
print(f'x * y = {x * y}')
print(f'x / y = {x / y}')
