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
    #board

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

        random_row = random.randint(0, 4)  #chooses random row
        random_column = random.randint(0, 4)   #chooses random column
        row_list.append(random_row)     #adds the random row to the list
        column_list.append(random_column)     #adds the random column to the list
        count = count - 1    #takes one from the count
    

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
            row = int(input('Enter your row: '))  #enter the row
        except ValueError:
            print('That is not a number.')    #if it is not a number
            continue
        try:
            column = int(input('Enter a column: '))   #enter the column
        except ValueError:
            print("That is not a number. ")    #if it is not a number
        
        if row < 1 or row > 5 or column < 1 or column > 5:   #has to be between 1 and 5
            print('Number must be between 1 and 5. ')
            continue
 
        row_index = row - 1      #converts input to index
        column_index = column - 1
 
        if board[row_index][column_index] == '🔥' or board[row_index][column_index] == '❌':
            print('You already guessed that square. Try again. ')
            continue     #makes sure the user didn't already guess that spot

        number = 0
        while number < 4:
            if row_index == row_list[number]:  #process checks to see if the shot hit
                if column_index == column_list[number]:
                    print('You hit! ')
                    board[row_index][column_index] = '🔥'   #turns spot to fire emoji
                    return True  #was hit
                else:
                    number += 1    
            else:
                    number += 1
        board[row_index][column_index] = '❌'   #if it doesn't hit, make it an X
        print('Its a miss! ')
        return False   #no hit




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
        ["🌊", "🌊", "🌊", "🌊", "🌊"],  #makes the board
    ]
    row_list = []
    column_list = []
 
    count = 4
    ships_hit = 0
    turns = 10
    #count of each variable
    ai_move(count, row_list, column_list) #makes the ai choose spots
    
    player_turn = '1'  #first turn
 
    while True:
        if player_turn == '1':
            player_turn = '2'     #initially shows what turn user is on
        else:
            player_turn = '1'
 
        display_user_board(board)  #displays the board
        
        if get_player_move(board, row_list, column_list) == True:  #checks if the ship was hit
            ships_hit += 1   #adds one to the count
        turns -= 1    #takes one turn away
        if ships_hit == count:    #if ships hit = 4 
            print("You won! ")
            break
        elif turns == 0:   #no more turns left, so you lost
            print("You lost! ")
            break
 

    
play_game()