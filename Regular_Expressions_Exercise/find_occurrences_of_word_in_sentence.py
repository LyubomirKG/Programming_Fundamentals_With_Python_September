import re

# Read input
text = input()
word = input()

# Create a regex pattern with word boundaries (\b) for the word
pattern = rf'\b{re.escape(word)}\b'

# Find all matches ignoring case
matches = re.findall(pattern, text, re.IGNORECASE)

# Print the count
print(len(matches))
