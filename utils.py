def create_board():
    """""
    Creates an 8x8 grid for the Game of Life.
    Returns:
        list: An 8x8 grid filled with zeros, representing dead cells
    """
    board = []
    for i in range(8):
        board.append([])
        for j in range(1, 9):
            board[i].append(0)
    return board
def print_board(board):
    """
    Prints the current state of the Game of Life board.
    
    Args:
        board (list of list of int): The Game of Life board to print.
    """
    for row in board:
        print(' '.join(['#' if cell else '.' for cell in row]))
    print()