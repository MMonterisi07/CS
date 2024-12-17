import random                                                   #imports random library so the magic 8 ball answers randomly
while True:                                                     #forever loop so 8 ball prompts user over and over again
    my_list = ["Yes!", "No!", "Maybe!", "Ask Again Later!"]     #represents the list of responses
    question = input ("Ask the Magic 8 Ball a question")        #prompts user to ask a question
    time.sleep(1)
    print (random.choice (my_list))                             #displays a random answer from the list
    
    




