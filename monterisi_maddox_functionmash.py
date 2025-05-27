'''
Name: Maddox Monterisi
Date: 5/5/25
Description: A function program that gives the user a choice of which function to use, then executes the function
Bugs: none
Challenges: reverse_string, is_palindrome
Sources: none
'''
import random

def chorus():
    '''
    Prints the chorus of the song
    Args: 
        none
    Returns: 
        print: chrous
    '''
    print('''
        Don't stop me now
I'm havin' such a good time, I'm havin' a ball
Don't stop me now
If you wanna have a good time, just give me a call
(Don't stop me now) 'Cause I'm havin' a good time
(Don't stop me now) Yes, I'm havin' a good time
I don't wanna stop at all, yeah''')
def sing():
    '''
    Use the chorus function to sing the entire song
    Args:
        None
    Returns:
        print: entire song
    '''
    print('''Tonight, I'm gonna have myself a real good time
I feel alive
And the world, I'll turn it inside out, yeah
I'm floatin' around in ecstasy
So don't stop me now
Don't stop me
'Cause I'm havin' a good time
Havin' a good time
I'm a shootin' star, leapin' through the sky like a tiger
Defyin' the laws of gravity
I'm a racin' car, passin' by like Lady Godiva
I'm gonna go, go, go, there's no stoppin' me
I'm burnin' through the sky, yeah
Two hundred degrees, that's why they call me Mister Fahrenheit
I'm travelling at the speed of light
I wanna make a supersonic man outta you''')
    chorus()
    print('''I'm a rocket ship on my way to Mars on a collision course
I am a satellite, I'm out of control
I'm a sex machine, ready to reload like an atom bomb
About to oh, oh, oh, oh, oh, explode
I'm burnin' through the sky, yeah
Two hundred degrees, that's why they call me Mister Fahrenheit
I'm travellin' at the speed of light
I wanna make a supersonic woman of you
Oh, I'm burnin' through the sky, yeah
Two hundred degrees, that's why they call me Mister Fahrenheit, hey
Travellin' at the speed of light
I wanna make a supersonic man outta you, hey, hey''')
    chorus()
def add(num1, num2):
    '''
    Takes two numbers and adds them together
    Args:
        num1 (int): first number
        num2 (int): second number
    Returns:
        print: sum of the two numbers
    '''
    print(num1 + num2)
def print_list(array):
    '''
    Takes a list and prints every element in that list individually (vertically)
    Args:
        array (list): the list printed
    returns:
        print: list vertically'''
    for element in array:
        print(element)
def in_list(array, element):
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args:
        array (list): the list checked
        element (any): the individual number in the list
    returns:
        bool: True/False based on if it is in the list
    '''
    return element in array
def is_integer(number):
    '''
    Takes any parameter and returns a boolean based on if it is an integer.
    Args:
        number (any): number that is checked to be an integer
    returns:
        bool: True/False based on if it is an integer
    '''
    try:
        int(number)
        return True
    except ValueError:
        return False
def get_integers():
    '''
    Asks the user for two numbers, uses is_integer to check input, returns the two integers.
    Args:
        None
    returns:
        number_1 (int)
        number_2 (int)
    '''
    while True:
        number_1 = input("Give me one integer: ")
        number_2 = input("Give me another integer: ")

        if is_integer(number_1) and is_integer(number_2):
            return int(number_1), int(number_2)
def get_random():
    '''
    Uses get_integers and prints a random number between the two given integers. 
    Args:
        none
    returns:
        print: random number between two numbers
    '''
    number_1, number_2 = get_integers()
    print(random.randint(number_1, number_2))
def count_vowels(string):
    '''
    Takes a string and returns the number of vowels in it
    Args:
        string (str)
    returns:
        int: count of vowels
    '''
    count = 0
    
    for character in string:
        if character in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count
def reverse_string(string):
    '''
    Takes a string and reverses it
    Args:
        string (str)
    returns:
        str: reversed string
    '''
    return string[::-1]
def is_palindrome(string):
    '''
    Takes a string and checks whether it is a palindrome
    Args:
        string (str)
    returns:
        bool: True/False based on if it is a palindrome'''
    return string == reverse_string(string)
def main():
    while True:
        function = input('''Which function do you want to use? Press q to quit. 
    1. sing an song
    2. add two numbers
    3. enter a list and print it vertically
    4. see if a number is in a list
    5. see if hello and 3 are numbers
    6. see how many vowels is in a word
    7. reverses an inputed string
    8. checks if an input is a palindrome
    Enter here: ''')
        if function == "q":
            break
        elif function == "1":
            sing()
        elif function == "2":
            a, b = get_integers()
            add(a, b)
        elif function == "3":
            user_list = input('Enter a list of items, use spaces to separate them: ').split(' ')
            print_list(user_list)
        elif function == "4":
            nums = [1, 2, 4, 5, 7, 10, 13, 15, 16, 19, 20]
            print(in_list(nums, 1))
            print(in_list(nums, 25))
        elif function == "5":
            print(is_integer('hello'))
            print(is_integer('3'))
        elif function == "6":
            get_random()
            print(count_vowels('adieu'))
        elif function == "7":
            string = input("Enter a string: ")
            print(reverse_string(string))
        elif function == "8":
            string = input("Enter a string: ")
            print(is_palindrome(string))
        else:
            print("Invalid response - enter a number between 1-8")
main()