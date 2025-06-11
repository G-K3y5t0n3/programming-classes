'''
If Statement Practice Prove Assignment
Last Updated: 10/14/24
Author: Michael Jacob (MJ) Quizon

Write a program that asks the user for two integers.

Then, write three separate if/else statements as follows:

If the first number is greater than the second, print "The first number is greater". 
Otherwise, print "The first number is not greater".

If the two numbers are equal print "The numbers are equal". 
Otherwise, print "The numbers are not equal".

If the second number is greater than the first, print "The second number is greater". 
Otherwise, print "The second number is not greater".

Comparing Strings
Have the program ask the user for their favorite animal. Then write an if statement as follows:

Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer). 
If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." 
Verify that it works regardless of the capitalization.
'''
print('-' * 40)
frst_npt = int(input('Give me a random integer: '))
scnd_npt = int(input("Give me a second random integer: "))
if frst_npt > scnd_npt:
    print(f'The first number: {frst_npt}, is greater than the second number: {scnd_npt}.')
else:
    print(f'The first number: {frst_npt}, is not greater than the second number: {scnd_npt}')
if frst_npt == scnd_npt:
    print(f'The numbers {frst_npt} & {scnd_npt} are equal as they are both the same number.')
else:
    print(f'The numbers {frst_npt} & {scnd_npt} are not equal')
if scnd_npt > frst_npt:
    print(f'The second number: {frst_npt}, is greater than the first number: {scnd_npt}.')
else:
    print(f'The second number: {frst_npt}, is not greater than the first number: {scnd_npt}.')

fv_anml = input('\nWhat is your favorite animal? ')
if fv_anml.lower() == "cats" or 'cat':
    print("Ayo really? That's my favorite animal too!")
else:
    print(f"Aw man... {fv_anml} isn't my favorite animal sadly")
print('-' * 40)