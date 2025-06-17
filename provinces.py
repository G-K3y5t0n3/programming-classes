# from pprint import pprint

def main():
    alberta_count = 0
    cleaned_provinces_list = create_list("provinces.txt")
    # for province in cleaned_provinces_list:
    #     print(province)
    #   pprint(cleaned_provinces_list)
    #
    cleaned_provinces_list.pop(0)
    #
    cleaned_provinces_list.pop()
    #
    for provinces in range(len(cleaned_provinces_list)):
        if cleaned_provinces_list[provinces] == "AB":
            cleaned_provinces_list[provinces] = "Alberta"
    #
    print(cleaned_provinces_list)
    #
    alberta_count = cleaned_provinces_list.count("Alberta")
    print(f'\nAlberta occurs {alberta_count} times in the modified list')

def create_list(filename):
    cleaned_provinces_list = []
    with open(filename, "rt") as provinces_list:
        for province in provinces_list:
            cleaned_province = province.strip()
            cleaned_provinces_list.append(cleaned_province)
    return cleaned_provinces_list

if __name__ == "__main__":
    main()