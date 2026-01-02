# Read names from a single string and split them into a list
entered_names = input().split(", ")

# Sort the names based on two criteria:
# 1. Primary: Length of the name in descending order (-len(x))
# 2. Secondary: Alphabetical order (x)
sorted_names_list = sorted(entered_names, key=lambda x: (-len(x), x))

# Print the sorted list
print(sorted_names_list)
