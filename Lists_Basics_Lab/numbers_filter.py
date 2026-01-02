# Read the number of integers to follow
n = int(input())

# Initialize a list to store all input numbers
numbers = []

# Collect each number and append it to the list
for _ in range(n):
    current_number = int(input())
    numbers.append(current_number)

# Read the filtering command and remove potential whitespace
command = input().strip()

# Apply filtering logic based on the received command
filtered = []
if command == "even":
    filtered = [x for x in numbers if x % 2 == 0]
elif command == "odd":
    filtered = [x for x in numbers if x % 2 != 0]
elif command == "positive":
    filtered = [x for x in numbers if x >= 0]
elif command == "negative":
    filtered = [x for x in numbers if x < 0]

# Print the final filtered list
print(filtered)
