# Read the number of characters to follow
number_of_lines = int(input())
total_sum = 0

# Loop through each line to get a character
for line in range(number_of_lines):
    character = input()
    # Convert character to its ASCII integer value and add to total_sum
    total_sum += ord(character)

# Print the final accumulated sum
print(f"The sum equals: {total_sum}")
