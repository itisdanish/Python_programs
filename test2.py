# # from typing import List
# # tcs={
# #     'Ceo':'Rajesh Gopinathan',
# #     'HeadQ':'Mumbai',
# #     'Founded':'1 April 1968',
# #     'Founders':['Tata Sons','Faquir Chand Kohli','JRD TATA'],
# #     'Employee':'5'
# # }
# # list = [(k, v) for k, v in tcs.items()]
# info = ['Rajesh Gopinathan', 'Mumbai', '1 April 1968', ['Tata Sons', 'Faquir Chand Kohli', 'JRD TATA'], '5']
# info1 = ['Ceo', 'HeadQ', 'Founded', 'Founders', 'Employee']
# test ={}
# for key in info1:
#     for value in info:
#         test[key] = value
#         info.remove(value)
#         break
# print(test)
n = 4562
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print(rev)