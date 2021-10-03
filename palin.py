input = input('Check Palindrome : ').upper()
def isPalin(txt):
    str=''
    for ele in txt:
        str=ele+str
    if str == input:
        print('Yes,it is')
    else:
        print('No,it is not')
isPalin(input)
# input = 'radar'
# if input == input[::-1]:
#     print('Yes')
# else:
#     print('No')
# print(input[::-1])