# function for storing transaction
def monthly_transactions(transaction_list, transaction):
    transaction_list.append(transaction)
    return transaction_list


def get_transaction_total(transaction_list):
    total = 0
    for trans in transaction_list:
        total += int(trans)
    return total


def print_transactions(transaction_list):
    for trans in transaction_list:
        print(trans)

