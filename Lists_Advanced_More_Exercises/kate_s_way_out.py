def deep_search(maze: list, start: list, memory: list, visited: list):
    # Possible moves: Up, Down, Right, Left
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    visited.append((start[0], start[1]))

    for index_row in range(4):
        row_deep = direction[index_row][0] + start[0]
        col_deep = direction[index_row][1] + start[1]

        # Check grid boundaries
        if 0 <= row_deep < len(maze) and 0 <= col_deep < len(maze[0]):
            # If the path is clear and not visited, add to memory for exploration
            if maze[row_deep][col_deep] != "#" and (row_deep, col_deep) not in visited:
                # Store coordinates and current step count
                memory.insert(0, [row_deep, col_deep, start[2] + 1])

    return memory, visited


rows_in_maze = int(input())
start_point = []
maze_list = []
memory_points = []
visited_out = []
exit_list = []
max_steps = []

# Build the maze and find Kate's starting position 'k'
for row in range(rows_in_maze):
    legend_maze = input()
    maze_list.append(legend_maze)

    if "k" in legend_maze:
        column_kate = legend_maze.index("k")
        start_point = [row, column_kate, 0] # [row, col, steps]

column_maze = len(maze_list[0])

# Check if Kate starts already at an exit
if start_point[0] == 0 or start_point[1] == 0 or \
   start_point[0] == rows_in_maze - 1 or start_point[1] == column_maze - 1:
    exit_list.append([start_point[0], start_point[1], 0])
    max_steps.append(0)

# Main exploration loop
while True:
    memory_points, visited_out = deep_search(maze_list, start_point, memory_points, visited_out)

    if not memory_points:
        break
    
    # Move to the next point in memory
    current_point = memory_points.pop(0)
    start_point[0], start_point[1], start_point[2] = current_point[0], current_point[1], current_point[2]

    # Check if the current point is an exit (edge of the maze)
    if start_point[0] == 0 or start_point[1] == 0 or \
       start_point[0] == rows_in_maze - 1 or start_point[1] == column_maze - 1:
        exit_list.append([start_point[0], start_point[1], start_point[2]])
        max_steps.append(start_point[2])

# Final output based on whether an exit was found
if not exit_list:
    print(f"Kate cannot get out")
else:
    # +1 because the problem usually counts the exit step itself
    print(f"Kate got out in {max(max_steps) + 1} moves")
