'''
File Author: Michael Jacob (MJ) Quizon
Last Updated: 09/24/24
Goal: to make an ID badge generator to practice string formatting

I decided to give my ID badge generator a sort of "interactive AI" appearence rather than the instructor's "input info here"
'''

import time
#This extra code was shown to me by fellow team member: Anna
#This is to help setup code for later, I don't really know what it's used for

print("\nHello, I am Baymax, your occupation's resident AI")
print('Every employee at Marshmallow Inc. is required to have a ID badge')
print("I'm here to help you create your ID badge!")
first_name = input('\nTo begin creating your ID badge, what is your first name?: ')
print()
last_name =  input('Excellent! Now tell me your last name: ')
print()
phone_number = input('Great! Input your phone number next: ')
print()
email = input('Up next, input your email: ')
print()
id_number = input('Lastly, please input your id number (for simplicity type your I-Number or any random 9 number combination): ')
print()
job_title = input('Perfect! Now that we have your contact information, what is your job title? ')
print()
print("Great, please allow a couple seconds for me to create your ID badge")
for i in range(4):
    print('.')
    time.sleep(1)
#sleep stops the loops for a set amount of time
print('\nYour badge has now been created:')
print('-' * 40)
print(f'''{last_name.upper()}, {first_name}
{job_title}
ID: {id_number}

{email.lower()}
{phone_number}''')
print('-' * 40)
for i in range(4):
    print('!WARNING!')
    time.sleep(1)
hair_color = input('\nDue to recent spread of counterfeit IDs, extra information is needed. Input your current hair color: ')
eye_color = input('\nNext, input your eye color: ')
month_began = input('\nInput the month you started working as a ' + '"' + job_title + '"' + ' here: ')
while True:
    adv_train = input('\nLastly, were you given advanced training for job of ' + '"' + job_title + '"' + '(y/n): ' )
    if adv_train.lower()[0] == 'y':
        adv_train = 'Yes'
        break
    elif adv_train.lower()[0] == 'n':
        adv_train = 'No'
        break
    else:
        for i in range(3):
            print('ERROR')
            time.sleep(1)
        print("I'm sorry, your response cannot be calulated")
print('\nAgain, please allow a couple seconds for me to complete your ID badge')
for i in range(4):
    print('.')
    time.sleep(1)
print('\nYour badge has now been updated:')
print('-' * 40)
print(f'''{last_name.upper()}, {first_name}
{job_title})
ID: {id_number}

{email.lower()}
{phone_number}

Hair: {hair_color:<21} Eyes: {eye_color}")
Month: {month_began:<21} Training: {adv_train}''')
#Looked up python string format and just edited the code to the desired result
#Learned more formatting in class today (09/24/24) 
print('-' * 40)
