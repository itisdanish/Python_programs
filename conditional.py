
numbers=[1,21,3,4,5,2,10]
x=int(input('x is \n'))
y=int(input('y is \n'))
print(f'X is {x} and Y is {y}\n')
if y and x in numbers:
    print('x and y Found')
    if x is y:
        print('Both are same')    
elif x in numbers:
    print('X Found')
elif y in numbers:
    print('Y Found')
else:
    print('Not Found')