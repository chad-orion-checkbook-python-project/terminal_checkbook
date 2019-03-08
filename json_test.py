# JSON test code

import json


data = [{'trans_no': 3, 'trans': 10.00}, {'trans_no': 4, 'trans': 75.00}]

# read from
with open('transaction_history.json', 'r') as f:
    historical_trans = json.load(f)

# overwrite to
with open('transaction_history.json', 'w') as f:
    new_trans = historical_trans + data
    json.dump(new_trans, f)

# import json
# my_sum_total = 0
# with open('profiles.json') as f:
#     profile_data = json.load(f)


# loop through list of dictions
# find transaction # return trans amoutn
