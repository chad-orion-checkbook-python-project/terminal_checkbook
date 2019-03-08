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


welcome()





# def write_to_trans_log(transaction):
#     with open('transaction_history.txt', 'a') as f:
#         for listitem in transaction:
#             f.write('%s' % listitem)
# t = ['a', 'b', 'c'] # list to populates/append the transaction history
# write_to_trans_log(t)


# import json
# filename = file.text

# checkbook = [
#     {



#     }
# ]








# create list of values



# open and append to it

# with open('4.5_working_with_files.py', 'w') as f:
#     f.write('# 4.5_working_with_files.py \n# Hackney,_Chad \n# 07 Mar 19 \n#==============#')


# with open('file_name.txt', x) as f:
#     f.write('my message to display and write\n')



# Logging naming conventions

# # required fields
# trans_no #incrementing number, int
# trans #dollar value, float

# # optional add'l field
# running_total # incrementing number, float, populated in code
# date #now, date type, populated automatically on transaction
# time #now, time type, populated automatically on transaction
# trans_type # deposit or withdrawal, str, populated in code based on type of trans
# trans_desc #open text field for user input, str, populated via user input



