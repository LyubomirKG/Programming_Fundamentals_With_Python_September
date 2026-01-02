# Read the list of integers and the count of numbers to remove
numbers = list(map(int, input().split()))
n = int(input())

# Identify the n smallest numbers by sorting a copy of the list
# We slice [:n] to get exactly the amount we need to eliminate
smallest_numbers = sorted(numbers)[:n]

# Remove the identified smallest numbers from the original list
# Using .remove() ensures we only delete the first occurrence, 
# preserving the relative order of the remaining elements.
for num in smallest_numbers:
    numbers.remove(num)

# Print the remaining numbers joined by a comma and a space
print(", ".join(map(str, numbers)))
