'''
Week 3: Variables and Expressions(math)
Last Updated: 10/01/24
Author: Michael Jacob (MJ) Quizon
'''

#### Which are each of the following? (string, int, float)
x = '10' # string, bc it has quotes
y = 5 # int, bc there's no decimal
z = 3.14 # float, bc it has a decimal
print(int(x) * 5, y, z * 2) #Used int code to change the string into a integer so math is done rather than repeating "10" 5 times
#This does not change x into a integer permantly in memory till the next set of code

#### What do the following do?
x = int(x) # turns whatever x is into a integetr
y = float(y) # turns whatever y is into a float
z = str(z) # turns whatever z is into a string
#Note: this particular coding changes and stores the variables depending on what code you use

# print(x, y, z + "2")
#Note: this won't work bc z is not a string, the 2 needs to be in qutoes in order for the code to run

# print(x, y, float(z) + 2)
#z does not stay a float, it is converted to a float just for this

#Concatenate: "Gluing it to the end"

#### Which is better?
# print("I have " + str(x) + " cats.")
print(f"I have {x} cats.")

#### Order of operations
#### math operations and order of operations
'''
Operator	Description
()	        Parentheses
**	        Exponent
* / // %	Multiply, Divide, Floor divide, Modulo
+ -	        Addition, Subtraction
= 	        Assign
'''

#### What is stored in a, b, c and d? 
a = 10 + (4 * 2) - 3  #15
b = 5 % 2  # 1 - "Modulo" returns the remainder
c = 5 // 2 # 2 - "Floor" divide returns the whole number of a div equation
d = 6 / 2 # 2.5 - Normal Division returns a float only in python
print(f'math {a}, modulo {b}, floor divide {c}, normal divide {d}')

#### Team Activity
## Core requirements: 
# get user input (be able to handle ints or floats)
# convert it to a number so you can do some math with it (float)
# calculate areas of 3 shapes

# side = ???(input('What\'s the length of one side: '))
