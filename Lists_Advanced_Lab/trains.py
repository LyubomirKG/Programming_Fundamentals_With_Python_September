# Initialize a list of wagons with zeros based on the input count
wagons = [0] * int(input())
add_command = []

while True:
    add_command = input().split()
    # Terminate the program when "End" is received
    if "End" in add_command:
        break
    # Add people to the last wagon
    elif "add" in add_command:
        wagons[-1] += int(add_command[1])
    # Add people to a specific wagon index
    elif "insert" in add_command:
        wagons[int(add_command[1])] += int(add_command[2])
    # Remove people from a specific wagon index
    elif "leave" in add_command:
        wagons[int(add_command[1])] -= int(add_command[2])

# Print the final state of all wagons
print(wagons)
