import random

n = 10
my_list = [random.randint(0, 100) for i in range(n)]
print("My list:", my_list)
new_list = [random.randint(0, 100) for i in range(n // 2)]
print("New list:", new_list)
for i in range(n):
    if i % 2 == 0:
        my_list[i] = new_list[i // 2]
print("Renewed list:", my_list)

part1 = my_list[::2]
part2 = my_list[1::2]
my_tuple = tuple(zip(part1, part2))
print("My tuple:", my_tuple)
