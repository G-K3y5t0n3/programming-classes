'''
Tire Volume  Assignment
Last Updated: 04/21/25
Author: Michael Jacob (MJ) Quizon

The previous lesson's prove milestone required you to write a program named tire_volume.py that computes the approximate volume of air inside a tire.
Add code near the end of that program that does the following:

1. Gets the current date from the computer's operating system.
2. Opens a text file named volumes.txt for appending.
3. Appends to the end of the volumes.txt file one line of text that contains the following five values:
    a. current date
    b. width of the tire
    c. aspect ratio of the tire
    d. diameter of the wheel
    e. volume of the tire
'''
import math
import time
from datetime import datetime

t_width = ''
t_aspectRatio = ''
w_diamter = ''
current_date = datetime.now()

def tire_volume():
    t_volume = (math.pi * (t_width**2) * t_aspectRatio * (t_width * t_aspectRatio + 2540 * w_diamter)) / 10000000000
    print(f'''\nThe approximate volume is {t_volume:.2f} liters''')
    while True:
        input_pnumber = input('\nWould you like to be notified via phone number(y/n)? ')
        # This phone number input is the extra feature that I wanted to add for full points
        if input_pnumber.lower()[0] == 'y':
            phone_number = int(input('Please type in your phone number: '))
            with open('volumes.txt', 'a') as volumes:
                volumes.write(f'''{current_date:%Y-%m-%d}, {t_width}, {t_aspectRatio}, {w_diamter}, {t_volume:.2f}, {phone_number}\n''')
            break
        elif input_pnumber.lower()[0] == 'n':
            with open('volumes.txt', 'a') as volumes:
                volumes.write(f'''{current_date:%Y-%m-%d}, {t_width}, {t_aspectRatio}, {w_diamter}, {t_volume:.2f}\n''')
            break
        else:
            for i in range(3):
                print('ERROR')
                time.sleep(1)
            print("I'm sorry, your response cannot be calulated")
    
# Enter the width of the tire in mm (ex 205): 185
# Enter the aspect ratio of the tire (ex 60): 50
# Enter the diameter of the wheel in inches (ex 15): 14

t_width = int(input('\nEnter the width of the tire in mm (ex 205): '))
t_aspectRatio = int(input('\nEnter the aspect ratio of the tire (ex 60): '))
w_diamter = int(input('\nEnter the diameter of the wheel in inches (ex 15): '))
tire_volume()