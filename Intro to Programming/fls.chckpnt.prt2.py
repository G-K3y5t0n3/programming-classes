'''
Files Checkpoint Part 2
Author: MJ Quizon
Last Updated: 12/02/24
'''
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

yngst_age = 9000
yngst_nm = ''

for peeps in people:
    peeps_parts = peeps.split()
    peep_name = peeps_parts[0]
    peep_age = int(peeps_parts[1])
    if peep_age < yngst_age:
        yngst_age = peep_age
        yngst_nm = peep_name

print(f'{yngst_nm} is the youngest in the list with an age of {yngst_age}')