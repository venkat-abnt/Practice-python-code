#Less than five

'''
Print all the elements in a list which are less than five
'''
input_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
final_list = []
NUM = int(input('enter a number: '))
#for i in input_list:
#	if i < 25 and i < NUM:
#		final_list.append(i)
#print(final_list)
'''
Instead of using above multiple lines of code which are commented
we can do it in a single line of code
using list comprehensions
'''
new_list = [i for i in input_list if i < 15 and i < NUM ]
print(new_list)

