import math
a = int(input("Enter first number: "))
x = int(input("Enter second number: "))
c = (((a ** 2) * x) ** (1 / 6)) + math.sqrt(x)
d = x ** (1 / 3) + a ** (1 / 3)
e = x ** (1 / 6)
b = (c / d + e) ** 3
f = 4 * (x + 1)
k = ((x * math.sqrt(x)) ** (1 / 3) + 1) ** 2
result = b + f + k
print("My result: ", result)
print("Expected result for a = 1, x = 4: ", 45)
