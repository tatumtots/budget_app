# function for storing income
def monthly_income(income_list, income):
    income_list.append(income)
    return income_list


def get_income_total(income_list):
    total = 0
    for inc in income_list:
        total += int(inc)
    return total


def print_income(income_list):
    for inc in income_list:
        print(inc)
