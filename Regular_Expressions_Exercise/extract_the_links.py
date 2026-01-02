import re

# Read input text (multiple lines)
text = []
while True:
    try:
        line = input()
        if not line:
            break
        text.append(line)
    except EOFError:
        break

text = " ".join(text)

# Regex pattern for valid links
pattern = r'\bwww\.[A-Za-z0-9-]+(?:\.[a-z]+)+\b'

# Find all matches
matches = re.findall(pattern, text)

# Print each match on a new line
for link in matches:
    print(link)
