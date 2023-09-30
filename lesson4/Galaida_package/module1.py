import math

a = 140 + 7 / 30 - 138 - 5 / 12
b = 18 + 1 / 6
c = 0.002
TASK_1_1_CONST = (a / b) / c

a = math.sin(math.cos(3))
b = math.cos(2 * math.sqrt(2)) ** 2
c = 4 * math.sin(4 * math.e ** 2)
TASK_1_2_CONST = a * b / c

def task_1_3_func(a, x):
    c = (((a ** 2) * x) ** (1 / 6)) + math.sqrt(x)
    d = x ** (1 / 3) + a ** (1 / 3)
    e = x ** (1 / 6)
    b = (c / d + e) ** 3
    f = 4 * (x + 1)
    k = ((x * math.sqrt(x)) ** (1 / 3) + 1) ** 2
    return b + f + k

def task_4_2_func(n):
    if n == 0:
        return 5
    if n == 1:
        return 1
    if n == 2:
        return -3
    return 3 * task_4_2_func(n - 1) - task_4_2_func(n - 2) + 3 * task_4_2_func(n - 3)

