'''
List Index Checkpoint
Author: MJ Quizon
Last Updated: 11/18/24
'''

shopping_list = []
add_to_cart = None
print('-' * 40)
print('\nPlease enter the items of the shopping list (type: quit to finish):')
while add_to_cart != 'quit':
    add_to_cart = input('Item: ') 
    if add_to_cart != 'quit':
        shopping_list.append(add_to_cart)

print('\nThe shopping list is:')
for items in shopping_list:
    print(items)

print('\nThe shopping list w/ indexes is:')
for i in range(len(shopping_list)):
    items = shopping_list[i]
    print(f"{i}. {items}")

index = int(input('\nWhich item would you like to change? '))
new_item = input('What is the new item? ')

shopping_list[index] = new_item

print('\nThe shopping list w/ indexes is:')
for i in range(len(shopping_list)):
    items = shopping_list[i]
    print(f"{i}. {items}")

print()
print('-' * 40)
