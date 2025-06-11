import random

def main():
    repeat = ''
    while repeat != 'no':
        numbers = [16.2, 75.1, 52.3]
        print(f'numbers {numbers}')
        append_random_numbers(numbers)
        print(f'numbers {numbers}')
        append_random_numbers(numbers, 3)
        print(f'numbers {numbers}')
        repeat = input('Would you like to go again (yes or no)? ')

def append_random_numbers(numbers_list, quantity=1):
    for amount in range(quantity):
        random_number = random.uniform(0, 100)
        rounded_num = round(random_number, 1)
        numbers_list.append(rounded_num)

main()