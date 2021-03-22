from income import *
from transactions import *

if __name__ == '__main__':

    income_list = []
    transaction_list = []


    def menu_selection():
        menu_select = input('Choose from menu: \n 1. Add Income \n 2: Add Transaction \n ')
        if menu_select == '1':
            add_income()
        elif menu_select == '2':
            add_transaction()


    def add_income():
        another_income = True
        global income_list
        while another_income:
            income = float(input('Add income: '))
            income_list = monthly_income(income_list, income)
            if input('Do you want to add more income?').lower() == 'no':
                another_income = False
                menu_selection()


    def add_transaction():
        another_transaction = True
        global transaction_list
        while another_transaction:
            transaction = float(input('Add transaction: '))
            transaction_list = monthly_transactions(transaction_list, transaction)
            if input('Do you want another transaction?').lower() == 'no':
                another_transaction = False
                menu_selection()


    # def print_income_total(income_list):
    #     print(income_list)

    # def print_transaction_list(transaction_list):
    #     print(transaction_list)

    menu_selection()
    print("Transaction Total: " + str(get_transaction_total(transaction_list)))
