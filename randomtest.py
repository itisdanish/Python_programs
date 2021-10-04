list = ['Name','Type']
data = ['Danish','Trainee']

emp={}
for key in list:
    for value in data:
        emp[key] = value
        data.remove(value)
        break
print(emp)