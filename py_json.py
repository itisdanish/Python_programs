# JSON is commonly used with data Apis

import json

# Sample JSON
userJSON = '{"first_name": "Danish", "last_name": "Iqbal", "age":26}'

# Parse to dict

user = json.loads(userJSON)
# print(userJSON['age'])
print(user)
print(user)
print(user['age'])