'''
By Maddox Monterisi
A menu that randomly generates an item and a flair, and displays their assigned prices. Then, it adds all the prices together and displays the total. 
4/4/25
Bugs: none
Challenges: flair costs, different menu, total cost of all items, ensures a valid number is entered
Sources: https://www.programiz.com/python-programming/methods/list/index, https://www.101computing.net/number-only/
'''

import random                                                                                       #imports random library

mains = ['chicken cutlet', 'steak', 'salmon', 'baked potato', 'bacon burger']                       #displays mains
main_prices = [15, 35, 30, 12, 18]                                                                  #displays prices
flairs = ['with mozzarella', 'with broccoli rabe', 'over white rice', 'with butter', 'with fries']  #displays flairs
flair_prices = [5, 6, 5, 2, 7]                                                                      #displays flair prices
print("Welcome to my restaurant!")                                                                  #Displays message

while True:                                                                                     #forever loop
    try:                                                                                        #makes sure input is a valid number
        num_of_items = int(input('How many items? '))                                           #asks user for number of items
    except ValueError:                                                                          #if it is not a valid number
        print('Invalid Response. Enter a valid number.')                                        #displays statement
        continue                                                                                #continues code
    total = 0                                                                                   #sets total at 0

    for i in range(num_of_items):                                                                                                                                                       #repeats random choices based on how many items user wants
        main = random.choice(mains)                                                                                                                                                     #randomly chooses a main
        flair = random.choice(flairs)                                                                                                                                                   #randomly chooses a flair
        price = main_prices[mains.index(main)] + flair_prices[flairs.index(flair)]                                                                                                      #get the price by adding up the numbers at the indexes above in prices
        print(f'Your main is {main}, which is ${main_prices[mains.index(main)]}. Your flair is {flair}, which is ${flair_prices[flairs.index(flair)]}, so your total is ${price}')      #displays the order that was selected 
        total += price                                                                                                                                                                  #adds the price of order to total
    print(f"Your total is ${total}")                                                                                                                                                    #displays total