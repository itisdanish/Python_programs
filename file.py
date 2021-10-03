from os import write



myFile = open('myFile.txt','w')

print('Name: ', myFile.name)

myFile.write('Pythons')