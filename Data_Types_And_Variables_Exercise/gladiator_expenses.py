# Inputs for lost fights and equipment prices
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

# Counters for broken equipment
broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0

# Loop through every lost fight to check for broken gear
for fight in range(1, lost_fights + 1):
    helmet_broken = False
    sword_broken = False

    # Every second lost fight, the helmet breaks
    if fight % 2 == 0:
        broken_helmet += 1
        helmet_broken = True

    # Every third lost fight, the sword breaks
    if fight % 3 == 0:
        broken_sword += 1
        sword_broken = True

    # If both helmet and sword break in the same fight, the shield breaks
    if helmet_broken and sword_broken:
        broken_shield += 1
        # Every second time the shield breaks, the armor also breaks
        if broken_shield % 2 == 0:
            broken_armor += 1

# Calculate total expenses
total_expenses = (
    broken_helmet * helmet_price +
    broken_sword * sword_price +
    broken_shield * shield_price +
    broken_armor * armor_price
)

# Output formatted to 2 decimal places
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
