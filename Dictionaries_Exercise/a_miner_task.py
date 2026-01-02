miner_dictionary = {}
counter = 0

while True:
    command = input()
    counter += 1
    
    # Exit condition
    if command == "stop":
        break
        
    # Odd counts represent the resource name
    if counter % 2 != 0:
        resource = command
        if resource not in miner_dictionary:
            miner_dictionary[resource] = 0
    # Even counts represent the quantity of the last resource
    else:
        quantity = int(command)
        miner_dictionary[resource] += quantity

# Iterate through the dictionary and print the results
for resource, quantity in miner_dictionary.items():
    print(f"{resource} -> {quantity}")
