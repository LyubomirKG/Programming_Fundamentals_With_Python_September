group_size = int(input())
days = int(input())

coins = 0
companions = group_size

for day in range(1, days + 1):
    # Every 10th day, 2 companions leave before daily calculations
    if day % 10 == 0:
        companions -= 2

    # Every 15th day, 5 new companions join before daily calculations
    if day % 15 == 0:
        companions += 5

    # Earn 50 coins every day
    coins += 50

    # Food expenses: 2 coins per companion per day
    coins -= 2 * companions

    # Every 3rd day - Motivation party expenses
    if day % 3 == 0:
        coins -= 3 * companions

    # Every 5th day - Slay a monster and earn 20 coins per companion
    if day % 5 == 0:
        coins += 20 * companions
        # Special condition: Additional expenses if it's both 3rd and 5th day
        if day % 3 == 0:
            coins -= 2 * companions

# Calculate the share for each companion (using integer division)
coins_per_companion = coins // companions

print(f"{companions} companions received {coins_per_companion} coins each.")
