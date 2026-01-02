# Read the list of employee happiness levels and the improvement factor
entered_employers = list(map(int, input().split()))
improve_happy = int(input())

# Multiply each employee's happiness by the factor
multiply_happy_employers = [data * improve_happy for data in entered_employers]
total_employers = len(multiply_happy_employers)

# Calculate the average happiness of the entire office
average_happy = sum(multiply_happy_employers) / total_employers

# Filter employees whose happiness is greater than or equal to the average
happy_employer = list(filter(lambda x: x >= average_happy, multiply_happy_employers))
count_happy_employers = len(happy_employer)

# Determine if the office is happy overall (at least 50% must be happy)
if count_happy_employers < (total_employers / 2):
    result = "are not happy!"
else:
    result = "are happy!"

# Print the final score and result
print(f"Score: {count_happy_employers}/{total_employers}. Employees {result}")
