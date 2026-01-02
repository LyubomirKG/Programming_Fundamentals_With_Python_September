sequence_of_integer = list(map(int, input().split()))
sum_remove_elements = 0

while sequence_of_integer:
    entered_index = int(input())
    
    # Handle index out of bounds (less than zero)
    if entered_index < 0:
        remove_item = sequence_of_integer[0]
        sequence_of_integer[0] = sequence_of_integer[-1]

    # Handle index out of bounds (greater than list length)
    elif entered_index >= len(sequence_of_integer):
        remove_item = sequence_of_integer[-1]
        sequence_of_integer[-1] = sequence_of_integer[0]

    # Handle valid index
    else:
        remove_item = sequence_of_integer.pop(entered_index)

    # Accumulate the sum of removed elements
    sum_remove_elements += remove_item

    # Update all remaining elements in the sequence
    for inx in range(len(sequence_of_integer)):
        if sequence_of_integer[inx] <= remove_item:
            sequence_of_integer[inx] += remove_item
        else:
            sequence_of_integer[inx] -= remove_item

# Print the final sum of all removed elements
print(sum_remove_elements)
