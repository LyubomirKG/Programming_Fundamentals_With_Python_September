# Read three integers from the input
num1 = int(input())
num2 = int(input())
num3 = int(input())

largest = 0

# Check if num1 is the largest
if num1 >= num2 and num1 >= num3:
    largest = num1
# Check if num2 is the largest
elif num2 >= num1 and num2 >= num3:
    largest = num2
# If neither, then num3 must be the largest
else:
    largest = num3

# Print the result
print(largest)
