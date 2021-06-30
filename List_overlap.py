#List overlap of two lists

'''
This will give you a list of all elements common in both the lists
'''

#if user has to provide the list input

'''
list1 = list(input('Enter some  list elements of your choice for list1: '))
print(f'This is list1: {list1}\n')
list2 = list(input('Enter some  list elements of your choice for list2: '))
print(f'This is list2: {list2}\n')
'''

# if lists have to be generated randomly

import random
list3 = [random.randint(1,30) for i in range(1,10)] #will give  alist of 10 elements b/w 1 to 30
print(f'This is list1: {list3}\n')

list4 = [random.randint(1,20) for i in range(1,8)] #will give  alist of 8 elements b/w 1 to 20
print(f'This is list1: {list4}\n')

new_list = [i for i in list3 if i in list4]
print(f'common elements from both the lists are: \n {new_list}')

