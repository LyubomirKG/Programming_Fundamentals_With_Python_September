# Read the current version and split it by the dot
previous_version = input().split(".")

# Join the parts into a single string and convert to an integer to increment it
temp_number = int("".join(previous_version))
temp_number += 1

# Convert the new number back to a string and then to a list of characters
next_version = list(str(temp_number))

# Print the result joined by dots
print(".".join(next_version))
