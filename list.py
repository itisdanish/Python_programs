# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create List
numbers = [1,2,3,4,5]
fruits =['Apples','Oranges','Grapes','Pears']

# Use a constructor
# numbers2 = list((1,2,3,4,5))

# Get Value
print(fruits)

# Insert
fruits.append('Mangoes')
fruits.insert(0, 'Test')
print(fruits)

# Remove
fruits.pop(0)
fruits.clear()
tuples =('one','Two')
temp = list(tuples)
temp.clear()
tuples=temp
print(temp)
print(tuples)