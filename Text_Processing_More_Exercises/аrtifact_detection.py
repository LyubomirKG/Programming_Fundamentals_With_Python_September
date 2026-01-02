import re

# Read the raw input containing potential hidden messages
text = input()

# Regex Pattern Breakdown:
# ([*^]+)           - Group 1: Leading symbols (* or ^)
# ([A-Za-z ]{6,})   - Group 2: Artifact name (letters/spaces, min 6 chars)
# ([*^]+)           - Group 3: Trailing symbols (* or ^)
# ([^A-Za-z0-9]*)   - Group 4: Separator (must NOT contain letters or digits)
# (\++(coord)\++)   - Group 5/6: Coordinates wrapped in pluses
pattern = r'([*^]+)([A-Za-z ]{6,})([*^]+)([^A-Za-z0-9]*)(\++([0-9\.\-]+,[0-9\.\-]+)\++)'

# Find all matches in the text
matches = re.finditer(pattern, text)
valid_artifacts = []

for m in matches:
    name = m.group(2)
    separator = m.group(4)
    coordinates = m.group(6)

    # RULE 1: The separator between name and coords cannot have letters/digits
    # This acts as a secondary filter for "corrupted" messages
    if re.search(r'[A-Za-z0-9]', separator):
        continue  

    # RULE 2: Validate coordinate format (signed floats/ints separated by comma)
    # Ensures that coordinates like "12.3.-4" are rejected
    if not re.fullmatch(r'-?\d+(\.\d+)?,-?\d+(\.\d+)?', coordinates):
        continue  

    valid_artifacts.append((name, coordinates))

# Output processing
if valid_artifacts:
    for name, coord in valid_artifacts:
        print(f"Found {name} at coordinates {coord}.")
else:
    print("No valid artifacts found.")
