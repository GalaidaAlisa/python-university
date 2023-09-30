file = open("lesson4/task4_1.txt", "r")
new_list = []
for line in file:
    line = line.split(", ")
    line[0] = line[0][1:]
    line[-1] = line[-1][:-1]
    for elem in line:
        elem = int(elem)
        new_list.append(elem)
file.close()

print(new_list)
