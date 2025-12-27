# Production and Resource Management Simulation
budget = float(input())
flour_price_kg = float(input())

# Calculating ingredient prices based on flour price
eggs_pack_price = flour_price_kg * 0.75
milk_liter_price = flour_price_kg * 1.25
milk_needed_price = milk_liter_price * 0.25 # Only 250ml per loaf

cost_per_bread = flour_price_kg + eggs_pack_price + milk_needed_price

bread_count = 0
colored_eggs_count = 0

# Simulating the baking process
while budget >= cost_per_bread:
    budget -= cost_per_bread
    bread_count += 1
    colored_eggs_count += 3

    # Penalty logic every 3rd bread produced
    if bread_count % 3 == 0:
        lost_eggs = bread_count - 2
        colored_eggs_count -= lost_eggs

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
