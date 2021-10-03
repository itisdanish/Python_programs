check = input()
check_list = list(check)
check_set = set(check)
check_list2 = list(check_set)
list3 = check_list - check_list2
print(set(list3))
# check_again = list(check_set)
# output = len(check_list) - len(check_set)
# # print(output)
# # print(f'User Input is {check} \n')
# # print(f'List Input is {check_list} \n')
# # print(f'Set Input is {check_set} \n')

# # Python program to find the common elements
# # in two lists
# def common_member(a, b):
#     a_set = set(a)
#     b_set = set(b)
 
#     if (a_set & b_set):
#         print(len(a_set & b_set) - output)
#     else:
#         print("No common elements")
          
  
# a = [1, 2, 3, 6, 5]
# b = [5, 6, 7, 8, 9]
# common_member(check_list, check_again)
  
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9]
# common_member(a, b)