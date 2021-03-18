from income import *
from transactions import *

if __name__ == '__main__':
    transaction_list = []
    income_list = []
    another_transaction = True
    another_income = True

    while another_income:
        income = float(input('Add income: '))
        income_list = monthly_income(income_list, income)
        if input('Do you want to add more income?').lower() == 'no':
            another_income = False

    while another_transaction:
        transaction = input('Add transaction: ')
        transaction_list = monthly_transactions(transaction_list, transaction)
        if input('Do you want another transaction?').lower() == 'no':
            another_transaction = False

    print("Transaction Total: " + str(get_transaction_total(transaction_list)))

    print_transactions(transaction_list)

