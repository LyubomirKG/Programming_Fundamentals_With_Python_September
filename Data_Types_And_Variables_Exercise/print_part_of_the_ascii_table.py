# Read start and end indices
start_index = int(input())
end_index = int(input())

# Loop through the ASCII codes and print their characters
for i in range(start_index, end_index + 1):
    print(chr(i), end=' ')
