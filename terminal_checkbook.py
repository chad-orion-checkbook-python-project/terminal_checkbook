# This is the terminal_checkbook.py file

import datetime
import time
import sys
import json
from pprint import pprint

MENU_OPTIONS = ('1', '2', '3', '4', '5')

# Welcome function


def welcome():
    print('~~~ Welcome to your terminal checkbook ~~~\n\n')
    main_menu()

# Exit function


def exit_method():
    print('\n~~~ Thank you for banking with Chad\'s Wallet! ~~~')
    exit()


# Menu items
def main_menu():
    print('\n Welcome to the Main Menu\n\n')
    print('1) view current balance')
    print('2) record a withdrawl')
    print('3) record a deposit')
    print('4) additional info')
    print('5) exit\n')
    selection = input('What would you like to do? ')
    if selection not in MENU_OPTIONS:
        print(
            f'Sorry but {selection} is not a valid option.  Returning to Main Menu.\n\n')
        main_menu()
    if selection == '1':
        # print('user selected view balance')
        view_balance()
    if selection == '2':
        # print('user selected to withdrawl')
        user_withdrawl()
    if selection == '3':
        # print('user selected to deposit')
        user_deposit()
    if selection == '4':
        # print('user selected additional info')
        additional_info_menu()
    if selection == '5':
        exit_method()

# View Balance Menu


def view_balance():
    balance = 0
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)
        for i in historical_trans:
            balance = balance + i['trans_amount']
    print(f'Your current balance is: ${balance}\n\n')
    main_menu()


# Withdrawl menu


def user_withdrawl():
    amount_to_withdrawl = float(
        input('How much are you withdrawling? (ex. $50.25) '))
    amount_to_withdrawl = amount_to_withdrawl * -1
    print(f'user entered withdrawl amount of {amount_to_withdrawl}')
    trans_date = trans_date_time()
    withdrawl_transaction = [{'trans_no': get_trans_no(),
                              'trans_type': 'withdrawl', 'trans_amount': amount_to_withdrawl, 'date_and_time': trans_date}]
    execute_withdrawl(withdrawl_transaction)
    # goto execute_withdrawl


# transaction number iterator
def get_trans_no():
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)
        trans_no = historical_trans[-1]['trans_no']
        return int(trans_no) + 1

# user deposit request


def user_deposit():
    amount_to_deposit = float(
        input('How much are you depositing? (ex. $50.25) '))
    print(f'user entered deposit amount of {amount_to_deposit}')
    trans_date = trans_date_time()
    deposit_transaction = [{'trans_no': get_trans_no(),
                            'trans_type': 'deposit', 'trans_amount': amount_to_deposit, 'date_and_time': trans_date}]
    execute_deposit(deposit_transaction)
    # goto execute_deposit

# Additional information menu


def additional_info_menu():
    print('\n Additional Information Menu\n\n')
    # print('1) See previous transactions')
    print('1) View all transactions')
    print('2) Return to Main Menu\n\n')
    selection = input('What would you like to do?\n')
    if selection not in MENU_OPTIONS:
        print(
            f'Sorry but {selection} is not a valid option.  Returning to Main Menu.\n\n')
        main_menu()
    # if selection == '1':
    #     see_prev_transactions()
    if selection == '1':
        print_all_transactions()
    if selection == '2':
        main_menu()

# execute the deposit


def execute_deposit(trans_list):
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)

    # overwrite to
    with open('transaction_history.json', 'w') as f:
        new_trans = historical_trans + trans_list
        json.dump(new_trans, f)
    view_balance()
    main_menu()

# execute the withdrawl


def execute_withdrawl(trans_list):
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)

    # overwrite to
    with open('transaction_history.json', 'w') as f:
        new_trans = historical_trans + trans_list
        json.dump(new_trans, f)
    view_balance()
    main_menu()

# print all transactions


def print_all_transactions():
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)
    pprint(historical_trans)
    additional_info_menu()

# return n-number of previous transactions:


def see_prev_transactions():
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)
        selection = input(
            'How many previous transactions would you like to view? ')
        if not selection.isdigit():
            print(
                f'Sorry but {selection} is not a valid option.  How many previous transactions would you like to view?\n\n')
        else:
            # trans_no = historical_trans[-1]['trans_no']
            print(f'Most recent {selection} transactions shown below:')
            # selection = int(selection)
        for i in historical_trans:

            if historical_trans['trans_no'] == selection:
                pprint(i)
    new_selection = historical_trans[-(selection)]  # ['trans_no']
    pprint(new_selection)
    additional_info_menu()


# date and time of transaction:
def trans_date_time():
    date_time = datetime.datetime.now().strftime("%m-%d-%y  %I:%M %p")
    return date_time


def find_trans_range():
    max = max(historical_trans['trans_no'])
    return max


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

# required fields
# trans_no  # incrementing number, int
# trans  # dollar value, float

# # optional add'l field
# running_total  # incrementing number, float, populated in code
# date  # now, date type, populated automatically on transaction
# time  # now, time type, populated automatically on transaction
# trans_type  # deposit or withdrawal, str, populated in code based on type of trans
# trans_desc  # open text field for user input, str, populated via user input


# email functionality?
# import smtplib

# TO = 'recipient@mailservice.com'
# SUBJECT = 'TEST MAIL'
# TEXT = 'Here is a message from python.'

# # Gmail Sign In
# gmail_sender = 'sender@gmail.com'
# gmail_passwd = 'password'

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.ehlo()
# server.starttls()
# server.login(gmail_sender, gmail_passwd)

# BODY = '\r\n'.join(['To: %s' % TO,
#                     'From: %s' % gmail_sender,
#                     'Subject: %s' % SUBJECT,
#                     '', TEXT])

# try:
#     server.sendmail(gmail_sender, [TO], BODY)
#     print ('email sent')
# except:
#     print ('error sending mail')
# # required fields
# trans_no #incrementing number, int
# trans #dollar value, float

# # optional add'l field
# running_total # incrementing number, float, populated in code
# date #now, date type, populated automatically on transaction
# time #now, time type, populated automatically on transaction
# trans_type # deposit or withdrawal, str, populated in code based on type of trans
# trans_desc #open text field for user input, str, populated via user input
