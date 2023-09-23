row = input("Enter a row: ")
i = int(input("Enter first index: "))
j = int(input("Enter second index: "))

new_row = ""
for x in range(i, j + 1):
    new_row += row[x]
print("New row:", new_row)
