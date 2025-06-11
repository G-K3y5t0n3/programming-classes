'''
Spanish Flu Database Prove Assignment
Author: MJ Quizon
Last Updated: 12/02/24
'''
print('-' * 40)

with open('life-expectancy.csv') as database:
    for data in database:
        data = data.strip()
        data_parts = data.split(',')
        country = data_parts[0]
        code = data_parts[1]
        year = (data_parts[2])
        expectancy = data_parts[3]
        min_expentancy = min(data_parts[3])
        max_expentancy = max(data_parts[3])
        print(min_expentancy)
        print(max_expentancy)
print('-' * 40)