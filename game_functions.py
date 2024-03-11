from utils import create_board, print_board
import logging

logging.basicConfig(filename='game_functions', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def get_user_params(board):
    """
    Interactively populates the game board with living cells based on user input.

    The function repeatedly prompts the user to enter the row and column numbers 
    where they wish to place a living cell, adjusting for 0-indexing internally. 
    Each cell specified by the user is set to '1', representing a living cell. 
    After each input, the user is asked if they wish to continue adding more cells. 
    The loop continues until the user opts not to continue, at which point the 
    function returns the updated game board with all user-specified living cells.

    Args:
        board (list of list of int): The game board, an 8x8 grid, to be populated 
                                     with living cells ('1') based on user inputs.

    Returns:
        list of list of int: The updated game board reflecting the living cells added by the user.
    """
    while True:
        row=int(input('Inter in the row: '))
        col=int(input('Inter in the col: '))
        board[row-1][col-1]=1
        ask = input('Do you want to continue? (yes/no): ')
        if ask.lower() != 'yes':
            break
    return board        



def simulate_round(board):
    """
    Simulate one round of the Game of Life, applying the rules to each cell.

    Args:
        board (list): The current state of the game board.

    Returns:
        The new state of the game board after one round of simulation.
    """   
    new_board = create_board()
    for row in range(8):
        for col in range(8):
            live_neighbors = sum(
                board[row + dx][col + dy]
                for dx in [-1, 0, 1]
                for dy in [-1, 0, 1]
                if 0 <= row + dx < 8 and 0 <= col + dy < 8
                and not (dx == dy == 0)
            )
            # Apply Game of Life rules
            if board[row][col] == 1 and live_neighbors in [2, 3]:
                new_board[row][col] = 1
            elif board[row][col] == 0 and live_neighbors == 3:
                new_board[row][col] = 1
    return new_board

def start_game():
    """
    Start the Game of Life simulation based on user inputs.
    Initializes the board, accepts user inputs for initial living cells, 
    and simulates the specified number of rounds, printing the board state each round.
    """
    board = create_board()
    board = get_user_params(board)
    rounds = int(input('How many rounds do you want to simulate? '))
    for _ in range(rounds):
        print("Next Round:")
        board = simulate_round(board)
        print_board(board)

if __name__ == '__main__':
    start_game()
