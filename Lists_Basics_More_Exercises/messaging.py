# Read input
numbers_input = input()
text = list(input())  # convert to list for easier char removal

# Convert numbers to list of integers
numbers = numbers_input.split()

message = ''

for number in numbers:
    # Sum the digits of the number
    index = sum(int(digit) for digit in number)

    # Adjust index to wrap around if needed
    index = index % len(text)

    # Append character to message and remove from text
    message += text.pop(index)

# Print the final message
print(message)
