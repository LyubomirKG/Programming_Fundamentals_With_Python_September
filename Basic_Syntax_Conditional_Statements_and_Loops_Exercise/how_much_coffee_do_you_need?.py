# Coffee Intake Tracker based on daily event intensity
coffee_needed = 0
valid_events = ["coding", "dog", "cat", "movie"]

while True:
    command = input()
    
    if command == "END":
        break

    # Normalize command to check against valid events list
    if command.lower() in valid_events:
        # Check intensity: uppercase adds double caffeine
        if command.isupper():
            coffee_needed += 2
        else:
            coffee_needed += 1

# Performance/Health threshold check
if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)
