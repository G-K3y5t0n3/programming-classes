'''
"While" Loop Checkpoint Assignment
Last Updated: 10/29/24
Author: Michael Jacob (MJ) Quizon

Write a Python Program that does each of the following:
    1. Use a while loop to ask the user for a positive number (>= 0).
        Continue asking as long as the number is negative, then display the number.

    2. Use a while loop, to simulate a child asking their parent for a piece of candy.
        Have the program keep looping until the user answers "yes", 
        then have the program output "Thank you."
'''
import time

print('-' * 40)
npt_nmbr = -1
gv_cndy = 'no'

while  npt_nmbr <= -1:
    npt_nmbr = int(input('\nPlease type a postive number: '))

print(f'''\nThe 1st Loop has been broken
The positive number you have chosen: {npt_nmbr}''')

for i in range(3):
    print('.')
    time.sleep(1)

while gv_cndy != 'yes':
    gv_cndy = input('May I have a piece of candy? ')

print('Thank you for the candy.')
print()
print('-' * 40)