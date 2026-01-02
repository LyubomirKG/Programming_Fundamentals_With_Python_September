# Read the sequence of fires and the available water
fires = input().split("#")
water = int(input())

# Define fire type valid ranges using a dictionary for cleaner logic
fire_ranges = {
    "High": range(81, 126),
    "Medium": range(51, 81),
    "Low": range(1, 51)
}

effort = 0
total_fire = 0
put_out_cells = []

for fire in fires:
    # Clean up the string and split into type and value
    fire = fire.strip()
    fire_type, value = fire.split(" = ")
    value = int(value)

    # Validate if the fire value is within the allowed range for its type
    if value in fire_ranges.get(fire_type, []):
        # Check if there is enough water to extinguish this cell
        if water >= value:
            water -= value
            effort += value * 0.25 # Effort is 25% of the fire value
            total_fire += value
            put_out_cells.append(value)

# Final report output
print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
