#!/usr/bin/env python3
import os
import time
from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    os.system('clear') 
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

    chango = int(input("Tell us the number of the square you would like to place an X in: "))
    if chango < 10:
        chango -= 1

    move_helper(board, chango, "X")

def ohh_move(board):
    # This function also accepts the board current status, asks a user about their move,
    # checks the input and updates the board according to the user's decision.

    chango = int(input("Tell us the number of the square you would like to place an O in: "))
    if chango < 10:
        chango -= 1

    move_helper(board, chango, "O")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    available = []
    for i in board:
        for j in range(1,10):
            if j in i:
                available.append(j) 
    return available 


def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game

    xos = []
    booly = False 
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                posi = (i,j)
                xos.append(posi) 

    # print(xos)
   
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

    if booly:
        print(sign, "is the winner of this game!")
        
    return booly 
    

def draw_move(board):
    # The function draws the computer's move and updates the board.

    avail = make_list_of_free_fields(board)

    x = randrange(len(avail))
    i = avail[x] - 1

    move_helper(board, i, "O")


def move_helper(board, val, sign):
    x = val // 3
    y = val % 3
    board[x][y] = sign 

    time.sleep(3)
    display_board(board)
    make_list_of_free_fields(board)

moves = 0
options = -1
friends = False

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

display_board(board)

victor = False

while not victor:
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

    victor = victory_for(board, sign)
