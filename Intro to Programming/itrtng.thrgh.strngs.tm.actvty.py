'''
Iterating Through Strings Team Activity
Last Updated: 11/05/24
Author: MJ Quizon
'''
print('-' * 40)

inpt_lttr = input('What letter do you want to choose? ')

wrd = 'Commitment'
for letters in wrd:
    print(letters)

print('-' * 20)

for letters in wrd:
    if letters.lower() == inpt_lttr.lower():
        print(letters.upper(), end = '')
    else:
        print(letters.lower(), end = '')

print()
print('-' * 20)

for letters in wrd:
    if letters.lower() == inpt_lttr.lower():
        print('_', end = '')
    else:
        print(letters.lower(), end = '')
