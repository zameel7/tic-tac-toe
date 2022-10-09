# Tic-Tac-Toe
#### Video Demo: https://youtu.be/iTPSmOSNgsU
#### Description:

### Final project done as a part of the CS50P course by Harvard

- Initially to play this game, run:
```
    pip install -r requirements.txt
    python tictactoe.py
```

- This is a minimal tic-tac-toe game

- This can be played by 2 players
    > (This does not have a single player mode now)

### Working of game
__________________________

#### main.py

> The game on beginning
    - Asks the first player to choose a marker
    - The second player gets assigned the other marker based on what the 
first player chooses

> If the players are okay with the markers chosen, the game begins

> tabulate library is used to display the game board

> Players can alternatively place their markers on the board but the first 
play will be for the player with the "X" marker

> Whenever there is a consecutive 3 markers "X" or "O" placed, diagonally 
or horizontally or vertically, the game declares the player with the 3 
markers as the winner

> If there are no 3 consecutive markers placed even after the entire board 
is filled, the game will be declared as a tie

> After each set of the game, players will be shown their points


### Unit tests
___________________________

#### test_project.py

- These are the tests implemented

> test_full_board_check()
    - used to check if there is any space left in the game board

> test_choose_first()
    - used to choose which player goes first

> test_space_check()
    - used to check if the specified position is free to insert marker

> test_marker_position()
    - used to check if the specified marker position is within the range 1 
to 10

