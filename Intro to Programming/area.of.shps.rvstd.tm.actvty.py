'''
Area of Shapes Revisited Team Activity
Author: MJ Quizon
Last Updated: 12/11/24
'''
import math
square_s = 0
rect_l = 0
rect_w = 0
circ_r = 0
shp_inpt = ''
print('-' * 40)
def compute_area_square(square_s):
    return square_s ** 2

def compute_area_rectangle(rect_l, rect_w):
    return rect_l * rect_w

def compute_area_circle(circ_r):
    return (circ_r ** 2) * math.pi

while shp_inpt != 'quit':
    shp_inpt = input('\nWhat shape do you have? ')
    shp_inpt = shp_inpt.lower()
    if shp_inpt == 'square':
        square_s = float(input('\nWhat is the length/height of a side of the square? '))
        square_a = compute_area_square(square_s)
        print(square_a)
    elif shp_inpt == 'rectangle':
        rect_l = float(input('\nWhat is the length of the rectangle? '))
        rect_w = float(input('What is the length of the rectangle? '))
        rect_a = compute_area_rectangle(rect_l, rect_w)
        print(rect_a)
    elif shp_inpt == 'circle': 
        circ_r = float(input('\nWhat is the radius of the circle? '))
        circ_a = compute_area_circle(circ_r)
        print(circ_a)

print('-' * 40)