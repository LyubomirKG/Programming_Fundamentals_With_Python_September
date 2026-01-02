# Read the input list and step
people = input().split()
k = int(input())

# Convert to integers
people = list(map(int, people))

# Output list to store the Josephus order
josephus_order = []

# Start from index 0
index = 0

# Repeat until all are removed
while people:
    # Move (k - 1) steps ahead (since current position counts as 1)
    index = (index + k - 1) % len(people)

    # Remove the person and add to result
    josephus_order.append(people.pop(index))

# Print result in required format
print(f"[{','.join(map(str, josephus_order))}]")
