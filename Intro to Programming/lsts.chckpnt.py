'''
Lists Checkpoint
Author: MJ Quizon
Last Updated: 11/14/24
'''
print('-' * 40)

frnd_lst = []
nm_inpt = '' 
while nm_inpt != 'end':
    nm_inpt = input('What are the names of your friends? ')
    if nm_inpt != 'end':
        frnd_lst.append(nm_inpt)

print()

for nms in frnd_lst:
    print(nms)

print('-' * 40)