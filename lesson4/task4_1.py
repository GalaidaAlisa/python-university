import random

n = 10
my_list = [random.randint(0, 100) for i in range(n)]
new_list = [random.randint(0, 100) for i in range(n // 2)]
for i in range(n):
    if i % 2 == 0:
        my_list[i] = new_list[i // 2]

file = open("lesson4/task4_1.txt", "w")
file.write(str(my_list))
file.close()
