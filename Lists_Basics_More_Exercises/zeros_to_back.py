# Read input string
input_string = input()

# Split the string into individual elements and convert to integers
numbers = [int(num) for num in input_string.split(', ')]

# Separate non-zero and zero elements
non_zeros = [num for num in numbers if num != 0]
zeros = [num for num in numbers if num == 0]

# Combine the lists: non-zeros first, then zeros
result = non_zeros + zeros

# Print the result
print(result)
