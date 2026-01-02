# Read initial gift list
gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    parts = command.split()

    if parts[0] == "OutOfStock":
        gift_to_remove = parts[1]
        # Replace all occurrences with "None"
        gifts = ["None" if gift == gift_to_remove else gift for gift in gifts]

    elif parts[0] == "Required":
        gift = parts[1]
        index = int(parts[2])
        # Replace gift at index if valid
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif parts[0] == "JustInCase":
        gift = parts[1]
        # Replace the last gift
        gifts[-1] = gift

# Remove all "None" entries and print the result
final_gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(final_gifts))
