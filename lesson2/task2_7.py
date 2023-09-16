import sys
import math

A = float(input("A = "))
B = float(input("B = "))
eps = 0.00001 # похибка обчислення кореня
dig = len(str(int(1 / eps))) # кількість десяткових цифр для округлення результату
def F(x):
    y1 = math.sqrt(x ** 2 - 16) / math.sqrt(x - 3) + math.sqrt(x + 3)
    y2 = 7 / math.sqrt(x - 3)
    return y1 - y2
def PrintAndExit(x):
    print('Корінь =', round(x, dig))
    sys.exit() # дострокове завершення програми

# попердні перевірки
if A >= B:
    print('Потрібно, щоб було A<B.')
    sys.exit() # дострокове завершення програми
if F(A) * F(B) > 0:
    print("На відрізку [A,B] корінь повинен бути локалізований.")
    sys.exit() # дострокове завершення програми
if F(A) == 0: PrintAndExit(A)
if F(B) == 0: PrintAndExit(B)
# початок алгоритму половинного ділення
a = A; fl = F(a)
b = B; fr = F(b)
while b - a > eps:
    x = (a + b) / 2
    f = F(x)
    if fl * f < 0:
        b = x
        fr = F(b)
    elif fr * f < 0:
        a = x
        fl = F(x)
    else: # точно потрапили в корінь
        PrintAndExit(x)
# друк результату
x = (a + b) / 2
PrintAndExit(x)
