'''
Discount Team Activity Assignment
Last Updated: 04/21/25
Author: Michael Jacob (MJ) Quizon

Work as a team to write a Python program named discount.py that gets a customer's subtotal as input and gets the current day of the week from your computer's operating system.
Your program must not ask the user to enter the day of the week. Instead, it must get the day of the week from your computer's operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal.
Your program must then compute the total amount due by adding sales tax of 6% to the subtotal.
Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.
'''
import math
from datetime import datetime

subtotal = ''
current_date = datetime.now()
current_weekday = current_date.weekday()
#current_weekday = 1

def total_amount():
    if current_weekday == 1 or current_weekday == 3:
        if subtotal >= 50:
            discount_amount = subtotal * .1
            total_before_tax = subtotal - discount_amount
            sales_tax = total_before_tax * .06
            total_amount = total_before_tax + sales_tax
        print(f'''
Discount amount: {discount_amount:.2f}
Sales tax amount: {sales_tax:.2f}
Total: {total_amount:.2f}''')
    else: 
        sales_tax = subtotal * .06
        total_amount = subtotal + sales_tax
        print(f'''
Sales tax amount: {sales_tax:.2f}
Total: {total_amount:.2f}''')

subtotal = float(input('Please enter the subtotal: '))
total_amount()

# discount_amount = subtotal * .1
#         total_before_tax = subtotal - discount_amount
#         sales_tax = total_before_tax * .06
#         total_amount = total_before_tax + sales_tax
#         print(f'''
# Discount amount: {discount_amount:.2f}
# Sales tax amount: {sales_tax:.2f}
# Total: {total_amount:.2f}''')