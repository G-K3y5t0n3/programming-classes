'''
Shopping Cart Prove Assignment (Milestone)
Author: MJ Quizon
Last Updated: 11/14/24
'''
shppng_lst = []
prc_lst = []
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
        while True:
            addToCrt = input('\nWhat would you like to add? ')
            shppng_lst.append(addToCrt)
            addToCrtPrc = float(input(f"What is the price of '{addToCrt.capitalize()}'? $"))
            prc_lst.append(addToCrtPrc)
            print(f"\n'{addToCrt.capitalize()}' has been added to cart for ${addToCrtPrc:.2f}.")
            rpt = input('Would you like to add another item (yes/no)? ')
            if rpt.lower() == 'no':
                break
    elif cntrl == 2:
        print("The contents of the shopping carts are:")
        for items in range(len(shppng_lst)):
            print(f'{items + 1}. {shppng_lst[items]} - ${prc_lst[items]:.2f}')
    elif cntrl == 3:
        while True:
            rmvFrmCrt = int(input('Which item would you like to remove? Item #'))
            if 0 <= rmvFrmCrt < len(shppng_lst):
                rmvdItm = shppng_lst.pop(rmvFrmCrt - 1)
                rmvdItmPrc = prc_lst.pop(rmvFrmCrt - 1)
                print(f'Item #{rmvFrmCrt}: {rmvdItm} - ${rmvdItmPrc:.2f} has been removed')
                break
            else:
                print(f'Sorry, Item #{rmvFrmCrt} is not in your cart and cannot be removed')
    elif cntrl == 4:
        shppngLstTtl = sum(prc_lst)
        print(f'The total price of your items in your cart is ${shppngLstTtl:.2f}')
    else:
        print('Thank you. Goodbye')

print()
print('-' * 40)