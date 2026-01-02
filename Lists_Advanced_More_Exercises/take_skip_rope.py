def take_even_number(number: list) -> list:
    """Extracts numbers at even positions to be used as 'take' counts."""
    return list(number[index_even] for index_even in range(len(number)) if index_even % 2 == 0)


def take_odd_number(number: list) -> list:
    """Extracts numbers at odd positions to be used as 'skip' counts."""
    return list(number[index_odd] for index_odd in range(len(number)) if index_odd % 2 != 0)


def non_number_list_pop(number_list: list, index_pop: int):
    """Moves a specific number of characters to the result list and removes them from the source."""
    taken_data.extend(number_list[:index_pop])
    del number_list[:index_pop]
    return taken_data, number_list


# Read the raw message
hidden_message = input()

# Separate digits from non-digit characters
numbers_list = [int(data) for data in hidden_message if data.isdigit()]
non_number_list = [data for data in hidden_message if not data.isdigit()]

taken_data = []

# Generate the take and skip patterns
take_list = take_even_number(numbers_list)
skip_list = take_odd_number(numbers_list)

# Process the message according to the patterns
for index in range(len(take_list)):
    take_index = int(take_list[index])
    skip_index = int(skip_list[index])
    
    # 1. Take a certain number of characters
    taken_string, non_number_list = non_number_list_pop(non_number_list, take_index)
    
    # 2. Skip (delete) a certain number of characters
    del non_number_list[:skip_index]

# Print the decoded message
print("".join(taken_string))
