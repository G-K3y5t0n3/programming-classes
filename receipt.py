from datetime import datetime
import sys

def main():
    repeat = ''
    while repeat != 'no':
        now = datetime.now()
        day = f"{now.day:2}"  # space-padded
        formatted_time = now.strftime(f"%a %b {day} %H:%M:%S %Y")
        products_dict = read_dictionary("products.csv")
        # print(products_dict)
        print('-' * 40)
        print("Inkom Emporium")
        print()
        total_product_amount = 0
        subtotal = 0
        sales_tax = 0
        with open("request.csv", "rt") as requests:
            for i, info in enumerate(requests):
                if i == 0: continue
                try:
                    productID, product_amount = info.strip().split(",")
                    total_product_amount += int(product_amount)
                    subtotal += (float(products_dict[productID][1]) * float(product_amount))
                    print(f'{products_dict[productID][0]}: {product_amount} @ {products_dict[productID][1]}')
                except KeyError as key_error:
                    print(f'''Error: unknown product ID in the request.csv file
    {key_error}''')
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax
        print(f'''\nNumber of Items: {total_product_amount}
    Subtotal: {subtotal:.2f}
    Sales Tax: {sales_tax:.2f}
    Total: {total:.2f}''')
        print('\nThank you for shopping at the Inkom Emporium.')
        print(formatted_time)
        print('-' * 40)
        repeat = input("Would you like to run the program again (yes/no)? ")
        print('-' * 40)

def read_dictionary(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}
    try:
        with open(filename, "rt") as file_info:
            for i, info in enumerate(file_info):
                if i == 0: continue
                pNumber, pName, pPrice = info.strip().split(",")
                products_dict[pNumber] = (pName, pPrice)
        return products_dict
    except FileNotFoundError as file_not_found_error:
            print("Error: Missing file")
            print(type(file_not_found_error).__name__, file_not_found_error, sep=": ")
            sys.exit()
           
if __name__ == "__main__":
    main()