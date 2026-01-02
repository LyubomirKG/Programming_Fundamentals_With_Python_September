# Number of pourings
n = int(input())
# Maximum capacity of the water tank in liters
capacity = 255
current_liters = 0

for _ in range(n):
    liters = int(input())
    
    # Check if the tank can hold the additional liters
    if current_liters + liters > capacity:
        print("Insufficient capacity!")
    else:
        # Add liters only if they fit
        current_liters += liters

# Output the final amount of water in the tank
print(current_liters)
