"""
Pendulum In-Class-Activity Assignment
Last Updated: 04/21/25
Author: Michael Jacob (MJ) Quizon

The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""
import math

p_length = ''

def pendulum_formula():
    time = (2 * math.pi) * math.sqrt(p_length/9.81)
    print(f'''\nTime (seconds): {time:.2f}''') 
print('-' * 40)
p_length = float(input('\nLength of pendulum (meters): '))
pendulum_formula()
print()
print('-' * 40)