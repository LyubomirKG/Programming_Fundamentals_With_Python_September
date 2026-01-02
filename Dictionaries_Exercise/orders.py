products_dictionary = {}

while True:
    command = input()
    if command == "buy":
        break
    
    information_about_product = command.split()
    name = information_about_product[0]
    price = float(information_about_product[1])
    quantity = float(information_about_product[2])
    
    # Initialize product data if name is not found [price, total_quantity]
    if name not in products_dictionary.keys():
        products_dictionary[name] = [0, 0]
    
    # Update price (overwrite) and add to the existing quantity
    products_dictionary[name][0] = price
    products_dictionary[name][1] += quantity

# Calculate and print total cost for each product
for product_name, data in products_dictionary.items():
    total_price = data[0] * data[1]
    print(f"{product_name} -> {total_price:.2f}")
