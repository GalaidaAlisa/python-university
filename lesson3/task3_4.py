def dict_creation():
    my_dict = {}
    for i in range(1, 11):
        my_dict[i] = i ** 2
    return my_dict

print("Dictionary:", dict_creation())
