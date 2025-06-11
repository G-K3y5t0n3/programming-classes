'''
Files Checkpoint
Author: MJ Quizon
Last Updated: 11/25/24
'''
print('-' * 40)
with open('books.txt') as bOM:
    for books in bOM:
        clean_books = books.strip()
        print(clean_books)
print('-' * 40)