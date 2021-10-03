message ='123456789'
def convert(str):
    rtr=0
    for int in message:
        rtr=rtr*10 + ord(int) - ord('0')
    print(rtr)
convert(message)

# def atoi(s):
#     rtr=0
#     for c in s:
#         rtr=rtr*10 + ord(c) - ord('0')
#         # 1
#         # 12
#         # 12345....
#         print('c:',ord(c),' 0:',ord('0'),' rts:',rtr,' rts*10:',rtr*10)
#     return rtr
# print(atoi('123456789'))
# print(ord('0'))