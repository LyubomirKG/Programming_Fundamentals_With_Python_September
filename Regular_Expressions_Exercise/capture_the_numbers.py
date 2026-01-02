import re

numbers = []

while True:
    try:
        line = input()
        if line == "":
            continue
        nums = re.findall(r"\d+", line)
        numbers.extend(nums)
    except EOFError:
        break

print(" ".join(numbers))
