'''
Week 2: More variables, input, and output
OG Author: Sister Hansen?
Current Working Author: MJ Quizon
Last Updated: 03/24/24
What kind of comment is this? This is a multi-line comment created with 3 quotes 
'''

#### variables (and good names) - What kind of comment is this?
# create a string variable
name = 'michael'

# create an integer variable
age = 18
#ints have no decimal

# create a float variable
age_2 = 18.7
#floats have decimals 

#### input
# get input from the user and store it in a variable
testing_age = input('Enter in your age: ')

# get a number from the user (decide if you want to convert now or later) *Converting at a later class
testing_age = int(age)

#### output and f-strings
# output all the variables with a single print statement
print(name, testing_age)

# now use an f-string to output all the variables
print(f"Hello {name}. Looks like you're {testing_age} years old." )


# output all the variables again, but use a string method on one 
# so that it prints in upper case, lower case, or title case
print(f"Hello {name.title()}. Looks like you're {testing_age} years old." )

# change what's in memory to the upper case version *Note: this is an example, this is needed when the scenario calls for it
# name = name.upper()
# Use ctrl + forward slash "/" to create/revert a single line comment 

print(f'''Here's your badge:
First name: {name}''')

print('-' * 10)

 