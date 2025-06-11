'''
Shopping Cart Prove Assignment (Milestone)
Author: MJ Quizon
Last Updated: 11/14/24
'''
shppng_lst = []
# prc_lst = []
cntrl = 0
print('-' * 40)
print('\nWelcome to the Shopping Cart Program! My name is Samuel, your helpful AI!')

while cntrl != 5:
    cntrl = int(input('''\nPlease select one of the following:
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: '''))
    if cntrl == 1:
        addToCrt = input('What would you like to add? ').lower()
        shppng_lst.append(addToCrt)
        print(f"'{addToCrt}' has been added to cart.")
    elif cntrl == 2:
        print("The contents of the shopping carts are:")
        for items in shppng_lst:
            print(items)
    else:
        print('Thank you. Goodbye')
