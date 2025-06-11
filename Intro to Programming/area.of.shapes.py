'''
Area of Shapes Team Activity
Last Updated: 10/01/24
Author: Micahel Jacob (MJ) Quizon

Write a program to compute the areas of three different shapes. 
Prompt for the necessary information, then compute and display the area, as follows:

Make sure that your program can appropriately handle decimal values as well as whole numbers.

1. Square—The area is the length of a side squared.
2. Rectangle—The area is the length multiplied by the width.
3. Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.

Stretch Challenge #1: Instead of using 3.14 for your value of Pi, 
see if you can find and use the built-in value of Pi included in the python "math" module. 
Hint, you might try searching on the internet for something like, "python how to get the value of pi."

'''
import time
import math
# Apparently this is one way to input the value of pi into your code

square_measurement = float(input('What is the length/height of a side of the square? '))
square_area = square_measurement ** 2
print(f'The area of the square is: {square_area} units')
rect_length = float(input('What is the length of the rectangle? '))
rect_width = float(input('What is the width of the rectangle? '))
rect_area = rect_length * rect_width
print(f'The area of the rectangle is: {rect_area} units')
circ_rad = float(input('What is the radius of the circle? '))
circ_area = (circ_rad ** 2) * math.pi
#Replaceed 3.14 with math.pi for 1st stretch challenge
print(f'The area of the circle is: {circ_area} units')
for i in range(2):
    print('-' * 10)
    time.sleep(1)
#2nd Stretch Challenge
'''
Prompt the user for a single length value, 
then compute and display the areas of a square with that length of side, 
a circle with that radius, and then the volumes of a cube with that side and a sphere with that radius, 
all from the same value from the user.
'''
single_value = float(input('Give me a random number: '))
sv_square_area = single_value ** 2
sv_circ_area = (single_value ** 2 ) * math.pi
sv_cube_vol = single_value ** 3
sv_sphere_vol = (4/3) * math.pi * (single_value ** 3)
print(f'''With your number: {single_value}, you will have:
A square with a length of {single_value} units has an area of {sv_square_area} units
A circle with a radius of {single_value} units has an area of {sv_circ_area} units
A cube with a side length of {single_value} units has an volume of {sv_cube_vol} units
A sphere with a radius of {single_value} units has a volume of {sv_sphere_vol} units
''')
for i in range(2):
    print('-' * 10)
    time.sleep(1)
#3rd Stretch Challenge
'''
For each of the three areas in the core requirements, 
change the prompt for the user to ask for the value in centimeters. 
Then, display the resulting area in both square centimeters and square meters. 
Keep in mind that a centimeter is 1/100 of a meter, 
and a square centimeter is 1/10,000 of a square meter.
'''
square_measurement_cm = float(input('What is the length/height of a side of the square in centimeters? '))
square_area_cm = square_measurement_cm ** 2
square_area_m = square_area_cm / 10000
print(f'The area of the square is: {square_area_cm} centimeters squared & {square_area_m} meters squared')
rect_length_cm = float(input('What is the length of the rectangle in cm? '))
rect_width_cm = float(input('What is the width of the rectangle in cm? '))
rect_area_cm = rect_length_cm * rect_width_cm
rect_area_m = rect_area_cm /10000
print(f'The area of the rectangle is: {rect_area_cm} centimeters squared & {rect_area_m} meters squared')
circ_rad_cm = float(input('What is the radius of the circle? '))
circ_area_cm = (circ_rad_cm ** 2) * math.pi
circ_area_m = circ_area_cm / 10000
print(f'The area of the circle is: {circ_area_cm} centimeters squared & {circ_area_m} meters squared')