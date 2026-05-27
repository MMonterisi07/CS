'''
Name: Maddox Monterisi
Date: 4/7/26
Description: Runs a tic tac toe game
Bugs: none
Sources: Will Everett taught me how to do the board
Version 1.1
'''

def display_board(board):
    '''
    Prints the tic-tac-toe board.
    Parameters: 
        board (list): 3x3 2D list of strings
    Returns: 
        None
    '''

    print(f'''   1     2     3
1  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}
------------------
2  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}
------------------
3  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}   
''')  #board
    


def get_player_move(board, player):
    '''
    Prompts the current player to enter a row and column and rejects squares that don't fit the criteria
    Parameters: 
        board (list) - 3x3 list
        player (str): 'x' or 'o'
    Returns: 
        row_index, column_index
    '''
    while True:
        print(f"Player {player}'s turn")    #displays whose turn it is
    
        try:
            row = int(input('Enter your row: '))    #prompts the user for a row
        except ValueError:    #if it is not a number
            print('That is not a number.')
            continue   #continues code
        try:    
            column = int(input('Enter a column: '))    #prompts user for a row
        except ValueError:     #if it is not a number
            print("That is not a number. ")
            continue    #continues code
        
        if row < 1 or row > 3 or column < 1 or column > 3:    #makes sure row is in the right range
            print('Number must be between 1 and 3. ')
            continue   #continues code
 
        row_index = row - 1       #converts input to index
        column_index = column - 1     #converts input to index
 
        if board[row_index][column_index] != " ":     #makes sure the spot is open
            print('That spot is already taken. Pick a different one.')
            continue
        return row_index, column_index  #returns row and column index

def check_winner(board):
    '''
    Checks all rows, columns, and diagonals for a winning combination
    Parameters: 
        board (list): 3x3 list
    Returns: 
        'X' if x wins, 'O' if o wins, None if no winner yet
    '''

    #vertical
    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
        return 'X'
    elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        return 'X'
    elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        return 'X'
 
    #horizontal
    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
        return 'X'
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        return 'X'
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
        return 'X'
 
    #diagonal
    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        return 'X'
    elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x':
        return 'X'
 
    #vertical
    elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
        return 'O'
    elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
        return 'O'
    elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
        return 'O'
 
    #horizontal
    elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
        return 'O'
    elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
        return 'O'
    elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
        return 'O'
 
    #diagonal
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        return 'O'
    elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == 'o':
        return 'O'
 

def is_draw(board):
    '''
    Checks whether the game is a draw
    Parameters: 
        board (list): 3x3 2D list
    Returns: 
        True if the board is full, False if any empty square remains
    '''
    for row in range(3):    #for all the rows
        for column in range(3):   #for all the columns
            if board[row][column] == ' ':   #if the spot is empty
                return False   #not a draw
    return True    #if this is not true, it is a draw


def play_game():
    '''
    Sets up the board and runs the main game loop, alternating turns between
    players until someone wins or the game ends in a draw.
    Parameters: 
        None
    Returns: 
        None
    '''
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]  #board
    current_player = 'x'   #shows current
    print('Welcome to Tic-Tac-Toe! Player x goes first. ')   
    display_board(board)   #displays the board
 
    while True:
        row, column = get_player_move(board, current_player)     #gets the player move
        board[row][column] = current_player    #the move is the current player
        display_board(board)     #displays board after each turn
 
        winner = check_winner(board)   #checks winner every turn
        if winner:   #if there is a winner
            print(f'Player {winner} wins! ')    #displays winner
            break
 
        if is_draw(board):   #if its a draw
            print('Its a draw! ')
            break
 
        if current_player == 'x':    #checks who is up after every turn
            current_player = 'o'
        elif current_player == 'o':
            current_player = 'x'
 
 
if __name__ == '__main__':
    while True:
        play_game()   #executes game
 
        play_again = input('Would you like to play again? (y/n): ').strip().lower()  #asks if user wants to play again 
 
        if play_again != 'y':    #if its not yes, end
            print("Thanks for playing!")
            break