# Function that combines adding and subtracting
def add_and_subtract(first, second, third):
    # Pass the first two numbers to the sum function
    sum_result = sum_numbers(first, second)
    # Pass the result and the third number to the subtract function
    final_result = subtract(sum_result, third)
    return final_result

# Function for adding two numbers
def sum_numbers(n1, n2):
    return n1 + n2

# Function for subtracting the third number from the sum
def subtract(sum_val, n3):
    return sum_val - n3

# Input section
first_num = int(input())
second_num = int(input())
third_num = int(input())

# Execute the main function and print result
print(add_and_subtract(first_num, second_num, third_num))
