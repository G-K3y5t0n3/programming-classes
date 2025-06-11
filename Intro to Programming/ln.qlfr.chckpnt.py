'''
Qualifying for a Loan Checkpoint Assignment
Last Updated: 10/24/24
Author: Michael Jacob (MJ) Quizon

Write a program to determine whether to loan money based on the following rules:

First, ask for a rating from 1–10 on the following:
    How large is the loan?
    How good is your credit history?
    How high is your income?
    How large is your down payment?

Then, you will create a boolean variable for whether you should loan the money that will be set to either True or False. 
Set up a series of if statements to decide if your decision to loan is "yes" or "no" according to the following rules:
    First, check if the loan size is at least 5. If it is, use the following rules:
    If the credit history and income are both at least 7, then the decision is "yes"
    If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"
    Otherwise (if neither the credit history nor income is at least 7), the decision is "no"

Otherwise (if the loan is not 5 or greater), use these rules:
    If the credit is less than 4, then the decision is "no"
    Otherwise, check the following:
        If either the income or the down payment is at least 7, the decision is "yes"
        If both the income and the down payment are at least 4, then the answer is "yes"
        Otherwise, the decision is "no"

Finally, display the decision to the user.
'''
print('-' * 40)
print('\nNote: Please respond to the following questions with a scale rating of 1-10')
ln_sz = int(input('\nHow large is your loan? '))

if ln_sz >= 5:
    crdt_hstry = int(input('\nHow reliable is your credit history? '))
    ncm_sz = int(input('How large is your income? '))
    if crdt_hstry >= 7 and ncm_sz >= 7:
        dp_sz = int(input('How big will your down payment be? '))
        fnl_dcsn = "Yes"
    elif crdt_hstry >= 7 or ncm_sz >= 7:
        dp_sz = int(input('How big will your down payment be? '))
        if dp_sz >= 5:
            fnl_dcsn = "Yes"
        else:
            fnl_dcsn = 'No'
    else:
        fnl_dcsn = 'No'
else:
    crdt_hstry = int(input('\nHow reliable is your credit history? '))
    if crdt_hstry < 4:
        fnl_dcsn = "No"
    else:
        ncm_sz = int(input('How large is your income? '))
        dp_sz = int(input('How big will your down payment be? '))
        if ncm_sz >= 7 or dp_sz >= 7:
            fnl_dcsn = 'Yes'
        elif ncm_sz >= 4 and dp_sz >= 4:
            fnl_dcsn = 'Yes'
        else:
            fnl_dcsn = 'No'

if fnl_dcsn == 'Yes':
    print('''Congratulations! Your loan has been approved!''')
elif fnl_dcsn == 'No':
    print('''Apologies. We cannot approve your loan at this point in time.
    Please try somewhere else. Enjoy the rest of your day''')