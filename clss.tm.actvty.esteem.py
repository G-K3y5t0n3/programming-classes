'''
Esteem Team Activity
Author: Michael Jacob (MJ) Quizon
Last Updated: 05/27/25
'''

def main():
    print('-' * 40)
    print(f'''This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
          ''')

    score = 0
    score += calculate_postive_question('1. I feel that I am a person of worth, at least on an equal plane with others.')
    score += calculate_postive_question('2. I feel that I have a number of good qualities.')
    score += calculate_negative_question(' 3. All in all, I am inclined to feel that I am a failure.')
    score += calculate_postive_question('4. I am able to do things as well as most other people.')
    score += calculate_negative_question('5. I feel I do not have much to be proud of.')
    score += calculate_postive_question('6. I take a positive attitude toward myself.')
    score += calculate_postive_question('7. On the whole, I am satisfied with myself.')
    score += calculate_negative_question('8. I wish I could have more respect for myself.')
    score += calculate_negative_question('9. I certainly feel useless at times.')
    score += calculate_negative_question('10. At times I think I am no good at all.')
    print(f'''\nYour score is {score}.
A score below 15 may indicate problematic low self-esteem.''')
    print('-' * 40)

def calculate_postive_question(prompt):
    print(prompt)
    answer = input('Enter D | d | a | A: ')
    if answer == "D":
        return 0
    elif answer == "d":
        return 1
    elif answer == "a":
        return 2
    elif answer == "A":
        return 3

def calculate_negative_question(prompt):
    print(prompt)
    answer = input('Enter D | d | a | A: ')
    if answer == "D":
        return 3
    elif answer == "d":
        return 2
    elif answer == "a":
        return 1
    elif answer == "A":
        return 0  

main()