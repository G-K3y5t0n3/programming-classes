'''
Tire Volume Milestone Assignment
Last Updated: 04/21/25
Author: Michael Jacob (MJ) Quizon

The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. 
The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. 

The volume of space inside a tire can be approximated with this formula:

v = π * w^2 * a(w * a + 2,540 * d)
   -------------------------------
            10,000,000,000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
'''
import math

t_width = ''
t_aspectRatio = ''
w_diamter = ''

def tire_volume():
    t_volume = (math.pi * (t_width**2) * t_aspectRatio * (t_width * t_aspectRatio + 2540 * w_diamter)) / 10000000000
    print(f'''The approximate volume is {t_volume:.2f} liters''')

# Enter the width of the tire in mm (ex 205): 185
# Enter the aspect ratio of the tire (ex 60): 50
# Enter the diameter of the wheel in inches (ex 15): 14

t_width = int(input('Enter the width of the tire in mm (ex 205): '))
t_aspectRatio = int(input('Enter the aspect ratio of the tire (ex 60): '))
w_diamter = int(input('Enter the diameter of the wheel in inches (ex 15): '))
tire_volume()