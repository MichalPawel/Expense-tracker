expenses = []


def show_expenses(month):
    for expense in expenses:
        if expense[2] == month:
            print(f'${expense[0]}, Type: {expense[1]}')


def add_expense(month):
    print()
    expense_amount = int(input("Input expense amount [USD]: "))
    expense_type = input(
        "Input expense type (food, entertainment, house, other): ")

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)


def show_stats(month):
    total_amount_this_month = sum(
        expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    total_amount_all = sum(
        expense_amount for expense_amount, _, _ in expenses)

    number_of_expenses_this_month = sum(
        1 for _, _, expense_month in expenses if expense_month == month)
    number_of_expenses_all = sum(
        1 for _, _, _ in expenses)

    average_expense_this_month = total_amount_this_month / number_of_expenses_this_month
    average_expense_all = total_amount_all / number_of_expenses_all

    print()
    print("Statistics: ")
    print(f'Total expenses this month: ${total_amount_this_month}')
    print(f'Total expenses: ${total_amount_all}')
    print(f'Average expense this month: ${average_expense_this_month}')
    print(f'Average expense: ${average_expense_all}')


while True:
    print()
    month = int(input("Choose a month [1-12]: "))

    while month < 0 or month > 12:
        month = int(input("Choose a month [1-12]: "))
    if month == 0:
        break

    while True:
        print()
        print("0. Return")
        print("1. Show all expenses")
        print("2. Add new expense")
        print("2. Show statistics")
        choice = int(input("Select an option: "))

        if choice == 0:
            break

        if choice == 1:
            show_expenses(month)

        if choice == 2:
            add_expense(month)

        if choice == 3:
            show_stats(month)
        if choice > 3 or choice < 0:
            print()
            print("Select correct option [0-3]")
