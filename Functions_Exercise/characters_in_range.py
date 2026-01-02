# Function to find all characters between two given symbols
def find_the_symbols(first_symbol, second_symbol, middle):
    # Iterate from the ASCII value of the first symbol + 1 to the second symbol
    for letter in range(ord(first_symbol) + 1, ord(second_symbol)):
        # Convert the ASCII number back to a character and add a space
        middle += chr(letter) + " "
    return middle

# Input section
first_symbol = input()
second_symbol = input()
middle = ""

# Execute and print the result
print(find_the_symbols(first_symbol, second_symbol, middle))
