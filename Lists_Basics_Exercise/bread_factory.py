# Read the sequence of events and initialize stats
events = input().split("|")
total_energy = 100
total_coins = 100
bakery_is_open = True

for event in events:
    # Split each event into type and value (e.g., "rest-10")
    event_values = event.split("-")
    event_type, event_value = event_values[0], int(event_values[1])
    
    if event_type == "rest":
        # Energy cannot exceed 100. Calculate actual gained energy.
        initial_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
        
    elif event_type == "order":
        # Orders cost 30 energy but grant coins
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            # If not enough energy, skip the order and recover 50 energy instead
            total_energy += 50
            print("You had to rest!")
            
    else:
        # For all other events, try to buy the ingredient/item
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            # If coins are insufficient, the bakery closes immediately
            bakery_is_open = False
            print(f"Closed! Cannot afford {event_type}.")
            break

# Final summary if the bakery survived the whole day
if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
