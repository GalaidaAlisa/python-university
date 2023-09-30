import math
import cmath

def task2_7_func(x):
    y1 = math.sqrt(x ** 2 - 16) / math.sqrt(x - 3) + math.sqrt(x + 3)
    y2 = 7 / math.sqrt(x - 3)
    return y1 - y2

def task1_4_func():
    for x in range(10):
        result = 2 * x + 6 - 3 * ((x + 3) ** (2 / 3))
        print(f'x = {x}, y = {round(result, 5)}')


def task1_5_func(x):
    a = math.sin(math.cos(3))
    b = cmath.cos(2 * x) ** 2
    c = 4 * cmath.sin(4 * x)
    result = a * b / c
    y = complex(round(result.real, 4), round(result.imag, 4))

    print(f'y = {y}')
    print(f'x + y = {x + y}')
    print(f'x * y = {x * y}')
    print(f'x / y = {x / y}')


def task1_6_func(x):
    y = x ** 2 + (math.cos(x + 1)) ** 2 + 2 * x
    return y



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

def task2_2_func(x1 = -0.5, x2 = 5.5):
    for i in range(11):
        x = x1 + i * (x2 - x1) / 10
        print('\t', round(x,4), '\t', round(f(x),4))

