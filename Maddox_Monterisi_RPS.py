import random                                                           #imports random library so bot answers randomly
import os                                                               #import for clearing code
print ("Welcome to the Rock Paper Scissors game!")                      #displays message               
RPS = ["rock", "paper", "scissors"]                                     #sets list
player1_score = 0                                                       #sets player 1 score at 0                        
player2_score = 0                                                       #sets player 2 score at 0
player2 = ""                                                            #sets player 2 name
player1 = ""                                                            #sets player 1 name
player1_name = input("Player 1, what is your name? ")                   #asks player 1 for name
while True:                                                             #forever loop
    play_style = input("2 player or bot? ").lower()                     #asks user for play style they want            
    if play_style == "2 player":                                        #if the play style is two players
        player2_name = input("Player 2, what is your name? ")           #asks player 2 for name
        break                                                           #breaks loop
    elif play_style == "bot":                                           #if the play style is bot
        player2_name = "bot"                                            #sets player 2 name as bot
        break                                                           #breaks loop
    else:                                                               #if user types something else
        print("Invalid response")                                       #displays message
while True:                                                             #forever loop                                               
    print (f"{player1_name}'s score is, {player1_score}")               #displays player 1 score        
    print (f"{player2_name}'s score is, {player2_score}")               #displays player 2 score        
    print ("Choose Rock, Paper, or Scissors")                           #displays message
    while True:                                                         #forever loop
        player1 = input ("Player 1, Make choice here: ").lower()        #asks player 1 for his choice
        if player1 not in RPS and player1 != "quit":                    #if player 1 makes choice not in list RPS and player 1 doesn't type quit
            print("Invalid response")                                   #displays message
        else:                                                           #if player 1 makes choice in list RPS
            break                                                       #breaks loop
    os.system("cls")                                                    #clears player 1 response
    if play_style == ("2 player"):                                      #if the play style is two player
        while True:                                                     #forever loop              
            player2 = input ("Player 2, make choice here:").lower()     #asks player 2 for his choice
            if player2 not in RPS and player2 != "quit":                #if player 2 makes choice not in list RPS and player 1 doesn't type quit                    
                print("Invalid response")                               #displays message
            else:                                                       #if player 2 makes choice in list RPS
                break                                                   #breaks loop
    elif play_style == ("bot"):                                         #if play style is bot                                  
        player2 = random.choice(RPS)                                    #sets player 2 choice to random
    if player1 == "quit" or player2 == "quit":                          #if any players choose to quit
        print (f"Player 1 final score was..., {player1_score}")         #displays player 1 final score
        print (f"Player 2 final score was..., {player2_score}")         #displays player 2 final score
        break                                                           #breaks loop
    print(f"Player 1 chose {player1}, player 2 chose {player2}")        #displays what each player chose
    if player1 == player2:                                              #if players tie
        print ("Tie! Try again.")                                       #displays message  
    elif player1 == "rock" and player2 == "scissors":                   #if player 1 chose rock and 2 chose scissors
        print ("Player 1 wins!")                                        #displays message
        player1_score += 1                                              #adds 1 to player 1 score    
    elif player1 == "rock" and player2 == "paper":                      #if player 1 chose rock and 2 chose paper
        print ("Player 2 wins!")                                        #displays message
        player2_score += 1                                              #adds 1 to player 2 score                     
    elif player1 == "scissors" and player2 == "rock":                   #if player 1 chose scissors and 2 chose rock
        print ("Player 2 wins!")                                        #displays message
        player2_score += 1                                              #adds 1 to player 2 score
    elif player1 == "scissors" and player2 == "paper":                  #if player 1 chose scissors and 2 chose paper
        print ("Player 1 wins!")                                        #displays message
        player1_score += 1                                              #adds 1 to player 1 score
    elif player1 == "paper" and player2 == "rock":                      #if player 1 chose paper and 2 chose rock
        print ("Player 1 wins")                                         #displays message
        player1_score += 1                                              #adds 1 to player 1 score
    elif player1 == "paper" and player2 == "scissors":                  #if player 1 chose paper and 2 chose scissors
        print ("Player 2 wins!")                                        #displays message
        player2_score += 1                                              #adds 1 to player 2 score
    while True:                                                         #forever loop
        play_again = input ("Play again? y/n").lower()                  #asks if user wants to play again
        if play_again == "n":                                           #if user says no
            print (f"Player 1 final score was..., {player1_score}")     #displays player 1 final score
            print (f"Player 2 final score was..., {player2_score}")     #displays player 2 final score
            exit()                                                      #exits code
        elif play_again != "y":                                         #if user doesn't say yes
            print ("Invalid response")                                  #displays message
        else:                                                           #if user types something other than y or n
            break                                                       #breaks loop
    


    
        
        
            
    
