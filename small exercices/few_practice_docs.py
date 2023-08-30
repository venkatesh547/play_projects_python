
# def sum_func(*args):
#     print(args)
#     return sum(args)
#
# print(sum_func(1,2,3))

# try:
#     x = int(input("Enter a number: "))
#     y = int(input("Enter another number: "))
#     result = x / y
#     print(result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")
# else:
#     print('result executes successfully')
#
# finally:
#     print('wanna try again ?')

# try:
#     x = int(input('Enter a num:: '))
#     y = int(input('Enter a num:: '))
#     res = x + y
#     print (res)
# except:
#     print('Something wrong! check the values')
# else:
#     print('All Good, wanna try again?')
# finally:
#     print('DONE')

#######################

# python code to print current time::
# import datetime
#
# current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
# print('Current Time: ', current_time)
# print (c_day)


# ex_str = 'this is a example string'
# l_str = ex_str.split()
# print(l_str)

###################

# def sum_func(*args, **kwargs):
#     total = 0
#     for item in kwargs.values():  # grabbing the values 10, 15 and do sum
#         total += item
#     return sum(args) + total
#
#
# print(sum_func(1, 2, 3, 4, num1=1, num2=1))

# Pepsico
# print('1' + '2' if '123'.isdigit() else '2'+'3' )

# Pepsico
# old_list=["john","amy","jules"]
# new_list=old_list
# new_list.append("emily")
# print(old_list)

# Pepsico
# dict_a = {"john":35, "jim":22, "jill":44}
# dict_copy = dict_a
# dict_copy['john'] = 40
# del dict_copy['john']
#
# print(dict_a['john'])

# question by passing 2 if condition - Pepsico
# a = [1, 'one', {2:'two'}, 3]
# b = len(a)
# if b == 4:
#     print('length of this list is 4')
# if b == 5:
#     print('length of this list is 5')
# else:
#     print(b)

# Python code to check Python is interpreter language - Pepsico
# python_func()
#
# def python_func():
#     print("This is a python function")

# list caption from Pepsico
# c = [1, 'hi', 2, 'hello', 3, 'greetings', 3.14159]
# for i in c:
#     if i == 3:
#         break
#     print(i,end = ' ')

# swapcase from Pepsico
# string = 'Happy, New, Year'
# new_string=string.str.swapcase()
# print (new_string)


# word count program from Tiger Analytics
# def word_count(str):
#     counts = dict()
#     words = str.split()
#
#     for i in words:
#         if i in counts:
#             counts[i] += 1
#         else:
#             counts[i] = 1
#     return counts
#
# print (word_count('the sun the'))

# to find sum of list
# list = [1, 4, 5, 2, 3, 7, 8, 1]
# tot = 0
# for i in list:
#     tot += i
#
# print(tot)

## program to print sum to next 2 consequitive number and find max of sum
# list = [1,7,8,6,5,3,5]
#
# max_sum = 0
# max_list = []
#
# for i in range(len(list)-1):
#     for j in range(i+1, len(list)):
#         sum = list[i]+list[j]
#         if sum>max_sum:
#             max_sum= sum
#             max_list=[list[i],list[j]]
#
# print ('max_sum: ', max_sum, 'max_list: ', max_list)


# list = [1, 3, 5, 2, 8, 6, 7, 7, 9, 11, 10]
# res_list = set(list)
# print (res_list)


# Python program to print duplicates from
# a list of integers
import copy

# lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
#
# uniqueList = []
# duplicateList = []
#
# for i in lis:
#     if i not in uniqueList:
#         uniqueList.append(i)
#     elif i not in duplicateList:
#         duplicateList.append(i)
#
# print(duplicateList)


# data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
# new_list = []
#
# while data_list:
#     minimum = data_list[0]  # arbitrary number in list
#     for x in data_list:
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     data_list.remove(minimum)
#
# print (new_list)

# l1 = [1,2,3,4]
# l2 = [5,6,7,3]
# # print(l1 + l2)
# res = l1.append(l2)
# print(res)

#############################

# def sqr(numb):
#     return numb**2
#
# lst = [2,3,4,5]
#
# res = list(map(sqr, lst))
# print(res)

###################################
## To find pairs in the list that sum up to the given number n=8
# def find_pairs(lst, target):
#     pairs = []
#     seen = set()
#
#     for num in lst:
#         complement = target - num
#
#         if complement in seen:
#             pairs.append((complement, num))
#
#         seen.add(num)
#
#     return pairs
#
#
# input_list = [1, 2, 4, 6, 5, 3, 7, 8]
# target_sum = 8
#
# result = find_pairs(input_list, target_sum)
#
# print(result)

##########################################################


# # To calculate the area of intersection between two circles,
# # you can use the following algorithm in Python:


# import math
#
#
# def calculate_area_of_intersection(x1, y1, r1, x2, y2, r2):
#     # Calculate the distance between the centers of the circles
#     d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
#     # Check for circle containment or no intersection
#     if d >= r1 + r2:
#         return 0
#
#     if d <= abs(r1 - r2):
#         r = min(r1, r2)
#         return math.pi * r ** 2
#
#     # Calculate the areas of the circle segments
#     theta1 = math.acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
#     theta2 = math.acos((r2 ** 2 + d ** 2 - r1 ** 2) / (2 * r2 * d))
#
#     area1 = 0.5 * theta1 * r1 ** 2 - 0.5 * r1 ** 2 * math.sin(2 * theta1)
#     area2 = 0.5 * theta2 * r2 ** 2 - 0.5 * r2 ** 2 * math.sin(2 * theta2)
#
#     # Calculate the area of intersection
#     intersection_area = area1 + area2
#
#     return intersection_area
#
#
# # Read the coordinates and radii of the two circles
# x1 = float(input())
# y1 = float(input())
# r1 = float(input())
# x2 = float(input())
# y2 = float(input())
# r2 = float(input())
#
# # Calculate the area of intersection between the two circles
# area_of_intersection = calculate_area_of_intersection(x1, y1, r1, x2, y2, r2)
#
# # Print the area rounded to 6 decimal places
# print(round(area_of_intersection, 6))

# basket = ('pears', 'pears', 'bananas')
#
# basket_dict = {}
#
# for item in basket:
#     if item in basket_dict:
#         basket_dict[item] += 1
#     else:
#         basket_dict[item] = 1
# print(basket_dict)

#############################

# # to print number of duplicates in list
# lst = [-25, 0, 25, 25, 1, 6, 8, 1, 4, 6, 4, 0]
#
# res_dict={}
#
# for i in lst:
#     if i in res_dict:
#         res_dict[i] += 1
#     else:
#         res_dict[i] = 1
# print(res_dict)
# # solution :: {-25: 1, 0: 2, 25: 2, 1: 2, 6: 2, 8: 1, 4: 2}
###############################################
# # to merge 2 list, we can use '+' operator

# list1 = [1,2,3]
# list2 = [4,5]
#
# print(list2 + list1)

#####################################
# # to print list in reverse
# x=[3,4,5,6,7,8,2]
# print(x[::-1])

###################################

# my_set = {1, 2, 3, 4, 5}
# my_lst = list(my_set)
# print(my_lst[1])
#
# for i in my_set:
#     print(i)
#
# # to print inputs each char in new line
# i = 'Venkatesh'
# for j in i:
#     print(j.lower())


##########################################

# # deep copy and shallow copy in list

# ls = [[1,1],[2,2],[3,3]]
# # ls1 = list(ls)
# # ls.append(6)
# # print('ls: ',ls)
# # print('ls1: ',ls1)
# ls2 = copy.copy(ls)
# ls.append([4,4])
# ls[1][1] = 'A,A'
# print('ls (after appending):',ls)
# print('ls2:',ls2)

#
# list = ['a','b','c','d','e']
# print(list[2:4])
# #solution : ['c', 'd']
########################################

# lst = [1,2,3,4]**2
# lst2 = [2,4,6,8]
# res = int(lst) **2
# print(res)
# it will throw error

# find max num from the list:
# lst = [2,3,4,79,5,6,1,8,5,12,45,6]
# lst2 = [-2,-3,-4,-79]
# res = lst[0]
# for i in lst:
#    if i > res:
#        res = i
# print(res)

# ## sorting
# lst = [2,3,4,79,5,6,1,8,5,12,45,6, -13, -35, 6, 122]
# res = []
#
# while lst:
#     mini_num = lst[0]
#     for i in lst:
#         if i < mini_num:
#             mini_num = i
#     res.append(mini_num)
#     lst.remove(mini_num)
#
# print(res)

# # reverse the string
# s= 'venkat'
# res = ''
# for i in s:
#     res = i+res
# print(res)

# method 2:

# s = 'venkat'
# print(s[::-1])

######################################################

# # #to print number of duplicates in a list
# list = ['a','b','c','d','e', 'b', 'd', 'b', 'b']
#
# res_lst = {}
#
# for i in list:
#     if i in res_lst:
#         res_lst[i] += 1
#     else:
#         res_lst[i] = 1
# print(res_lst)

# name = 'roshan'
# print(name[::-1])

# def col(x):
#     return x
#
# df.where(col('state'),'Delhi' & col('gender'),'Male')


# name = "PythonProgramming"
# print(name[6:33])


# str = 'google'
#
# res= {}
# for i in str:
# 	if i in res:
# 		res[i]+=1
# 	else:
# 		res[i]=1
#
# print(res)

# inp_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# def get_result(inp_list):
#   """
#   Gets the result of {'blue': [2, 4], 'red': [1], 'yellow': [1, 3]} from inp_list.
#
#   Args:
#     inp_list: The input list.
#
#   Returns:
#     The result dictionary.
#   """
#
#   result = {}
#   for color, value in inp_list:
#     result.setdefault(color, []).append(value)
#   return result
# print(get_result(inp_list))

# num_list = [1,2,3,4,5]
# num_list.remove(2)
# print(num_list)

