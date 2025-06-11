'''
List of Numbers Team Activity
Author: MJ Quizon
Last Updated: 11/14/24
'''
nmbr_lst = []
nmbr_inpt = ''
print('-' * 40) 
print('Enter a list of numbers, type 0 when finshed.')
while nmbr_inpt != 0:
    nmbr_inpt = int(input('Enter number: '))
    if nmbr_inpt != '0':
        nmbr_lst.append(nmbr_inpt)

lst_sm = sum(nmbr_lst)
print(f'The sum is: {lst_sm}')

lst_avrge = sum(nmbr_lst)/len(nmbr_lst)
print(f'The average is: {lst_avrge}')

# lrgst_nmbr = 0
# for nmbrs in nmbr_lst:
#     if nmbrs > lrgst_nmbr:
#         lrgst_nmbr = nmbrs

lrgst_nmbr = max(nmbr_lst)
print(f'The largest number is: {lrgst_nmbr}')
