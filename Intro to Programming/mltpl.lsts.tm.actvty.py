'''
Multiple Lists Team Activity
Author: MJ Quizon
Last Updated: 11/22/24
'''
bnk_accnt_nms = []
bnk_accnt_amnts = []
accnt_nm_inpt = ''
accnt_amnt_inpt = ''

print('-' * 40)
print('\nEnter the names and balances of bank accounts (type: quit when done)')
while accnt_nm_inpt != 'quit':
    accnt_nm_inpt = input('What is the name of this account? ')
    if accnt_nm_inpt != 'quit':
        bnk_accnt_nms.append(accnt_nm_inpt)
        accnt_amnt_inpt = float(input('What is the balance? '))
        bnk_accnt_amnts.append(accnt_amnt_inpt)

print('\nAccount Information:')
for names in range(len(bnk_accnt_nms)):
    print(f'{names + 1}. {bnk_accnt_nms[names]} - ${bnk_accnt_amnts[names]}')

accnt_ttl = sum(bnk_accnt_amnts)
accnt_ttl_avrg = sum(bnk_accnt_amnts) / len(bnk_accnt_amnts)

print(f'''\nTotal: {accnt_ttl}
Average: ${accnt_ttl_avrg:.2f}''')
print()
print('-' * 40)