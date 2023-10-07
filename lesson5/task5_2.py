import numpy as np

matrix = np.random.randint(-10, 10, (5, 5))
print("Matrix:\n", matrix)

min_values = np.min(matrix, axis=1)
max_values = np.max(matrix, axis=1)

diag_indeces = np.arange(5)
matrix[diag_indeces, 4 - diag_indeces] = (min_values + max_values) / 2
print("Changed natrix:\n", matrix)

row_sums = np.sum(matrix, axis=1)
max_sum_row_num = np.argmax(row_sums) + 1
max_sum_value = np.max(row_sums)
print(f'Maximum suma: {max_sum_value}, in row {max_sum_row_num}')

print(f'Maximum of minimum values in rows: {np.max(min_values)}')
