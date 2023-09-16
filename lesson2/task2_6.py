number = int(input("Enter number: "))
n = int(input("Enter a digit you want to add: "))

number_of_digits = len(str(number))
number = number + n * (10 ** number_of_digits)
print("Changed number:", number)
