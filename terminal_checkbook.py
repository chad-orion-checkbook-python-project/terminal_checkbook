# This is the terminal_checkbook.py file

import time
import sys
import json
# time
# pprint

MENU_OPTIONS = ('1', '2', '3', '4', '5')

# Welcome function


def welcome():
    print('~~~ Welcome to your terminal checkbook ~~~\n\n')
    main_menu()

# Exit function


def exit_method():
    print('~~~ Thank you for banking with Chad\'s Wallet! ~~~')
    exit()


# Menu items
def main_menu():
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
        print('user selected view balance')
        view_balance()
    if selection == '2':
        print('user selected to withdrawl')
        user_withdrawl()
    if selection == '3':
        print('user selected to deposit')
        user_deposit()
    if selection == '4':
        print('user selected additional info')
    if selection == '5':
        exit_method()

# View Balance Menu


# def get_balance():
#     balance = 0
#     return balance


def view_balance():
    balance = 0
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)
        for i in historical_trans:
            balance = balance + i['trans_amount']
    print(f'Your current balance is: ${balance}')

    # amount_to_view = input('How many transactions would you like to view? ')

    # with open('transaction_history.txt') as f:
    #     msg = f.read()
    #     print(msg)

# Withdrawl menu


def user_withdrawl():
    amount_to_withdrawl = float(
        input('How much are you withdrawling? (ex. $50.25) '))
    amount_to_withdrawl = amount_to_withdrawl * -1
    print(f'user entered withdrawl amount of {amount_to_withdrawl}')
    withdrawl_transaction = [{'trans_no': get_trans_no(),
                              'trans_type': 'deposit', 'trans_amount': amount_to_withdrawl}]
    execute_withdrawl(withdrawl_transaction)
    # goto withdrawl_transaction

# Deposit menu


def get_trans_no():
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)
        trans_no = historical_trans[-1]['trans_no']
        return int(trans_no) + 1


def user_deposit():
    amount_to_deposit = float(
        input('How much are you depositing? (ex. $50.25) '))
    print(f'user entered deposit amount of {amount_to_deposit}')
    deposit_transaction = [{'trans_no': get_trans_no(),
                            'trans_type': 'deposit', 'trans_amount': amount_to_deposit}]
    execute_deposit(deposit_transaction)
# Additional information menu


def additional_info_menu():
    print('1) option 1')
    print('2) option 2')
    print('3) option 3')
    print('4) option 4')

# database stuff
# data = [{'trans_no': 3, 'trans': 10.00}, {'trans_no': 4, 'trans': 75.00}]

# read from


def execute_deposit(trans_list):
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)

    # overwrite to
    with open('transaction_history.json', 'w') as f:
        new_trans = historical_trans + trans_list
        json.dump(new_trans, f)


def execute_withdrawl(trans_list):
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)

    # overwrite to
    with open('transaction_history.json', 'w') as f:
        new_trans = historical_trans + trans_list
        json.dump(new_trans, f)


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
