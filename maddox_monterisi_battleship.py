'''
Name: Maddox Monterisi
Date:
Description: Runs a battleship game between a player and a bot
Bugs: none
Sources: 
Version 1.1
'''
import random

def display_user_board(board):
    '''
    Displays the player's guess board, showing hits misses, and unexplored ocean.

    Parameters: 
        board (list): representing the player's guess board
    Returns: 
        None
    '''
    print(f'''   1     2     3     4     5
1  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |  {board[0][3]}  |  {board[0][4]}
-------------------------------
2  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |  {board[1][3]}  |  {board[1][4]}
-------------------------------
3  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |  {board[2][3]}  |  {board[2][4]}
-------------------------------
4  {board[3][0]}  |  {board[3][1]}  |  {board[3][2]}  |  {board[3][3]}  |  {board[3][4]}
-------------------------------
5  {board[4][0]}  |  {board[4][1]}  |  {board[4][2]}  |  {board[4][3]}  |  {board[4][4]}
''')
    

def ai_move(count, row_list, column_list):
    '''
    Randomly places the bot's ships by generating random row and column. Ship locations are fixed to be kept hidden from the player and never placed on the visible board.
    Parameters:
        count (int): Number of ships to place
        row_list (list): List to store ship row positions
        column_list (list): List to store ship column positions
    Returns: 
        None
    '''
    while count > 0:

        random_row = random.randint(0, 4)
        random_column = random.randint(0, 4)
        row_list.append(random_row) 
        column_list.append(random_column)
        count = count - 1
    

def get_player_move(board, row_list, column_list):
    '''
    Prompts the player to enter a row and column to guess, then checks whether the guess hits or misses.
        board (list): representing the player's guess board
        row_list (list): List of bot ship row positions (hidden from player)
        column_list (list): List of bot ship column positions (hidden from player)
    Returns: 
        True if the guess was a hit, false if it was a miss
    '''
    while True:
        try:
            row = int(input('Enter your row: '))
        except ValueError:
            print('That is not a number.')
            continue
        try:
            column = int(input('Enter a column: '))
        except ValueError:
            print("That is not a number. ")
        
        if row < 1 or row > 5 or column < 1 or column > 5:
            print('Number must be between 1 and 5. ')
            continue
 
        row_index = row - 1
        column_index = column - 1
 
        if board[row_index][column_index] == '🔥' or board[row_index][column_index] == '❌':
            print('You already guessed that square. Try again. ')
            continue
        
        number = 0
        while number < 4:
            if row_index == row_list[number]:
                if column_index == column_list[number]:
                    print('You hit! ')
                    board[row_index][column_index] = '🔥'
                    return True
                else:
                    number += 1
            else:
                    number += 1
        board[row_index][column_index] = '❌' 
        print('Its a miss! ')
        return False




def play_game():
    '''
    - Runs the main battleship game
    - Creates the player's guess board
    - alternates turns until the player either sinks all ships or runs out of turns
    Parameters:
        None
    Returns:
        None
    '''
    board = [
        ["🌊", "🌊", "🌊", "🌊", "🌊"],
        ["🌊", "🌊", "🌊", "🌊", "🌊"],
        ["🌊", "🌊", "🌊", "🌊", "🌊"],
        ["🌊", "🌊", "🌊", "🌊", "🌊"],
        ["🌊", "🌊", "🌊", "🌊", "🌊"],
    ]
    row_list = []
    column_list = []
 
    count = 4
    ships_hit = 0
    turns = 10
 
    ai_move(count, row_list, column_list)
 
    player_turn = '1'
 
    while True:
        if player_turn == '1':
            player_turn = '2'
        else:
            player_turn = '1'
 
        display_user_board(board)
        
        if get_player_move(board, row_list, column_list) == True:
            ships_hit += 1
        turns -= 1
        if ships_hit == count:
            print("You won! ")
            break
        elif turns == 0:
            print("You lost! ")
            break
 

    
play_game()