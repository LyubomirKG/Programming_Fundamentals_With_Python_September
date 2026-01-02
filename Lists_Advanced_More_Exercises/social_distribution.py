# Read the initial population wealth and the minimum wealth required
population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
is_not_possible = False

# Iterate through the population to distribute wealth
for _ in range(len(population)):
    # Identify the wealthiest and the poorest person in each step
    wealth_person = max(population)
    wealth_person_index = population.index(wealth_person)
    poor_person = min(population)
    poor_person_index = population.index(poor_person)

    # If the poorest person is below the minimum threshold
    if poor_person < minimum_wealth:
        add_money_to_poor = minimum_wealth - poor_person
        
        # Check if the wealthiest person can afford to give money 
        # while still staying above or at the minimum wealth level
        if wealth_person - add_money_to_poor >= minimum_wealth:
            # Transfer the wealth
            population[poor_person_index] += add_money_to_poor
            population[wealth_person_index] -= add_money_to_poor
        else:
            # If even the richest cannot cover the poorest, distribution fails
            is_not_possible = True
            break

# Final output based on the possibility of distribution
if is_not_possible:
    print("No equal distribution possible")
else:
    print(population)
