# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

people=['John','Harry','Ron','Rob']
print(people)
ser = input('Search: ')

for name in people:
    if name == ser:
        print(f'{ser} found')
        print(people)
        people[name]='Update'
        print(f'{ser} Updated')
        print(people)
    else:
        print('Task completed')
