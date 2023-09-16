import random

def check(arr):
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] == 0:
            return True
    return False

n = 20
a = -10
b = 10
my_list = []
for i in range(n):
    my_list.append(random.randint(a, b))
print(my_list)

if check(my_list):
    print("Послідовність має два сусідних наля.")
else:
    print("Послідовність не має два сусідних нуля.")
