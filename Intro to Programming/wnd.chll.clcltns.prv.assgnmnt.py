'''
Wind Chill Calculations Prove Assignment
Author: MJ Quizon
Last Updated: 12/11/24
'''
print('-' * 40)
def calculate_wind_chill(t, ws):
    wind_chill = 35.74 + (0.6215 * t) - (35.75 * (ws ** 0.16)) + (0.4275 * t) * (ws ** 0.16)
    print(f'At temperature {t}F, and wind speed {ws} mph, the windchill is: {wind_chill:.2f}F')

def celsius_to_fahrenheit(t):
    return t * 9/5 + 32

t = float(input('What is the temperature? '))

fORc = ''
while fORc not in ['c', 'f']:
    fORc = input('Fahrenheit or Celsius (F/C)? ' ).lower()
    if fORc == 'c':
        t = celsius_to_fahrenheit(t)

for ws in range(5, 61, 5):
    calculate_wind_chill(t, ws)

print('-' * 40)
    