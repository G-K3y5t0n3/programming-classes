def main():
    products_dict = read_dictionary("products.csv")
    print(products_dict)
    print('\nRequested Items')
    with open("request.csv", "rt") as requests:
        for i, info in enumerate(requests):
            if i == 0: continue
            productID, product_amount = info.strip().split(",")
            print(f'{products_dict[productID][0]}: {product_amount} @ {products_dict[productID][1]}')

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
            products_dict[pNumber] = (pName, pPrice)
    return products_dict

# def create_request_list(filename):
#     requests = []
#     with open(filename, "rt") as request_info:
#         for i, info in enumerate(request_info):
#             if i == 0: continue
#             requests.append(info.strip().split(","))
#     return requests



if __name__ == "__main__":
    main()