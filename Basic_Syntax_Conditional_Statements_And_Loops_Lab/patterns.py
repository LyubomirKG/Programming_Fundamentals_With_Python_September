# Read the maximum number of stars from the input
n = int(input())

# First part: increasing the number of stars from 1 to n
for i in range(1, n + 1):
    print('*' * i)

# Second part: decreasing the number of stars from n - 1 down to 1
for i in range(n - 1, 0, -1):
    print('*' * i)
