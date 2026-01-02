# Read a list of characters separated by comma and space
list_of_characters = input().split(", ")

# Option 1: Using zip and dict (Commented out in your version)
# list_to_ascii = [ord(string) for string in list_of_characters]
# print(dict(zip(list_of_characters, list_to_ascii)))

# Option 2: Using Dictionary Comprehension (Commented out in your version)
# ascii_dictionary = {character: ord(character) for character in list_of_characters}
# print(ascii_dictionary)

# Option 3: Using a classic for-loop to populate the dictionary
ascii_dictionary = {}
for char in list_of_characters:
    # Store the character as key and its ASCII value as value
    ascii_dictionary[char] = ord(char)

# Print the final dictionary
print(ascii_dictionary)
