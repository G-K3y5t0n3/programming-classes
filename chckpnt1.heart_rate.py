"""
Heart Rate Checkpoint Assignment
Last Updated: 04/21/25
Author: Michael Jacob (MJ) Quizon

When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
age = ''

def caculate_heart_rate():
    max_hr = 220 - age
    min_ex_hr = max_hr * .65
    max_ex_hr = max_hr * .85 
    print(f'''
At {age}, your maximum heart rate should only go to {max_hr} bpm.

When you exercise to strengthen your heart, you should
keep your heart rate between {min_ex_hr:.0f} and {max_ex_hr:.0f} bpm.
''')

age = int(input("Please enter your age: "))

caculate_heart_rate()