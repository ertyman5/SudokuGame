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
        row = [0]*9  # create a row with nine zeros
        board.append(row)   # Append the row to the board

    # Fill Diagonal subgrids:
    for i in range(0, 9, 3):
        fill_subgrid(board,i,i)

    return board

def fill_subgrid(board, start_row, start_col):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)
    for i in range(3):
        for j in range(3):
            number = numbers.pop() # Take a number from the suffled list
            board[start_row + i][start_col + j] = number    # board[0,0] = number popped, board[0,1] = next number popped

sudoku_board = generate_board()
for row in sudoku_board:
    print(row)






