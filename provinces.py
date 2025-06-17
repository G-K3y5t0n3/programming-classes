def main():
    cleaned_provinces_list = create_list("provinces.txt")
    for province in cleaned_provinces_list:
        print(cleaned_provinces_list)
    #
    # cleaned_provinces_list.pop(0)
    # print(cleaned_provinces_list)
    # #
    # cleaned_provinces_list.pop()
    # print(cleaned_provinces_list)

def create_list(filename):
    cleaned_provinces_list = []
    provinces_list = open(filename, "rt")
    for province in provinces_list:
        cleaned_province = province.strip()
        cleaned_provinces_list.append(cleaned_province)
    return cleaned_provinces_list

if __name__ == "__main__":
    main()