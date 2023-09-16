import math

print('\tfor ... in range')
print('\tx','\t y','\t y**2','\texp(-y)')
print('\t-------------------------------')
for i in range(10, 21):
    x = i * 0.1
    y = x ** 2 + (math.cos(x + 1)) ** 2 + 2 * x
    print('\t', round(x, 2),'\t', round(y, 3),'\t', round(y ** 2, 3),'\t', round(math.exp(-y), 3))
print('\n')

print('\tfor ... in list')
print('\tx','\t y','\t y**2','\texp(-y)')
print('\t-------------------------------')
for i in [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]:
    y = x ** 2 + (math.cos(x + 1)) ** 2 + 2 * x
    print('\t', round(x, 2),'\t', round(y, 3),'\t', round(y ** 2, 3),'\t', round(math.exp(-y), 3))
print('\n')

print('\twhile')
print('\tx','\t y','\t y**2','\texp(-y)')
print('\t-------------------------------')
x = 1.0
while x < 2.1:
    y = x ** 2 + (math.cos(x + 1)) ** 2 + 2 * x
    print('\t', round(x, 2),'\t', round(y, 3),'\t', round(y ** 2, 3),'\t', round(math.exp(-y), 3))
    x += 0.1
