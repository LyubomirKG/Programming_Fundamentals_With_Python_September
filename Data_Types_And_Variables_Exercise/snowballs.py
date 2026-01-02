# Read the number of snowballs
n = int(input())

# Variables to store the best snowball data
max_value = 0
best_weight = 0
best_time = 0
best_quality = 0

# Loop through each snowball to calculate its value
for _ in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())

    # Formula for snowball value: (weight / time) ^ quality
    value = (weight // time) ** quality

    # Check if the current snowball is the best one so far
    if value > max_value:
        max_value = value
        best_weight = weight
        best_time = time
        best_quality = quality

# Print the result in the required format
print(f"{best_weight} : {best_time} = {max_value} ({best_quality})")
