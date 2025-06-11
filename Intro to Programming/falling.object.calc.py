'''
Team Activity: Falling Object Calculator
Last Updated: 10/07/24
Author: Michael Jacob (MJ) Quizon

For this team activity, you will work together to implement a fairly complicated Physics formula.

Where:
m = mass (in kg)
g = acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)
t = time (in seconds)
c = 1/2 p A C
p = density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)
A = cross sectional area of projectile (in square meters)
C = drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)
exp = the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).
sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).

Prompt the user for each of the variables described above.
Compute the value for the inner value c which is computed as:
c = (1 / 2) * p * A * C
Display the value c to three decimal places.
Compute and display the overall velocity. Display the value to three decimal places.
'''
import math
import time
print('Hello, I am Vanessa, your AI velocity calculator.')
for i in range(2):
    print('.')
    time.sleep(1)
print('At this current point in my programming, I can only calulate the speed of a falling object')
for i in range(2):
    print('.')
    time.sleep(1)
print('To begin my calculations, please enter the following: ')
for i in range(2):
    print('.')
    time.sleep(1)
m = float(input('Mass (in kg): '))
g = float(input('Gravity (in m/s^2 - 9.81 on Earth, 24 on Jupiter): '))
t = float(input('Time (in sec): '))
p = float(input('Fluid Density (1.3 kg/m^3 for air, 1000 kg/m^3 for water): '))
C = float(input('Drag Constant (Sphere - 0.5|Cylinder - 1.1): '))
A = float(input('Projectile Cross Sectional Area (in m^2): '))
c = (1/2) * p * A * C
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c)/m) * t))
print('\nCalculating. Please Wait')
for i in range(2):
    print('.')
    time.sleep(1)
print(f'''The inner value of c is: {c:.3f}
The velocity after {t:.2f} seconds is: {v:.3f} m/s
''')