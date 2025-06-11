'''
Amusement Park Rides Team Activity
Last Updated: 10/24/24
Author: Michael Jacob (MJ) Quizon

The basic rules are as follows:
    No one under 36 inches may ever ride, either by themselves or with another rider.
    Normally, two riders sit in the car together. 
        A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.
    If there are two riders and one of them is at least 18 years old, they may ride together.

Core Requirements:
    1. Prompt the user for the age and height of the first person. 
        Then, ask whether there is a second rider, and if so, ask for their age and height.
    2. Handle the case of a single rider.
    3. Finish implementing the basic rules.

Stretch Challenge:
    1. If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.
    2. If a person is age 12–17, ask if that person has a golden passport. 
        If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)
    3. If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. 
        (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)
'''
print('-' * 40)
ride_dcsn = 'No'

frst_rdr_age = int(input('How old is the first rider? '))
frst_rdr_hght = int(input('How tall (in inches) is the first rider? '))
optnl_scnd_rdr = input('Is there a second rider (yes/no)? ').lower()
if optnl_scnd_rdr == 'yes':
    scnd_rdr_age = int(input('How old is the second rider? '))
    scnd_rdr_hght = int(input('How tall (in inches) is the second rider? '))

if frst_rdr_age >= 18:
    if frst_rdr_hght >= 62:
        if optnl_scnd_rdr == 'yes':
            if scnd_rdr_hght >= 36:
                rd_dcsn = 'Yes'
            else:
                rd_dcsn = 'No'
        elif optnl_scnd_rdr == 'no':
            rd_dcsn = 'Yes'
    else:
        rd_dcsn = 'No'
else:
    # S1: If there are two riders, but neither one is at least 18 years old, 
    # they may still ride as long as they are both:
    # at least 12 years old and at least 52 inches tall.
    # if frst_rdr_age >= 12 and frst_rdr_age >= 52:
    #     if scnd_rdr_age >= 12 and scnd_rdr_hght >= 52:
    #         rd_dcsn = 'Yes'
    #     else:
    #         rd_dcsn = 'No'
    # else: 
    #     rd_dcsn = 'No'
    rd_dcsn = 'No'

if rd_dcsn == 'Yes':
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')

print('-' * 40)

