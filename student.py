def main():
    repeat = ''
    clean_student_info = read_dictionary("students.csv")
    while repeat != "no":
        i_number = input("Please enter an I-Number (xxxxxxxxx): ")
        if i_number in clean_student_info:
            student_name = clean_student_info[i_number]
            print(student_name)

        else:
            print(f"There is no such student with the I-Number: {i_number} ")
        repeat = input("Would you like to search for another I-Number (yes/no)? ")

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    clean_student_info = {}
    with open(filename, "rt") as student_info:
        for i, info in enumerate(student_info):
            if i == 0: continue #Skips the first line
            iNumber, student_name = info.strip().split(",")
            clean_student_info[iNumber] = student_name
    return clean_student_info

if __name__ == "__main__":
    main()