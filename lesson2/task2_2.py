import math

def f1(x):
    return 2 * x + 6 - 3 * ((x + 3) ** (2 / 3))

def f2(x):
    return x ** 2 + (math.cos(x + 1)) ** 2 + 2 * x

def f3(x):
    return (f1(x) + f2(x)) / 2

a = 1
b = 4

def f(x):
    if x < a:
        return f1(x) - f1(a)
    elif x <= b:
        return f2(x) - f2(a)
    else:
        return f3(x) - f3(b) + f2(b) - f2(a)

x1 = -0.5  # лівий кінець відрізка зміни x
x2 = 5.5 # правий кінець відрізка зміни x
for i in range(11):
    x = x1 + i * (x2 - x1) / 10
    print('\t', round(x,4), '\t', round(f(x),4))
