# Read input numbers and split them
numbers = input().split()

# Convert input strings to integers
numbers = map(int, numbers)

# Use filter to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print the resulting list
print(even_numbers)
