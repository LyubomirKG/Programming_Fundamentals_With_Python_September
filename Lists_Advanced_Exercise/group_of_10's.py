# Read the sequence and convert to a list of integers
sequence_of_numbers = list(map(int, input().split(", ")))
group = 0

# Continue as long as there are numbers in the sequence
while sequence_of_numbers:
    group += 10
    # Filter numbers that belong to the current group (e.g., <= 10, <= 20)
    list_of_groups = [number for number in sequence_of_numbers if number <= group]
    # Remove the grouped numbers from the main sequence
    sequence_of_numbers = [number for number in sequence_of_numbers if number > group]
    
    # Print the result for the current group
    print(f"Group of {group}'s: {list_of_groups}")
