import random

def half_div_met(fun, a, b, eps=0.0001):
    if a > b:
        a, b = b, a
    if a == b:
        if fun(a) == 0:
            return f"{a} - корінь"
        else:
            return f"{a} - не корінь"

    fl = fun(a)
    fr = fun(b)

    if fl * fr > 0:
        print('Функція на краях відрізка [A,B] повинна мати різні знаки.')
        return None

    while b - a > eps:
        x = (a + b) / 2
        f = fun(x)
        if fl * f < 0:
            b = x
            fr = fun(b)
        elif fr * f < 0:
            a = x
            fl = fun(x)
        else:  # якщо точно потрапили в корінь
            x = (a + b) / 2
            return x
    return x


def list_to_file(data, file_name):
    n = 10
    my_list = [random.randint(0, 100) for i in range(n)]
    new_list = [random.randint(0, 100) for i in range(n // 2)]
    file = open(file_name, "w")
    for i in range(n):
        if i % 2 == 0:
            my_list[i] = new_list[i // 2]
    file.write("Renewed list: " + str(my_list))

    part1 = my_list[::2]
    part2 = my_list[1::2]
    my_tuple = tuple(zip(part1, part2))
    file.write("My tuple:" + str(my_tuple))

    file.close()

