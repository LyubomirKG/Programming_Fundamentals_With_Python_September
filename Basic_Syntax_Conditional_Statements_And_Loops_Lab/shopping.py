# Read the initial budget
budget = int(input())
total_price = 0

while True:
    command = input()

    # Check for exit command
    if command == 'End':
        print('You bought everything needed.')
        break

    # Convert the command (string) to an integer price
    price = int(command)

    # Validate if the price exceeds the remaining budget
    if total_price + price > budget:
        print('You went in overdraft!')
        break

    # Accumulate the total cost
    total_price += price
