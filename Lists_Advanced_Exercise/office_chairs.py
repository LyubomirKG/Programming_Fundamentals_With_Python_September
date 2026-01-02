number_of_rooms = int(input())

# Read input for each room into a list
chairs_visitors = [input() for _ in range(number_of_rooms)]
number_of_room = 0
is_need_chairs = False
total_free_chairs = 0

for data in chairs_visitors:
    number_of_room += 1
    chairs, visitors = data.split()
    
    # Calculate the difference between chairs (string length) and visitors
    needed_chairs_in_room = len(chairs) - int(visitors)
    
    if needed_chairs_in_room < 0:
        # If the result is negative, more chairs are needed
        print(f"{abs(needed_chairs_in_room)} more chairs needed in room {number_of_room}")
        is_need_chairs = True

    # Accumulate the total balance of chairs across all rooms
    total_free_chairs += needed_chairs_in_room

# If all rooms have enough chairs, print the total remaining chairs
if not is_need_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
