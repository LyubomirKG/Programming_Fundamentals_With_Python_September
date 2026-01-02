# Read two integers and store them in a list
values = [int(input()), int(input())]

# Print values before the swap
print(f"Before:\na = {values[0]}\nb = {values[1]}")

# Swap the elements in the list using tuple unpacking
values[0], values[1] = values[1], values[0]

# Print values after the swap
print(f"After:\na = {values[0]}\nb = {values[1]}")
