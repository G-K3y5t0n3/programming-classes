'''
World Prove Assignment
Last Updated: 11/19/24
Author: Michael Jacob (MJ) Quizon

Requirements:
    1. Have a secret word stored in the program.
    2. Prompt the user for a guess.
    3. Continue looping as long as that guess is not correct.
    4. Calculate the number of guesses and display it at the end.
    5. Add the hints according to the rules above.
    6. Add a check to verify that the length of the guess is the same as the length of the secret word. If it is not, display a message. If they are the same, then proceed to give the hint.
    7. Use a loop to generate the initial hint.
    8. Make sure to account for the following in your hints:
    9. Letters that are not present at all in the secret word (underscore _).
    10. Letters that are present in the secret word, but in a different spot (lowercase).
    11. Letters that are present in the secret word at that exact spot spot (uppercase).
'''

wrdl_wrd = 'stove'
npt_wrd = ''
guss_attmpt = 0
print('-' *40)
print('''\nWelcome to the word guessing game! 
(commonly known as Worlde but I need to avoid copyright infringement)''')

print('\nYour first hint is: ', end = '')
for letters in wrdl_wrd:
    print('_', end = ' ')

while npt_wrd != wrdl_wrd:
    npt_wrd = str(input('\nWhat is your guess? '))
    if len(npt_wrd) == len(wrdl_wrd):
        if npt_wrd != wrdl_wrd:
            for i, letters in enumerate(npt_wrd):
                if letters == wrdl_wrd[i]:
                    print(letters.upper(), end = ' ')
                elif letters in wrdl_wrd:
                    print(letters.lower(), end = ' ')
                else:
                    print('_', end = ' ')
            guss_attmpt += 1
        else:
            guss_attmpt += 1
    else:
        print('Sorry, the guess must have the same number of letters as the secret word.')



print(f'''Congrats! You guessed it!
It took you {guss_attmpt} times to get it right.''')
print()
print('-' * 40)
