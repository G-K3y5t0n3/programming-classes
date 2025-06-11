'''
Week 8: For loops
Last Updated: 11/05/24
Author: MJ Quizin
'''

# 1) loop to print 1 through 5 (using a range)
for num in range(1, 6):
    print(num)


# 2) loop to print "Hello World" a user specified number of times
print()
loop_num = int(input('Number of times to loop: '))
for x in range(1, loop_num + 1):
    print(x, 'Hello World')


# 3) loop to print each letter in a string (two ways)
print() # 1st Way
my_string = "Hello"
for letters in my_string:
    print(letters)
print() # 2nd Way
for i in range(len(my_string)): # range --> (0, 1, 2, 3, 4)
    print(my_string[i])


# 4) loop to print each item in a list
print()
my_list = [1,3,5,7,9]
for numbers in my_list:
    print(numbers, end = '')

# team activity - looping through strings 

#### for day 2
# # variation on the stretch example
# first_name = "Brigham"
# last_name = "Younger"

# # use range and len to loop through the string
# for i in range(len(first_name)):
#     print(f"The letter {first_name[i]} is at position {i} in the first name")
#     print(f"The letter {last_name[i]} is at position {i} in the last name")
#     # we could also use if statements to check if the letters are the same
