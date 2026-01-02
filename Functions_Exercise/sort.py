# Read input numbers and split them
numbers = input().split()

# Convert input strings to integers
numbers = map(int, numbers)

# Sort the numbers in ascending order
sorted_numbers = sorted(numbers)

# Print the sorted list
print(sorted_numbers)
