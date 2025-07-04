'''
Unit Conversion: Temperatures Checkpoint
Last Updated: 10/04/24
Author: Michael Jacob (MJ) Quizon

Write a program to convert from Fahrenheit to Celsius. 
Display the result to one decimal place of precision.

To convert degrees in Fahrenheit to Celsius you need to subtract 32 from the Fahrenheit amount and then multiply it by the fraction 5/9.

Verify that your program works correctly by following each step in this testing procedure:
    1. Try the values in the examples on this page and ensure that your program generates the same results.
    2. Verify that you are displaying the result to 1 decimal point of precision as shown.
    3. Try converting 32 degrees Fahrenheit (freezing, which should be 0 degrees Celsius) and 212 degrees (boiling, which should be 100 degrees Celsius)
    4. Try converting 0 and a negative number and make sure they come out as you would expect.
    5. Verify that you have used good style, by checking the variable names you have used as well as the use of blank lines and whitespace around your operators.
'''
print('-' * 40)
print("\nLet's convert degrees Fahrenheit to degrees Celsius!")
f_temp = int(input('What is the temperature in Fahrenheit? '))
c_temp = (f_temp - 32) * (5/9)
print(f'{f_temp} degrees Fahrenheit converts to {c_temp:.1f} degrees Celsius')
print()
print('-' * 40)