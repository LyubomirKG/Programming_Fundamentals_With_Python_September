def is_valid_index(index, lst):
    return 0 <= index < len(lst)

def is_valid_count(count, lst):
    return 0 <= count <= len(lst)

def exchange(lst, index):
    if not is_valid_index(index, lst):
        print("Invalid index")
        return lst
    return lst[index + 1:] + lst[:index + 1]

def find_max_min(lst, even_odd, find_max):
    parity = 0 if even_odd == "even" else 1
    filtered = [num for num in lst if num % 2 == parity]
    if not filtered:
        print("No matches")
        return
    target = max(filtered) if find_max else min(filtered)
    # Find last occurrence of target
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == target:
            print(i)
            return

def get_first_last(lst, count, even_odd, get_first):
    if count > len(lst):
        print("Invalid count")
        return
    parity = 0 if even_odd == "even" else 1
    filtered = [num for num in lst if num % 2 == parity]
    result = filtered[:count] if get_first else filtered[-count:]
    print(result)

# Input and processing
numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    tokens = command.split()
    cmd_type = tokens[0]

    if cmd_type == "exchange":
        index = int(tokens[1])
        numbers = exchange(numbers, index)

    elif cmd_type in ["max", "min"]:
        even_odd = tokens[1]
        find_max_min(numbers, even_odd, find_max=(cmd_type == "max"))

    elif cmd_type in ["first", "last"]:
        count = int(tokens[1])
        even_odd = tokens[2]
        get_first_last(numbers, count, even_odd, get_first=(cmd_type == "first"))

# Final list output
print(numbers)
