# Read the input
times = list(map(int, input().split()))

# Get the middle index
middle = len(times) // 2

# Split times for each racer
left_racer_times = times[:middle]
right_racer_times = times[-1:middle:-1]  # from end to just after middle, reversed

def calculate_time(steps):
    total_time = 0
    for time in steps:
        total_time += time
        if time == 0:
            total_time *= 0.8  # Apply 20% reduction
    return total_time

# Calculate times
left_time = calculate_time(left_racer_times)
right_time = calculate_time(right_racer_times)

# Determine winner
if left_time < right_time:
    winner = "left"
    total = left_time
else:
    winner = "right"
    total = right_time
