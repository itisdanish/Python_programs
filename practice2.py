color_list = ['Red','Blue','Yellow','Test','Green','Yellow','Test']
color = ()

# Length
# color_list[1]='Black'
# userInput = int(input('Add Some List\n'))
# Get Value
# n = int(input("Element : "))

# for i in range(n):
#     ele = input('Enter List : ')
#     color.append(ele)
#     print('Inserted : ',i+1)

print(color_list)
color_set = set(color_list)
color_uniq = list(color_set)
color_uniq[1]='Sample'
print(color_set)
print(color_uniq)
print(set())