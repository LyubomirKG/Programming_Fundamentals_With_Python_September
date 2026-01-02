# Step 1: Read inputs
n = int(input())
search_word = input()

# Step 2: Collect all strings in a list
all_strings = []
for _ in range(n):
    text = input()
    all_strings.append(text)

# Step 3: Filter the list for strings containing the search_word
filtered_strings = [s for s in all_strings if search_word in s]

# Step 4: Print both lists
print(all_strings)
print(filtered_strings)
