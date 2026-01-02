import math

# Read input: total number of people and elevator capacity
N = int(input())  # Number of people
P = int(input())  # Elevator capacity

# Calculate the number of courses needed
# math.ceil() rounds the result up to the nearest integer
courses = math.ceil(N / P)

# Print the final result
print(courses)
