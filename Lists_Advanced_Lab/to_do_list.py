temp_list = []
entered_notes = []

# Collect commands until "End" is received
while True:
    command = input()
    if "End" in command:
        break
    # Split the input by "-" to separate importance from the note text
    entered_notes.append(command.split("-"))

# Sort the notes based on the importance level (the first element converted to int)
# Note: The loop is not strictly necessary for the sorting logic itself
for index in range(len(entered_notes)):
    temp_list = sorted(entered_notes, key=lambda x: int(x[0]))

# Extract only the text part of the notes after they are sorted
only_text = [data[1] for data in temp_list]

# Print the final ordered list of notes
print(only_text)
