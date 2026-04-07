'''
Name: Maddox Monterisi
Date: 4/2/26
Description: creates a data dictionary of the most common words in Macbeth and Romeo and Juliet
Bugs: none
Sources: Will Everett taught me how to do the board
Version 1.0
'''

def display_board(board):

    print(f'''   1     2     3
1  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}
------------------
2  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}
------------------
3  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}
''')
    


def get_player_move(board, player):

    while True:
        print(f"Player {player}'s turn")
    
        try:
            row = int(input('Enter your row: '))
        except ValueError:
            print('That is not a number.')
            continue
        try:
            column = int(input('Enter a column: '))
        except ValueError:
            print("That is not a number. ")
        
        if row < 1 or row > 3 or column < 1 or column > 3:
            print('Number must be between 1 and 3. ')
            continue

        row_index = row - 1
        column_index = column - 1

        if board[row_index][column_index] != " ":
            print('That spot is already taken. Pick a different one.')
            continue
        return row_index, column_index

def check_winner(board):

    if board[0][0] == 'x' and board [0][1] == 'x' and board [0][2] == 'x':
        return 'X'
    elif board[1][0] == 'x' and board [1][1] == 'x' and board [1][2] == 'x':
        return 'X'
    elif board[2][0] == 'x' and board[2][1] == 'x' and board [2][2] == 'x':
        return 'X'
    
    elif board[0][0] == 'x' and board[1][0] == 'x' and board [2][0] == 'x':
        return 'X'
    elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        return 'X'
    elif board[2][0] == 'x' and board[2][1] == 'x' and board [2][2] == 'x':
        return 'X'
    
    elif board[0][0] == 'x' and board[1][1] == 'x' and board [2][2] == 'x':
        return 'X'
    elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x':
        return 'X'
    

    if board[0][0] == 'o' and board [0][1] == 'o' and board [0][2] == '':
        return 'O'
    elif board[1][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
        return 'O'
    elif board[2][0] == 'o' and board[2][0] == 'o' and board [2][2] == 'o':
        return 'O'
    
    elif board[0][0] == 'o' and board[1][0] == 'o' and board [2][0] == 'o':
        return 'O'
    elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
        return 'O'
    elif board[2][0] == 'o' and board[2][1] == 'o' and board [2][2] == 'o':
        return 'O'
    
    elif board[0][0] == 'o' and board[1][1] == 'o' and board [2][2] == 'o':
        return 'O'
    elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == 'o':
        return 'O'
 

def is_draw(board):
  
    for row in range(3):
        if board[row] == ' ':
            return True
    for column in range(3):
        if board[column] == ' ':
            return True



def play_game():

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    current_player = 'x'
    print('Welcome to Tic-Tac-Toe! Player x goes first. ')
    display_board(board)

    while True:
        row, column = get_player_move(board, current_player)
        board[row][column] = current_player
        display_board(board)

        winner = check_winner(board)
        if winner is True:
            print(f'Player {winner} wins! ')
            break

        if is_draw(board):
            print('Its a draw! ')
            break

        if current_player == 'x':
            current_player = 'o'
        elif current_player == 'o':
            current_player = 'x'



 
if __name__ == '__main__':
    while True:
        play_game()
 
        play_again = input('Would you like to play again? (y/n): ').strip().lower()
 
        if play_again != 'y':
            print("Thanks for playing!")
            break