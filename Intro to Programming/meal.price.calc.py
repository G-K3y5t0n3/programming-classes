'''
Meal Price Calculator Prove Assignment
Last Updated: 10/04/24
Author: Michael Jacob (MJ) Quizon

Compute the price of a meal as follows by asking:
    for the price of child and adult meals, the number of each, 
    and then the sales tax rate. Use these values to determine the total price of the meal. 
    Then, ask for the payment amount and compute the amount of change to give back to the customer.

Keep in mind that some of these values are: 
    floating point numbers (they can have decimals) 
    and some of them are integers (whole numbers).

Ask the user for the following:

The price of a child's meal (floating point)
The price of an adult's meal (floating point)
The number of children (integer)
The number of adults (integer)
The sales tax rate (floating point)

Then, complete the following steps:

Determine the meal's subtotal (before adding sales tax) by: 
    multiplying the number of children by the price of their meal, 
    and multiplying the number of adults by the price of their meal 
    and adding those two values together.
Display the subtotal.

Hint from Instructor:
As you will see in the requirements list below, 
    this is as far as you need to get for the milestone requirements of Lesson 03, 
    but you should try to get as far as you can during Lesson 03 to make it even easier for yourself in the next lesson, 
    especially if you run into trouble.

Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.

Compute and display the total price of the meal by adding the subtotal and the sales tax.

Finally:

Ask the user for the the payment amount (floating point)

Compute and display the change.
'''
import time
import math

print('-' * 40)
print('\nHello! Welcome to The Crossroads!')
for i in range(2):
    print('.')
    time.sleep(1)
print("My name is Connor and I will be your AI assistant to help calculate your wanted meal's price")
for i in range(2):
    print('.')
    time.sleep(1)
c_price = float(input("To begin, what is the current price of a children's meal? $"))
a_price = float(input("Next, what is the current price of a adult's meal? $"))
c_amount = int(input('How many children are there in your given party? '))
a_amount = int(input('How many adults are in your given party? '))
c_total = c_price * c_amount
a_total = a_price * a_amount
subtotal = c_total + a_total
sales_tax = float(input("What is your area's current sales tax percentage? " )) /100
st_amount = subtotal * sales_tax
total = subtotal + st_amount
print('\nYour input is greatly appreciated, please wait a couple moments for your total to be calculated')
for i in range(3):
    print('.')
    time.sleep(1)
print(f'''Your total goes as follows:
Subtotal: {subtotal:.2f}$
Sales Tax: {st_amount:.2f}$
Total: {total:.2f}$''')
#Week 3 Milestone stops here

'''
cash = float(input('\nWhat is your payment amount? $'))
change = cash - total
print(f'Change: ${change:.2f}')
'''
#Using this code, you can choose a payment method of cash or card (debit or credit)
while True:
    p_method = input('\nWhat is your method of payment? ')
    if p_method.lower() == 'cash':
        p_method = 'Cash'
        break
    elif p_method.lower() == 'card':
        adv_train = 'Card'
        break
    else:
        for i in range(3):
            print('ERROR')
            time.sleep(1)
        print("I'm sorry, we do not take cryptocurrency at The Crossroads")
if p_method == 'Cash':
    print('\nYou have chosen to pay with "Cash"')
    for i in range(2):
        print('.')
        time.sleep(1)
    cash = float(input('What is your payment amount? $'))
    change = cash - total
    print(f'With your payment of ${cash} cash, your change equals up to: ${change:.2f}')
    for i in range(1):
        print('.')
        time.sleep(1)
    print("Thank you for using Connor, The Crossroads' AI. Have a nice day!")
    print('-' * 40)
elif p_method == 'Card':
    cc_rate = float(2.5) / 100
    # Average Credit Card Processing Fee is 2.5%
    cc_fee = total * cc_rate
    cc_total = total + cc_fee
    for i in range(2):
        print('.')
        time.sleep(1)
    print('You have chosen to pay with "Card"')
    print(f'Note: When using any card, there is a 2.5% processing fee. In your case, your fee will be ${cc_fee:.2f} ')
    while True:
        y_n = input('Is this acceptable? (Y/N): ')
        if y_n.lower() == 'yes':
            y_n = 'Yes'
            break
        elif y_n.lower() == 'no':
            print("Guess you're not getting your meals then...")
            y_n = 'Cash'
            break
        else:
            for i in range(2):
                print('ERROR')
                time.sleep(1)
            print("You almost have your food... Please respond with Yes or No")
    if y_n == 'Yes':
        print(f'Your new total is now ${cc_total:.2f} ')
        for i in range(1):
            print('.')
            time.sleep(1)
        print("Thank you for using Connor, The Crossroads' AI. Have a nice day!")
        print('-' * 40)