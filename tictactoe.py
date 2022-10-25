from pyfiglet import Figlet
from tabulate import tabulate

def main():
    # MAIN FUNCTION
    POINT = [0, 0]
    figlet = Figlet()
    fonts = figlet.getFonts()
    figlet.setFont(font="slant")
    print(figlet.renderText("Tic-Tac-Toe"))
    try:
        while True:

            boardgame = [" "]*10

            # ASK THE PLAYERS TO CHOOSE THEIR MARKER
            player1,player2 = player_input()

            # CHOOSE WHO GOES IN FIRST
            turn = choose_first(player1)
            print("\n"+turn+" goes first")

            play_game = input('\nLets play game? (Y or N): ')

            if play_game.upper() == 'Y':
                game_on = True

            else:
                game_on = False

            while game_on:
                # CHECK WHOSE TURN
                table = [["Player", "Point"]]
                if turn == "Player 1":
                    # MOVES FOR PLAYER ONE
                    display_board(boardgame)

                    # ASK THE PLAYER TO PLACE THEIR MARKER,
                    position = player_choice(boardgame)
                    place_marker(boardgame,player1,position)

                    # CHECK FOR WIN OR TIE
                    if win_check(boardgame, player1):
                        display_board(boardgame)
                        POINT[0] += 1
                        print('Player 1 has won the game!\n')
                        game_on = False
                    else:
                        if full_board_check(boardgame):
                            display_board(boardgame)
                            print('The game has been tied!\n')
                            game_on = False
                        else:
                            turn = 'Player 2'

                else:
                    # MOVES FOR PLAYER TWO
                    display_board(boardgame)

                    # ASK THE PLAYER TO PLACE THEIR MARKER,
                    position = player_choice(boardgame)
                    place_marker(boardgame,player2,position)

                    # CHECK FOR WIN OR TIE
                    if win_check(boardgame, player2):
                        display_board(boardgame)
                        POINT[1] += 1
                        print('Player 2 has won the game!\n')
                        game_on = False
                    else:
                        if full_board_check(boardgame):
                            display_board(boardgame)
                            print('The game has been tied!\n')
                            game_on = False
                        else:
                            turn = 'Player 1'
                if game_on == False:
                    table.append(["P1", POINT[0]])
                    table.append(["P2", POINT[1]])
                    print(tabulate(table, headers="firstrow", 
tablefmt="grid"))
                print()


            # Check whether the player wants to play again
            if not replay():
                break

    except (EOFError, KeyboardInterrupt):
        print("\n\nAww! We are sad you left early🥲.")

    else:
        print("\n", tabulate([["Thank you for playing Tic-Tac-Toe!"]], 
tablefmt="grid"), "\n")

def display_board(board):
    # display the game as a board
    print('\n'*100)
    table = [[board[1], board[2], board[3]], [board[4], board[5], 
board[6]], [board[7], board[8], board[9]]]
    print(tabulate(table, tablefmt="grid"))
    print("\n\n")

def player_input():
    # take users input on which marker to choose
    pmark = input('Choose your marker (X or O): ').upper()
    table = [["Player", "Marker"]]
    while pmark.upper() not in ('X','O'):
        print('Sorry! Invalid marker chosen.')
        pmark = input('Choose your marker (X or O): ')
    table.append(["P1", pmark])
    if pmark.upper() == 'X':
        table.append(["P2", "O"])
        player1 = 'X'
        player2 = 'O'
    else:
        table.append(["P2", "X"])
        player1 = 'O'
        player2 = 'X'
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    return player1,player2

def place_marker(board, marker, position):
    # place a marker at a position by the user
    board[position] = marker

def win_check(board, marker):
    # win_check() checks if any user wins during the game
    return ((board[1]==marker and board[2]==marker and board[3]==marker) 
or
    (board[4]==marker and board[5]==marker and board[6]==marker) or
    (board[7]==marker and board[4]==marker and board[1]==marker) or
    (board[8]==marker and board[5]==marker and board[2]==marker) or
    (board[9]==marker and board[6]==marker and board[3]==marker) or
    (board[1]==marker and board[5]==marker and board[9]==marker) or
    (board[7]==marker and board[8]==marker and board[9]==marker) or
    (board[7]==marker and board[5]==marker and board[3]==marker))



def choose_first(player1):
    # selects the player that chooses X as the first player
    if player1 == "X":
        pone = 1
    else:
        pone = 2
    return f'Player {pone}'

def space_check(board, position):
    # check if there is a space in the given position
    if board[position] == " ":
        return True
    else:
        return False

def full_board_check(board):
    # checks if the board is full to find if its a draw
    countn=0
    for i in range(1,10):
        if board[i] != " ":
            countn+=1
        else:
            return False
    if countn == 9:
        return True

def marker_position(a):
    while a not in range(1, 10):
        return False
    return True

def player_choice(board):
    # enter the next user choice
    a = int(input('Enter your next position: '))
    while not marker_position(a):
        print("Invalid position entered\n")
        a = int(input('Enter your next position: '))
    while a in range(1, 10):
        if space_check(board,a):
            return a
        else:
            print('Please change the position since it is full')
            a = int(input('Enter your next position: '))

def replay():
    # ask user if they want to play again
    replay=input('Would you like to play again by changing the markers? (Y or N): ')
    if replay.upper() == 'Y':
        return True
    else:
        return False

if __name__ == "__main__":
    main()
