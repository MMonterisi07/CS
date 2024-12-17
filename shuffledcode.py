import random                                                                                                               #import random library
name = input("What is your name? ")                                                                                         #set variable name to response of "What is your name"
print ("Good luck,", name)                                                                                                  #print message "good luck (name)"
words = ["computer", "science", "programming", "python", "logic", "board", "game", "condition"]                             #create list words - "computer", "science", "programming", "python", "logic", "board", "game", condition
games = 0                                                                                                                   #set variable games = 0
wins = 0                                                                                                                    #set variable wins = 0
while True:                                                                                                                 #create forever loop
    word = random.choice(words)                                                                                             #set variable word = random selection from word
    display = list(word)                                                                                                    #make variable word into a list and set it to variable display
    random.shuffle(display)                                                                                                 #scramble display list
    display = " ".join(display)                                                                                             #join list display and set it to variable display
    turns = 5                                                                                                               #set variable turns = 5
    while turns > 0:                                                                                                        #create condition: while turns > 0
        guess = input (f"Unscramble {display}. Enter a real word here: ")                                                   #set variable guess to response of "unscramble (display). Enter real word here: "
        if guess == word:                                                                                                   #if guess equals word
            print ("You got it!")                                                                                           #print message "you got it!"
            wins += 1                                                                                                       #add 1 to variable wins
            break                                                                                                           #end loop
        while True:                                                                                                         #create forever loop               
            y_n = input ("You did not get the word. Would you like to rescramble? Enter y/n: ")                             #set variable to response of "you did not get the word. Would you like to rescramble? Enter y or n: "
            if y_n == "n":                                                                                                  #if scramble equals "n"
                break                                                                                                       #end loop
            elif y_n == "y":                                                                                                #else/if scramble equals "y"
                display = list(word)                                                                                        #make variable display into a list and set it to display
                random.shuffle(display)                                                                                     #scramble display list
                display = " ".join(display)                                                                                 #join list display and set it to variable display
                break                                                                                                       #end loop
            else:                                                                                                           #else
                print ("Invalid response")                                                                                  #print message "invalid response"
        turns -= 1                                                                                                          #subtract 1 from variable turns
    print ("The word was", word)                                                                                            #print message "the word was (word)"
    games += 1                                                                                                              #add 1 to variable games
    while True:                                                                                                             #create forever loop
        play_again = input (f'{name}, you have won {wins} out of {games} games. Would you like to play again? y/n: ')       #set variable play_again to response of "(name), you have won (wins) out of (games) games. Would you like to play again? y/n: "
        if play_again == "n":                                                                                               #if play again equals "n"
            exit()                                                                                                          #end code
        elif play_again == "y":                                                                                             #else/if play_again equals "y"
            break                                                                                                           #end forever loop
        else:                                                                                                               #else
            print ("Invalid response. Limit to y/n.")                                                                       #print message "invalid response. Limit to y or n"