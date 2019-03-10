import datetime
import time

# date and time of transaction:
def trans_date_time():
    print("Transaction date and time: " ,datetime.datetime.now().strftime("%m-%d-%y  %I:%M %p"))

trans_date_time()


# return n-number of previous transactions:
def see_prev_transactions():
    with open('transaction_history.json', 'r') as f:
        historical_trans = json.load(f)
        selection = input('How many previous transactions would you like to view? ')
        if not isalnum(selection):
            print(
                 f'Sorry but {selection} is not a valid option.  How many previous transactions would you like to view?\n\n')      
        else:
        int(trans_no) = historical_trans[-1]['trans_no']
            print('Most recent {selection} transactions shown below:')
        selection = int(selection)
        return new_selection = historical_trans[-selection:]['trans_no']
            print(new_election)
            print('Returning to the main menu.\n\n')
        main_menu()


