# Christmas Spirit: Complex Resource Management Algorithm
quantity = int(input())
days_to_christmas = int(input())

total_expenses = 0
total_spirit_points = 0

for current_day in range(1, days_to_christmas + 1):
    # Logistic adjustment: increment quantity
    if current_day % 11 == 0:
        quantity += 2

    # Event: Ornament Set purchase
    if current_day % 2 == 0:
        total_expenses += quantity * 2
        total_spirit_points += 5

    # Event: Tree Skirts and Garlands purchase
    if current_day % 3 == 0:
        total_expenses += quantity * (5 + 3)
        total_spirit_points += 13

    # Event: Tree Lights purchase and synergy bonus
    if current_day % 5 == 0:
        total_expenses += quantity * 15
        total_spirit_points += 17
        if current_day % 3 == 0:
            total_spirit_points += 30

    # Event: Cat's penalty (fixed costs and spirit loss)
    if current_day % 10 == 0:
        total_spirit_points -= 20
        total_expenses += 23  # (5 for skirt + 3 for garland + 15 for lights)

# Final day penalty if applicable
if days_to_christmas % 10 == 0:
    total_spirit_points -= 30

print(f"Total cost: {total_expenses}")
print(f"Total spirit: {total_spirit_points}")
