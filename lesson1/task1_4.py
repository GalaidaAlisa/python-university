import math

for x in range(10):
    result = 2 * x + 6 - 3 * ((x + 3) ** (2 / 3))
    print(f'x = {x}, y = {round(result, 5)}')
