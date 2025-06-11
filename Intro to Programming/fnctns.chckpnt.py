'''
Functions Checkpoint
Author: MJ Quizon
Last Updated: 12/11/24
'''
display_input = ''
print('-' * 40)

def display_regular():
    print(display_input)

def display_uppercase():
    print(display_input.upper())

def display_lowercase():
    print(display_input.lower())

display_input = input('What is your message? ')

display_regular()
display_uppercase()
display_lowercase()
print('-' * 40)


