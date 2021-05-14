#!/usr/bin/env python3
import os

def display_board(board):
    os.system('clear') 
    print(3 * "+-------", end="+\n")
    for i in range(3): 
        print(3 * "|       ", end="|\n|")
        for j in range(3):
            print(f"   {board[i][j]}   ", end="|")
        print()
        print(3 * "|       ", end="|\n")
        print(3 * "+-------", end="+\n")

    victor = victory_for(board, "X")
    
    if victor:
        return

    enter_move(board)

    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    chango = int(input("Tell us the number of the square you would like to place an X in: "))
    if chango < 10:
        chango -= 1
    x = chango // 3
    y = chango % 3
    board[x][y] = "X"
    display_board(board)
    make_list_of_free_fields(board)

    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    available = []
    for i in board:
        for j in range(1,10):
            if j in i:
                available.append(j) 
    return available 
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    xos = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                posi = (i,j)
                xos.append(posi) 

    print(xos)
    '''
    if 
   
    ### there is a total of 8 possible combinations of squares that will form a victory
    # for either sign. Of these 3 are vertical, 3 are horizontal and 2 lay diagonaly
    # accross the board. some of these possibilities can be grouped together with 'and'
    # 'or' combinations.  for example out of the top [0,0] corner we have 3 distinct
    # posibilities, one vertical, one horizontal and one diagonal.  The same is true for
    # the bottom far corner [3,3]. with these 6 possibilities out of the way, there
    # remains only one vertical and one horizontal posibility to contend with.

    '''
    return True 
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    return 
    # The function draws the computer's move and updates the board.

# creating the 2D array for the board
board = [[0 for x in range(3)] for y in range(3)]

# populating 2D array for the board
for i in range(9):
    x = i // 3
    y = i % 3
    z = board[x][y] = i + 1

board[1][1] = "X"
board[0][1] = "O"
board[2][0] = "X"

print(board)
display_board(board)

#victory_for(board, "X")

# enter_move(board)
