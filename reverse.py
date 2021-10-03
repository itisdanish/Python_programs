message = 'Hello World'
def reverse(txt):
    str=''
    for word in message:
        str=word+str
    print(str)

reverse(message)



# name = input('Check whether is String is Palindron or Not\n').upper()
# def isp(str):
#     temp = str[::-1].upper()
#     print(temp)
#     if temp == str:
#         print('Yes')
#     else:
#         print('No')
# isp(name)
# print(name)