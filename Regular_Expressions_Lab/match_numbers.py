import re

text = input()

pattern = r"(^|(?<=\s))-?(0|[1-9]\d*)(\.\d+)?(?=$|\s)"

matches = re.finditer(pattern, text)

numbers = [m.group().strip() for m in matches]

print(" ".join(numbers))
