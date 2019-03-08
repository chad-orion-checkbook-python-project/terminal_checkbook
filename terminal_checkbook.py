# This is the terminal_checkbook.py file

import time
import sys
# time
# pprint

MENU_OPTIONS = '12345'

# Welcome function


def welcome():
    print('~~~ Welcome to your terminal checkbook ~~~\n\n')
    main_menu()

# Exit function


def exit_method():
    print('~~~ Thank you for banking with Chad\'s Wallet! ~~~')
    exit()

# Input validation


def menu_selection(user_selection):
    if user_selection in MENU_OPTIONS:
        return user_selection
    if user_selection not in MENU_OPTIONS:
        print(f'Sorry but {user_selection} is not a valid option.  Try again.')
        selection = input('What would you like to do? ')
        return menu_selection(selection)
    print('user selected {}'.format(selection))  # error checking
    return user_selection


# Sub menu prompt


# Menu items
def main_menu():
    print('1) view current balance')
    print('2) record a withdrawl')
    print('3) record a deposit')
    print('4) exit\n')
    selection = input('What would you like to do? ')
    menu_selection(selection)
    # if user_selection == 4:
    #     exit_method()
# Logging naming conventions


<<<<<<< HEAD
welcome()
=======


# Logging naming conventions

# required fields
trans_no #incrementing number, int
trans #dollar value, float

# optional add'l field
running_total # incrementing number, float, populated in code
date #now, date type, populated automatically on transaction
time #now, time type, populated automatically on transaction
trans_type # deposit or withdrawal, str, populated in code based on type of trans
trans_desc #open text field for user input, str, populated via user input



>>>>>>> e17bbb66f2e677876d50b5e53aa3f8231271a42b
