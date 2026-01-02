def data_types(data_1: str, data_2: str) -> str:
    # If the type is integer, multiply the number by 2
    if data_1 == "int":
        return f"{int(data_2) * 2}"
    # If the type is real, multiply by 1.5 and format to 2nd decimal place
    if data_1 == "real":
        return f"{float(data_2) * 1.5:.2f}"
    # If the type is string, surround it with "$"
    if data_1 == "string":
        return f"${data_2}$"

# Read the command and the data from input
entered_manipulator = input()
entered_data = input()

# Get the result from the function
result = data_types(entered_manipulator, entered_data)

# Print the final result
print(result)
