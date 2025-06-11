'''
week10.py
Author: MJ Quizon
Last Updated: 11/19/24
'''

#### review
nums = []  # empty list we can append to later
nums = [1,5,7,9]  # initialized list
print(f'the third item is: {nums[2]}') # using the index

# get the number of items in the list & print it


# loop through a list to print each item
# print('\nprint the list')

# loop through a list using the index (and range)
# print('\nprint with index')

#### NEW
# loop thru list using index and user friendly (+1) display
# print("\nuser friendly (don't print 0)")


# use the index for 2 "parallel" lists
names = ['bill', 'jenny', 'tom']
ages = [9, 10, 8]
# print('\nloop thru two lists to print both values')

# index + 1 makes it more user friendly


# replace the second age 
# print('\nages before changing 2nd item (index 1):', ages)

# print('ages after changing the 2nd item:', ages)

# ask the user which line they want to change the age on
# if I used user friendly numbers to display, 
# I need to -1 to get the correct index 

# ask the user what the new age should be and store it


# show the list again to show the new age is in the list
# print('\naltered list:', ages)



# remove an item from the nums list with pop()
nums = [1,5,7,9]  # initialized list
print('\nbefore popping from nums')
print(nums)

num_poped = nums.pop() # pop or deletes the last item

print('\nafter popping from nums')
print(nums)

# print the item removed (popped)
print(num_poped)











# print()

# BONUS: insert a value at index 1 (may confuse some)
# val = int(input('Enter a value to insert at index 1: '))
# nums.insert(1, val)
# print('list with value inserted at index 1: ', nums)
# print()

