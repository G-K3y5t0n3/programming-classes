'''
World Prove Assignment (Milestone)
Last Updated: 10/29/24
Author: Michael Jacob (MJ) Quizon

Milestone Requirements:
At the end of Lesson 07, to help make sure you are on track to finish the assignment, you need to complete the following:
    1. Have a secret word stored in the program.
    2. Prompt the user for a guess.
    3. Continue looping as long as that guess is not correct.
    4. Calculate the number of guesses and display it at the end.
    5. You do not need to have any hints at this point.
'''
wrdl_wrd = 'stove'
npt_wrd = 'words'
guss_attmpt = 0
print('-' *40)
print('''\nWelcome to the word guessing game! 
(commonly known as Worlde but I need to avoid copyright infringement)''')

while npt_wrd != wrdl_wrd:
    npt_wrd = str(input('\nWhat is your guess? '))
    if npt_wrd != wrdl_wrd:
        print('Your guess was incorrect.')
        guss_attmpt += 1
    else:
        guss_attmpt += 1

print(f'''Congrats! You guessed it!
It took you {guss_attmpt} times to get it right.''')
print()
print('-' * 40)
