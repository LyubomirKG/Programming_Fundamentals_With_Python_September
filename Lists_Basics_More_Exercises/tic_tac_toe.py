# Read the 3x3 board
board = [list(map(int, input().split())) for _ in range(3)]

# Function to check if a player has won
def check_winner(player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check for winner
if check_winner(1):
    print("First player won")
elif check_winner(2):
    print("Second player won")
else:
    print("Draw!")
