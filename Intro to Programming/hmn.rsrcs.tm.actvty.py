'''
Human Resources Team Activity
Author: MJ Quizon
Last Updated: 12/02/24
'''
print('-' * 40)
with open('hr_system.txt') as information:
    for info in information:
        info = info.strip()
        info_parts = info.split(" ")
        print(info_parts)
        name = info_parts[0]
        job_title = info_parts[2]
        print(f'Name: {name}, Title: {job_title}')  

print('-' * 40)