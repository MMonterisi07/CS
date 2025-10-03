'''
Author: Maddox Monterisi
Date: 9/30/25
Description: A list of functions that are based of an imputed name
Bugs: N/A
Challenges: build a menu, has_title, sorted_array
Sources: Ms. Marciano, worked with Will Everett on the board multiple times
Log: 1.0 initial release
'''
import random
def reverse(name):
    '''
    Reverses the name that the user inputed
    Args:
        name(str): original name input
    returns:
        reversed name
        '''
    reverse_name = str.lower(name[::-1])
    #returning the name from the back to the front
    return(reverse_name)
def count_vowels(name):
    '''
    counts the number of vowels in the name
    Args:
        name(str): original name input
    returns 
        number of vowels in the name
    '''
    count_vowel = 0
    for character in name:
        if character in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count_vowel += 1
    #if a vowel is in the name, adds 1 to counter
    #returns final count
    return(count_vowel)
def count_consonants(name):
    '''
    counts the number of cononants 
    Args:
        name(str): original name input
    returns
        number of consonants in the name
    '''
    count_consonant = 0
    for character in name:
        if character not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count_consonant += 1
    #if a consonant is in the name, adds 1 to counter
    #returns final count
    return(count_consonant)
def first_name(name):
    '''
    Description: prints only the first name in the full name that the user imputed
    Args:
        name(str): original name input
    returns
        first name in full name'''
    names = name.split(' ')
    if names[0] in ('Dr.', 'Mr.', 'Professor', 'sir', 'lord', 'lady', 'king', 'queen'):
        return(names[1])
    #if the name has a title at front, exclude that and return the next index, which would be the first name
    else:
        return(names[0])
def last_name(name):
    '''
    Description: prints only the last name in the full name that the user imputed
    Args:
        name(str): original name input
    returns
        last name in full name
    '''
    names = name.split(' ')
    if names[0] in ('Dr.', 'Mr.', 'Professor', 'sir', 'lord', 'lady', 'king', 'queen'):
        return names[3]
    #if the name has a title at front, exclude that and return the next index, which would be the last name
    else:
        return(names[2])
def middle_name(name):
    '''
    Description: prints only the middle name in the full name that the user imputed
    Args:
        name(str): original name input
    returns 
        middle name in full name
        '''
    names = name.split(' ')
    if names[0] in ('Dr.', 'Mr.', 'Professor', 'sir', 'lord', 'lady', 'king', 'queen'):
        return(names[2])
    #if the name has a title at front, exclude that and return the next index, which would be the first name
    else:
        return(names[1])
def has_hyphen(name):
    '''
    Description: determines if the name has a hyphen
    Args:
        name
    returns
        boolean if the name has a hyphen
    '''
    hyphen = '-'
    if hyphen in last_name(name):
        print('True')
    else:
        print('False')
def lowercase(name):
    '''
    Description: converts full name to lowercase
    Args:
        name
    returns
        full name in lowercase
    '''
    lowercase_name = str.lower(name)
    return(lowercase_name)
def uppercase(name):
    '''
    Description: converts full name to uppercase
    Args: 
        name
    returns
        full name in uppercase'''
    uppercase_name = str.upper(name)
    return(uppercase_name)
def shuffle_name(name):
    '''
    Description: randomly shuffles name
    Args:
        name
    returns
        shuffled name
    '''
    shuffled_name = ''
    letters = list(name)
    #while length of the name is longer than 0 letters, keeps randomly selecting numbers and deleting them, then adding them to the shuffled name
    while len(letters) > 0:
        letter = random.choice(letters)
        shuffled_name += letter
        letters.remove(letter)
    return (lowercase(shuffled_name))
def is_palindrome(name):
    '''
    Description: tests if the name inputed is a palindrome
    Args:
        name
    returns
        boolean based on if the name is a palindrome
    '''
    return name == reverse(name)
def initials(name):
    '''
    Description: shows the initials of the name
    Args:
        name
    returns
        initials of inputed name
    '''
    final_initials = ' '
    first = first_name(name)
    second = middle_name(name)
    third = last_name(name)
    #splitting full input into first, last, and middle names

    first_initial = first[0]
    second_initial = second[0]
    third_initial = third[0]
    #takes first index of every name and adds it to final initials
    final_initials = (first_initial + second_initial + third_initial)
    return(uppercase(final_initials))
def sorted_array(name):
    '''
    Description: returns name as a sorted array
    Args:
        name(str): original name input
    returns
        sorted array
    '''
    real_name = name.replace(' ', '')
    real_name = name.replace(' ', '')
    characters = list(real_name)
    sorted_characters = sorted(characters)
    #sorts by alphabetical order
    return ' '.join(sorted_characters)
def has_title(name):
    '''
    Description:
    Args:
        name(str): original name input
    '''
    titles = ['Dr.', 'Mr.', 'Jr.', 'Sr.', 'III', 'IV', 'PhD', 'MD', 'Professor', 'sir', 'lord', 'lady', 'king', 'queen']
    for char in titles:
        if char in name:
            return True
        else:
            return False
    #if the characters in the title listed are in the name, returns true - else, false
def main():
    while True:
        name = input('What is your full (first, middle, last) name? ')
        while True:
            selection = input('''What would you like to do with your name?
                              1. Reverse it
                              2. Find the number of vowels in the name
                              3. Find the number of consonants
                              4. Returns your first name
                              5. Returns your last name
                              6. Returns your middle name
                              7. Returns True/False if your last name has a hyphen
                              8. Converts full name to lower case
                              9. Converts full name to upper care
                              10. Mix up the letters in the name
                              11. Returns True/False if the name is a palindrome
                              12. Makes initials from name
                              13. Return name as a sorted array of characters
                              14. Check if your name has a title
                              15. Exit code
                              Choose a number:
                              ''')
            if selection == '1':
                print(reverse(name))
            elif selection == '2':
                print(count_vowels(name))
            elif selection == '3':
                print(count_consonants(name))
            elif selection == '4':
                print(first_name(name))
            elif selection == '5':
                print(last_name(name))
            elif selection == '6':
                print(middle_name(name))
            elif selection == '7':
                has_hyphen(name)
            elif selection == '8':
                print(lowercase(name))
            elif selection == '9':
                print(uppercase(name))
            elif selection == '10':
                print(shuffle_name(name))
            elif selection == '11':
                print(is_palindrome(name))
            elif selection == '12':
                print(initials(name))
            elif selection == '13':
                print(sorted_array(name))
            elif selection == '14':
                print(has_title(name))
            elif selection == '15':
                break
            else:
                print('Invalid response. That option does not exist.')
main()