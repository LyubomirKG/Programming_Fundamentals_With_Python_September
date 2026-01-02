# Read the collection of items and the initial budget
collection_of_items = input().split("|")
budget = float(input())
ticket_price = 150

selling_price_list = []
total_shopping_sum = 0
total_selling_sum = 0

for item in collection_of_items:
    # Parse item type and price
    new_item = item.split("->")
    current_item, current_price = new_item[0], float(new_item[1])
    
    # Check if we can afford the item at all
    if budget < current_price:
        continue
    
    # Validate item price based on specific category limits
    is_valid = False
    if current_item == "Clothes" and current_price <= 50.00:
        is_valid = True
    elif current_item == "Shoes" and current_price <= 35.00:
        is_valid = True
    elif current_item == "Accessories" and current_price <= 20.50:
        is_valid = True
        
    if is_valid:
        # Buy the item and calculate 40% markup for resale
        budget -= current_price
        total_shopping_sum += current_price
        selling_price = current_price * 1.40
        total_selling_sum += selling_price
        selling_price_list.append(f"{selling_price:.2f}")

# Print all new prices formatted to the second decimal
print(" ".join(selling_price_list))

# Calculate and print profit
profit = total_selling_sum - total_shopping_sum
print(f"Profit: {profit:.2f}")

# Update budget with the money from sales and check for ticket affordability
budget += total_selling_sum
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
