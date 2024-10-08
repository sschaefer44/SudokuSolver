import os

def print_board(gameBoard):
    for row in gameBoard:
        print(" ".join(map(str, row)))

def valid_move_Check(gameBoard, r, c, val):
    #Checks validity of inserting val into board, based on row
    if val in gameBoard[r]:
        return False
    #Checks validity of inserting val into board, based on column
    if val in [gameBoard[i][c] for i in range(9)]:
        return False
    #Checks validity based on 3x3 grid
    #Line below identifies what 3x3 grid (r,c) is in
    init_r, init_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(init_r, init_r + 3):
        for j in range(init_c, init_c + 3):
            if gameBoard[i][j] == val:
                return False
    return True

def empty_Check(gameBoard):
    for i in range(9):
        for j in range(9):
            if gameBoard[i][j] == 0:
                return i, j
    return False, False

def solve(gameBoard):
    r, c = empty_Check(gameBoard)
    #If statement below checks if board is already solved or not. This is done by checking to see if 
    #the row value that the empty_Check function returned is False. False being returned means that there
    #are no more empty squares in the puzzle and the game has been solved.
    if r is False:
        return True

    for val in range(1,10):
        if valid_move_Check(gameBoard, r, c, val):
            gameBoard[r][c] = val
            if solve(gameBoard):
                return True
            gameBoard[r][c] = 0 
    return False

def main():
    fileName = input('Welcome! Please enter a file name to continue. ')
    if(os.path.exists(fileName) == False):
        fileName = input('Invalid file name. Please enter a valid file name. ')
    board = []
    with open(fileName, 'r') as file:
        for line in file:
            values = list(map(int, line.strip().split()))
            board.append(values)

    print("\nInitial Sudoku Puzzle:")
    print_board(board)
    
    if solve(board):
        print("\nSolved Sudoku Puzzle:")
        print_board(board)
    else:
        print("\nNo solution exists for the given puzzle.")

main()