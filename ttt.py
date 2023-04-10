'''
This file contains a program that runs a basic 3 by 3 tic tac toe game 
between a player (user inputs) and the computer (randomized inputs).
Through various functions, it checks, calculates, and results in the 
player winning, losing, or tying with the computer in this game. 
'''

# import to generate randomized position for tic tac toe game
import random

def user():
    '''
    (None) -> string

    Ask and return which character, X or O, does the player want to be (accounting for invalid inputs)
    '''
    player = input("Do you want to be X or O? ").upper().strip()
    while player not in ["X", "O"]:
        player = input("Please input X or O? ")
    return player


def position():
    '''
    (None) -> string

    Ask and return what position the player would like to choose (accounting for invalid inputs)
    '''
    position = input(
        "Please pick a position: ").upper().replace(" ","")
    list = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    while position not in list:
        print(list)
        position = input(
            "Please input a valid position that hasn't already been taken (list of valid positions given above): ").upper().replace(" ","")
    return position

def print_board(board):
    '''
    Print given board.
    '''
    print("  A B C ")
    for i in range(3):
        print(str(i+1) + " " + board[i][0] + "|" + board[i][1] + "|" + board[i][2])

def win(board, char):
    '''
    (list, string) -> boolean

    Check to see given game board has a valid winning line (3 in a row, 3 in a column, or 3 diagonally). 
    Return True if a winning line is found, False otherwise.
    '''
    result = False

    # checking for a valid winning row
    for row in board:
        if row.count(char) == 3:
            result = True
            break

    # checking for valid winning column
    for column in range(len(board[0])):
        if board[0][column] == char:
            if board[0][column] == board[1][column] == board[2][column]:
                result = True
                break

    # checking for valid winning diagonal
    if board[0][0] == board[1][1] == board[2][2] == char:
        result = True
    elif board[0][2]  == board[1][1] == board[2][0] == char:
        result = True

    return result

def getCoordinate(position):
    ''' 
    (string) -> list

    Return coordinate of the given board at given position 
    '''

    column = 0
    if position[0] == "B":
        column = 1
    elif position[0] == "C":
        column = 2

    row = int(position[1])
    return [row-1, column]

def game():
    '''
    Compiling tic tac toe game
    '''
    # create a 3x3 tic tac toe game board using a 2D array.
    gameBoard = [["-","-","-"],["-","-","-"],["-","-","-"]]

    userChar = user()
    # the character for the computer will be whichever one the player didn't choose
    if userChar == "X":
        compChar = "O"
    else:
        compChar = "X"

    # this list will be used for computer's randomized moves
    spots = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    # stay in loop until player wins or computer wins or ties
    while not win(gameBoard, userChar):
        # print out game board at the beginning of each turn for player to see the game progress
        print_board(gameBoard)

        # player turn
        # to check for valid spot, ie. if the input spot is already taken, ask until valid spot
        validSpot = False
        while not validSpot:
            pos = position()
            spot = getCoordinate(pos)
            if gameBoard[spot[0]][spot[1]] == "-":
                gameBoard[spot[0]][spot[1]] = userChar
                # found a valid position, change validSpot to exit while loop
                validSpot = True
                # remove spot from list of available spots
                spots.remove(pos)
            else:
                print("Spot already taken!")
        
        # check if player win before computer moves
        if win(gameBoard, userChar):
            # print game board to show player how the game ended
            print_board(gameBoard)
            return "Congratulations! You've won! :)"

        # check for a tie or player won before computer moves
        if len(spots) == 0:
            # print game board to show player how the game ended
            print_board(gameBoard)
            return "It's a tie! >:)"

        # computer turn
        compPos = random.choice(spots)
        compSpot = getCoordinate(compPos)
        gameBoard[compSpot[0]][compSpot[1]] = compChar
        spots.remove(compPos)

        # check to see if computer won at the end of each turn
        if win(gameBoard, compChar):
            # print game board to show player how the game ended
            print_board(gameBoard)
            return "Sorry! You've lost! :( "


if __name__ == "__main__":
    print(game())  # implementing tic tac toe game