secret_message = input().split()
result_message = []

for data in secret_message:
    # Extract the numeric part of the word
    first_char = "".join([number for number in data if number.isdigit()])
    # Extract the letters part of the word
    last_char = [char for char in data if not char.isdigit()]
    
    # Swap the first and last letters of the remaining part
    if len(last_char) > 1:
        last_char[0], last_char[-1] = last_char[-1], last_char[0]
    
    # Convert the extracted number into its ASCII character
    first_char = chr(int(first_char))
    
    # Combine the character and the letters back into a word
    result_message += ["".join([first_char] + [*last_char])]

# Print the decoded message joined by spaces
print(*result_message)
