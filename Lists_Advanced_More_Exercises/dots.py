def largest_connected_dots():
    # Read the number of rows
    n = int(input())
    # Represent the grid as a list of lists
    board = [input().split() for _ in range(n)]
    # Keep track of visited nodes to avoid infinite recursion
    visited = [[False] * len(board[0]) for _ in range(n)]

    def dfs(r, c):
        # Check if the current position is within the grid boundaries
        if r < 0 or r >= n or c < 0 or c >= len(board[0]):
            return 0
        # Check if the node is already visited or is not a dot
        if visited[r][c] or board[r][c] != '.':
            return 0
        
        # Mark the current cell as visited
        visited[r][c] = True
        size = 1
        
        # Explore 4 directions (Down, Up, Right, Left)
        size += dfs(r+1, c)
        size += dfs(r-1, c)
        size += dfs(r, c+1)
        size += dfs(r, c-1)
        return size

    max_dots = 0
    # Iterate through every cell in the grid
    for i in range(n):
        for j in range(len(board[0])):
            # If we find a dot that hasn't been visited, start a new DFS
            if board[i][j] == '.' and not visited[i][j]:
                connected = dfs(i, j)
                # Keep track of the largest component found so far
                max_dots = max(max_dots, connected)

    print(max_dots)

# Example execution
largest_connected_dots()
