def rec(n):
    if n == 0:
        return 5
    if n == 1:
        return 1
    if n == 2:
        return -3
    return 3 * rec(n - 1) - rec(n - 2) + 3 * rec(n - 3)

print(rec(0))
print(rec(1))
print(rec(2))
print(rec(3))
print(rec(20))
