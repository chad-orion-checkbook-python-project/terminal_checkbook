#JSON test code

import json


data = {'trans_no': 3, 'trans': 100.00}, {'trans_no': 4, 'trans': 50.00}
with open('transaction_history.json', 'w') as f:
    orion = json.dumps(data, indent=4)
    chad = dict.update(data)
print(chad)


with open('transaction_history.json') as f:
    data = json.load(f)
    for record in data:
        transaction = record['trans']
    print(transaction)

# import json
# my_sum_total = 0
# with open('profiles.json') as f:
#     profile_data = json.load(f)



# loop through list of dictions
# find transaction # return trans amoutn





