# Read the list of money amounts and the number of beggars
money_as_string = input().split(", ")
number_of_beggars = int(input())

# Convert the string list to integers
money_as_integers = [int(money) for money in money_as_string]

beggars_sums = []
start_index = 0

# Distribute the money
for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    
    # Each beggar takes every N-th element, where N is the total number of beggars
    # This simulates a circular distribution (1st, 2nd, 3rd, then back to 1st)
    for index in range(start_index, len(money_as_integers), number_of_beggars):
        current_beggar_sum += money_as_integers[index]
    
    beggars_sums.append(current_beggar_sum)
    start_index += 1

# Print the final distribution list
print(beggars_sums)
