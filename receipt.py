# def main():
#     products_dict = read_dictionary()
#     pass

def read_dictionary(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}
    with open(filename, "rt") as file_info:
        for i, info in enumerate(file_info):
            if i == 0: continue
            pNumber, pName, pPrice = info.strip().split(",")
            products_dict[pNumber] = pPrice
    return products_dict

products_dict = read_dictionary("products.csv")
print(products_dict)