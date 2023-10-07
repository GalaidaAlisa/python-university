import numpy as np

n = int(input("Enter number of elements in list: "))

arr = np.random.randint(-5, 5, size=n)
print("Array: ", arr)

min_el = np.min(np.absolute(arr))
print("Minimum element: ", min_el)

arr = np.concatenate((np.zeros(np.sum(arr == 0), dtype = int), arr[arr != 0]))
print("Wanted array: ", arr)
