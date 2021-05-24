#!/usr/bin/env python3
import os
import time
from random import choice


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    # clearing the screen
    os.system('clear') 
    # little bit of ascii art and values from the 2d array created in the main function
    print(3 * "+-------", end="+\n")
    for i in range(3): 
        print(3 * "|       ", end="|\n|")
        for j in range(3):
            print(f"   {board[i][j]}   ", end="|")
        print()
        print(3 * "|       ", end="|\n")
        print(3 * "+-------", end="+\n")


def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.

    # Current version initiates a variable and then keeps prompting user until a valid
    # number between 1 and 9 is presented.  Current version is not equiped to deal with a
    # user accidently reusing an already occupied square
    chango = 10

    while chango >= 10:
        chango = int(input("Tell us the number of the square you would like to place an X in: "))

    # Sending the choice to the function that makes the moves
    move_helper(board, chango, "X")

def ohh_move(board):
    # This function also accepts the board current status, asks a user about their move,
    # checks the input and updates the board according to the user's decision.

    # see lines 26 thru 28
    chango = 10

    while chango >= 10:
        chango = int(input("Tell us the number of the square you would like to place an O in: "))

    # Sending the choice to the function that makes the moves
    move_helper(board, chango, "O")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    # the way this was implemented is by checking that the value held by the particular tuple
    # that represents a square is a number between 1 and 9  
    available = []
    for i in board:
        for j in range(1,10):
            if j in i:
                available.append(j) 
    return available 


def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game

    # xos variable - list of x's or of o's
    xos = []
    # booly is global 'cause we need it in the main function body
    global booly
    booly = False 

    # The next few lines create tuples for locations in a 2D array
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                posi = (i,j)
                xos.append(posi) 

    # While commented out the next line is here for debugging purposes.
    # print(xos)
  
    # After extended deliberations, the method settled on to check the results is 3 if
    # statements, each of them with further if/elif statements nested
    if (1,1)in xos:
        if (0,2) in xos and (2,0) in xos:
            booly = True
        elif (1,0) in xos and (1,2) in xos:
            booly = True
        elif (0,1) in xos and (2,1) in xos:
            booly = True
        elif (0,0) in xos and (2,2) in xos:
            booly = True
    
    if (0,0) in xos:
        if (0,1) in xos and (0,2) in xos:
            booly = True
        elif (1,0) in xos and (2,0) in xos:
            booly = True

    if (2,2) in xos:
        if (2,0) in xos and (2,1) in xos:
            booly = True
        elif (0,2) in xos and (1,2) in xos:
            booly = True

    # Once an if statement above is successful, we print the winner
    if booly:
        print(sign, "is the winner of this game!")
        
    return booly 
    

def draw_move(board):
    # The function draws the computer's move and updates the board.

    # using another function we find the available locations on the board
    avail = make_list_of_free_fields(board)

    # In previous versions we used randint, choice is a much cleaner option
    x = choice(avail)

    # Sending the choice to the function that makes the moves
    move_helper(board, x, "O")


def move_helper(board, val, sign):
    # The function makes the actual moves for X and O (whether O is a user or machine) 
    
    # we adjust val to properly work with our calculation
    val -= 1
    x = val // 3
    y = val % 3
    # we place the provided sign in the apropriate location within the 2D array
    board[x][y] = sign 

    # the next line is here because the original version was very abrupt
    time.sleep(1.2)

    # we then go ahead and call a couple of a few functions from above.
    display_board(board)
    make_list_of_free_fields(board)
    victory_for(board, sign)

# Yeah, I know, someone is going to complain that I did not define an actual main function
# right here, maybe I later will, maybe I won't.  I currently do not need to incorporate
# this into anyting else, and do not particularly care if anyone else would like to.

# variables used moves - tracks where we are, options and Friends - whether it's a 2 player 
# game or user vs "AI", booly - global value from above, initialized for use in the main
moves = 0
options = -1
friends = False
booly = ""

# a loop that lets the user select the number of players
while options != 0 and options != 1:
    os.system('clear') 
    print("\n\nWould you like to play TicTacToe vs. a machine or against a friend?")
    options = int(input("\n\t\t[0] for a machine \n\t\t[1] for a friend\n\t\t\t"))
    if options == 1:
        friends = True
        
# creating the 2D array for the board
board = [[0 for x in range(3)] for y in range(3)]

# populating 2D array for the board
for i in range(9):
    x = i // 3
    y = i % 3
    z = board[x][y] = i + 1

# next line is self-explanatory
display_board(board)

# Loop that keeps the game going until a winner is decided 
while not booly:
    if moves % 2:
        sign = "X"
        if friends:
            ohh_move(board)
        else:
            draw_move(board)
    else:
        sign = "O"
        enter_move(board)

    moves += 1
