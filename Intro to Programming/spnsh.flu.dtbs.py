'''
Spanish Flu Database Prove Assignment
Author: MJ Quizon
Last Updated: 12/02/24
'''

min_l_expectancy = float(9000)
mIlec = ''
mIyr = 0
max_l_expectancy = float(-9000)
mAlec = ''
mAyr = 0
nptale = 0
nptle = []
nptmAle = float(-9000)
nptmIle = float(9000)
nptmAlec = ''
nptmIlec = ''

print('-' * 40)
input_year = int(input('Designate a year of interest: '))
with open('life-expectancy.csv') as database:
    d_header = next(database)
    for data in database:
        data = data.strip().split(',')
        country = data[0].strip()
        code = data[1]
        year = int(data[2])
        expectancy = float(data[3])
        if expectancy > max_l_expectancy:
            max_l_expectancy = expectancy
            mAlec = country
            mAyr = year
        elif expectancy < min_l_expectancy:
            min_l_expectancy = expectancy
            mIlec = country
            mIyr = year
        elif year == input_year:
            nptle.append(float(expectancy))
            nptale = sum(nptle) / len(nptle)
            if expectancy > nptmAle:
                nptmAle = expectancy
                nptmAlec = country
            elif expectancy < nptmIle:
                nptmIle = expectancy
                nptmIlec = country

print(f'''\nThe overall max life expectancy is: {max_l_expectancy} from {mAlec} in {mAyr}
The overall min life expectancy is: {min_l_expectancy} from {mIlec} in {mIyr}''')
print(f'''\nFor the year {input_year}:
The average life expectancy across all countries was {nptale:.2f}
The max life expectancy was in {nptmAlec} with {nptmAle}
The min life expectancy was in {nptmIlec} with {nptmIle}''')
print('-' * 40)
