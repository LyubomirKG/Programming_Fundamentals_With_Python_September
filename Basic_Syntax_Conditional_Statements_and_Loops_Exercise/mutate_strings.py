first = input()
second = input()

current = list(first)
printed = set()

for i in range(len(first)):
    if current[i] != second[i]:
        current[i] = second[i]
        new_string = ''.join(current)
        if new_string not in printed:
            print(new_string)
            printed.add(new_string)
