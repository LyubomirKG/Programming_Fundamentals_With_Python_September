# Even Numbers Filter: Using for-else loop structure
# The program checks a sequence of numbers and breaks if an odd one is found.
n = int(input())

for _ in range(n):
    number = int(input())

    # Check for the first odd number
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
else:
    # This block executes only if the loop finishes without hitting 'break'
    print("All numbers are even.")
