while True:
    number = float(input())

    # Check if the number is within the specified range [1, 100]
    if 1 <= number <= 100:
        print(f'The number {number} is between 1 and 100')
        # Exit the loop once a valid number is provided
        break
