#Sudoku Board some 9x9 2D array
board = [
    [1,0,0,4,8,9,0,0,6],
    [7,3,0,0,0,0,0,4,0],
    [0,0,0,0,0,1,2,9,5],
    [0,0,7,1,2,0,6,0,0],
    [5,0,0,7,0,3,0,0,8],
    [0,0,6,0,9,5,7,0,0],
    [9,1,4,6,0,0,0,0,0],
    [0,2,0,0,0,0,0,3,7],
    [8,0,0,5,1,2,0,0,4]
]

#Function that prints a board
def printBoard(board):
    for i in range(len(board)):
        if i % 3 ==0 and i != 0:
            print("-------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print (str(board[i][j]) + " ", end="")

#Function that finds an empty space in the board 
#Returns a tuple (row, column)
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) 
    return None

#Backtracking Algorithim
def solve(board):
    #Base Case
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    #Recursive Case
    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

#Checking to see if a given position in the board is valid
#Returns a boolean
def valid(board, number, position):
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check box within board
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True
printBoard(board)
solve(board)
print("___________________________________")
printBoard(board)
