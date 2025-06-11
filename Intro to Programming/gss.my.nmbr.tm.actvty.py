'''
Guess My # Team Activity
Last Updated: 10/29/24
Author: Michael Jacob (MJ) Quizon

'''

import random

print('-' * 40)
# nmbr = random.randint(1,10)
# print(f'\n{nmbr})

# Step 1:
# mgc_nmber = int(input('\nWhat is the magic number? '))
# npt_nmbr = int(input('What is your guess? '))

# if npt_nmbr > mgc_nmber:
#     print('Guess lower')
# elif npt_nmbr < mgc_nmber:
#     print('Guess higher')
# elif npt_nmbr == mgc_nmber:
#     print('You guessed correctly!')

# Step 2:
# mgc_nmber = int(input('\nWhat is the magic number? '))
# npt_nmbr = 0

# while mgc_nmber != npt_nmbr:
#     npt_nmbr = int(input('What is your guess? '))
#     if npt_nmbr > mgc_nmber:
#         print('Guess lower')
#     elif npt_nmbr < mgc_nmber:
#         print('Guess higher')

# print('You guessed correctly!')

# Step 3:
# mgc_nmbr = random.randint(1, 100)
# npt_nmbr = 0

# while mgc_nmbr != npt_nmbr:
#     npt_nmbr = int(input('\nWhat is your guess? '))
#     if npt_nmbr > mgc_nmbr:
#         print('Guess lower')
#     elif npt_nmbr < mgc_nmbr:
#         print('Guess higher')

# print(f'''\nYou guessed correctly!
# The magic number was {mgc_nmbr}.''')

# Stretch Challenge 1:
# mgc_nmbr = random.randint(1, 100)
# npt_nmbr = 0
# gss_attmpts = 0

# while mgc_nmbr != npt_nmbr:
#     npt_nmbr = int(input('\nWhat is your guess? '))
#     if npt_nmbr > mgc_nmbr:
#         print('Guess lower')
#         gss_attmpts += 1
#     elif npt_nmbr < mgc_nmbr:
#         print('Guess higher')
#         gss_attmpts += 1


# print(f'''\nYou guessed correctly!
# The magic number was {mgc_nmbr}.
# You guessed {gss_attmpts} times till you got it right!''')

# Stretch Challenge 2:
gm_lp = 'yes'

while gm_lp == 'yes':
    mgc_nmbr = random.randint(1, 100)
    npt_nmbr = 0
    gss_attmpts = 0

    while mgc_nmbr != npt_nmbr:
        npt_nmbr = int(input('\nWhat is your guess? '))
        if npt_nmbr > mgc_nmbr:
            print('Guess lower')
            gss_attmpts += 1
        elif npt_nmbr < mgc_nmbr:
            print('Guess higher')
            gss_attmpts += 1


    print(f'''\nYou guessed correctly!
The magic number was {mgc_nmbr}.
You guessed {gss_attmpts} times till you got it right!''')
    gm_lp = str(input('\nWould you like to play again? ')).lower()

print('\nThank you for playing!')
print()
print('-' * 40)
