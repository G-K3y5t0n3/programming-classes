'''
Finding Items In A File Team Activity
Author: MJ Quizon
Last Updated 12/03/24
'''
largest_chapter_amount = -1
largest_book = ''

with open('books_and_chapters.txt') as info:
    for scripture in info:
        scripture_parts = scripture.strip().split(':')
        book = scripture_parts[0]
        chapter_amount = int(scripture_parts[1])
        scripture_source = scripture_parts[2]
        if chapter_amount > largest_chapter_amount:
            largest_chapter_amount = chapter_amount
            largest_book = book
        print(f'Scripture: {scripture_source}, Book: {book}, Chapters: {chapter_amount}')

print(f'The largest book in the scriptures is: {largest_book} with {largest_chapter_amount} chapters')

