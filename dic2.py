#  Dictionary in Python
# Dictionary is a collection which is unordered, Changeable and Indexed (by Keys), No Duplicate allow

tcs={
    'Ceo':'Rajesh Gopinathan',
    'HeadQ':'Mumbai',
    'Founded':'1 April 1968',
    'Founders':{'Tata Sons','Faquir Chand Kohli','JRD TATA'},
    'Employee':'5'
}
print('Tata Sons' in tcs['Founders'])
# add
tcs['type']='IT-MNC'
print(tcs)