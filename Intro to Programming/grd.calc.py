'''
Grade Calculator Team Activity Assignment
Last Updated: 10/24/24
Author: Michael Jacob (MJ) Quizon

Write a program that determines the letter grade for a course according to the following scale:
    A >= 90
    B >= 80
    C >= 70
    D >= 60
    F < 60
'''
print('-' * 40)

npt_grd = int(input('What is your current grade percentage? '))

if npt_grd >= 90:
    lttr_grd = 'A'
elif npt_grd >= 80:
    lttr_grd = 'B'
elif npt_grd >= 70:
    lttr_grd = 'C'
elif npt_grd >= 60:
    lttr_grd = 'D'
else:
    lttr_grd = 'F'

print(f'\nBased on your {npt_grd} grade %, your letter grade is a(n): {lttr_grd}')    
if npt_grd > 70:
    print("Congratulations! You've passed the class!")
else:
    print("...That's rough buddy...")
print('-' * 40)



