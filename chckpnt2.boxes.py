'''
Boxes Checkpoint Assignment
Last Updated: 04/21/25
Author: Michael Jacob (MJ) Quizon

A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
Write a Python program named boxes.py that asks the user for two integers:

the number of manufactured items
the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items. 
This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
'''
import math

items = ''
items_per_box = ''

def boxes_needed():
    boxes = items / items_per_box
    print(f'''For {items} items, packing {items_per_box} items in each box, you will need {math.ceil(boxes)} boxes.''')
    # The github assignment link says to use the math.ceil() function which does work, but I normally use :.#f to determine whether it's a whole number or to use certain decimal places
    # print(f'''For {items} items, packing {items_per_box} items in each box, you will need {boxes:.0f} boxes.''')
items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))
boxes_needed()