# Read input numbers as a string and split into a list
numbers = input().split()

# Convert each string to float, round it, and store in a new list
rounded_numbers = [round(float(num)) for num in numbers]

# Print the resulting list
print(rounded_numbers)
