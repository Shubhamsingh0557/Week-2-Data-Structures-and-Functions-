#python program that accept user input and print the sum of square of users input:

def sum_of_squares(numbers):
    return sum([x**2 for x in numbers])

# Taking input from user
user_input = input("Enter numbers separated by spaces: ")

# Converting input string to list of integers
number_list = [int(x) for x in user_input.split()]

# Calculating sum of squares
result = sum_of_squares(number_list)

# Displaying the result
print("Sum of squares:", result)
