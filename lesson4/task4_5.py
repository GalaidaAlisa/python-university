import Galaida_package as g
import cmath

print(g.CONST1_1)
print(g.CONST1_2)
print(g.func1_3(1, 4))
print(g.func4_2(20))
g.func1_4()
g.func1_5(complex(1, 2))
print(g.func1_6(-4))
g.func2_2()
print(g.func2_7(5))


g.list_to_file([i for i in range(10)], "lesson4/task4_5.txt")


def f(x):
    return (x - 1) * (x - 3)

print(f"\nHalf division method: ")
print(f"\tRoot of function (x - 1) * (x - 3) on (0, 2) is: {g.half_div(f, 0, 2, 0.0001)}")

