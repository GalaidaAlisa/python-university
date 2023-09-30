row = input("Enter a row: ")
a = int(input("Enter number of first space: "))
b = int(input("Enter number of second space: "))

list_of_index = []
for i in range(len(row)):
    if row[i] == ' ':
        list_of_index.append(i)

index_left = list_of_index[a - 1]
index_right = list_of_index[b - 1]
print(row[index_left + 1:index_right])
