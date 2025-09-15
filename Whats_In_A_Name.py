import random
def reverse(name):
    reverse_name = str.lower(name[::-1])
    print(reverse_name)

def count_vowels(name):
    count_vowel = 0
    for character in name:
        if character in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count_vowel += 1
    print (count_vowel)

def count_consonants(name):
    count_consonant = 0
    for character in name:
        if character not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count_consonant += 1
    print (count_consonant)

def first_name(name):
    names = name.split(' ')
    print(names[0])
def last_name(name):
    names = name.split(' ')
    print(names[2])
def middle_name(name):
    names = name.split(' ')
    print(names[1])

def has_hyphen(name):
    hyphen = '-'
    if hyphen in name:
        print('True')
    else:
        print('False')

def lowercase(name):
    lowercase_name = str.lower(name)
    print(lowercase_name)

def uppercase(name):
    uppercase_name = str.upper(name)
    print(uppercase_name)

def shuffle_name(name):


def is_palindrome(name):
    return name == reverse(name)

def initials(name):
    first_name = first[0]
    middle_name = middle[0]
    last_name = last[0]

def sorted_array(name):


def main():
    while True:
        name = input('What is your name? ')
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
                              13. Returns name in alphabetical order
                              Choose a number:
                              ''')
            if selection == '1':
                reverse(name)
            elif selection == '2':
                count_vowels(name)
            elif selection == '3':
                count_consonants(name)
            elif selection == '4':
                first_name(name)
            elif selection == '5':
                last_name(name)
            elif selection == '6':
                middle_name(name)
            elif selection == '7':
                has_hyphen(name)
            elif selection == '8':
                lowercase(name)
            elif selection == '9':
                uppercase(name)
            elif selection == '10':
                shuffle(name)
            elif selection == '11':
                print(is_palindrome(name))
main()