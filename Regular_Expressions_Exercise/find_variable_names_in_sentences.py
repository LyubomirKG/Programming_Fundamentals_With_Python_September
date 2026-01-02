import re

variables = []

while True:
    try:
        line = input()
        if line == "":
            continue
        # Find variable names that start with '_' and followed by letters/digits
        matches = re.findall(r'\b_([A-Za-z0-9]+)\b', line)
        variables.extend(matches)
    except EOFError:
        break

print(",".join(variables))
