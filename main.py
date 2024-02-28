# Setup the initial board:
# Value zero corresponds to an empty cell

# Step 2:
# Fill the cells corresponding to the diagonal sub_grids, with random valid numbers. ensuring they don't violate the rules.
# As they are isolated from the rest of the board,it´s easy to make sure they don't interfere with the others.
# This ensures a balanced distribution of numbers across rows, columns and subgrids. Next step is backtracking algorithm
import random


def generate_board():
    board = []
    for _ in range(9):
        row = [0] * 9  # create a row with nine zeros
        board.append(row)  # Append the row to the board

    # Fill Diagonal subgrids:
    for i in range(0, 9, 3):
        fill_subgrid(board, i, i)

    return board


def fill_subgrid(board, start_row, start_col):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)
    for i in range(3):
        for j in range(3):
            number = numbers.pop()  # Take a number from the suffled list
            board[start_row + i][start_col + j] = number  # board[0,0] = number popped, board[0,1] = next number popped


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Sudoku board is already solved

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):     # Function is called recursively to attempt to solve the rest
                return True             # If the function returns True (it's solved) then the function returns True to the function that called originally
            board[row][col] = 0         # BackTrack if the solutions fails
                                        # It will reset the cell to the empty state, then the algorithm tries a different nu,ber in the previous cell, exploring different paths
    return False                        # If the loop exhausts all possible numbers for the current empty cell without finding a solution the functions returns False,
                                        # indicating this path does not lead to a valid solution, triggering backtracking again.


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Returns the spot on the board to insert a number
    return None  # otherwise returns nothing


def is_valid(board, row, col, num):
    # Check if the number is not repeated in the same row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Check if the number is not repeated in the same column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check if the number is not repeated in the same 3x3 subgrid
    # For this part I opted to divide the grid with operator '//', which it divides two numbers and rounds down to the nearest integer.
    start_row = 3 * (
            row // 3)  # This effectively divides the Sudoku board into 3 equal parts vertically, each containing 3 rows.
    start_col = 3 * (
            col // 3)  # Similarly, this divides the Sudoku board into 3 equal parts horizontally, each containing 3 columns.
    # By multiplying by 3, it scales the rows and columns indices back up to the 3x3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


# --RUN--#
sudoku_board = generate_board()
solve_sudoku(sudoku_board)
for row in sudoku_board:
    print(row)
