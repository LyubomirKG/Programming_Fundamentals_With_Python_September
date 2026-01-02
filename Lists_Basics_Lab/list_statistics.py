# Step 1: Read number of integers
n = int(input())

# Step 2: Initialize the lists
positive_numbers = []
negative_numbers = []

# Step 3: Loop through n inputs
for _ in range(n):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

# Step 4: Print the required output
print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
