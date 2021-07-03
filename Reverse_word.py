'''
This Program asks user input for a string
and reverse that 
'''

WORD = input('Enter your word/string: ')

'''
This func uses for loop and lists
'''
def reverse_fun():
	temp_list = []
	print(f'string is : {WORD}')
	for letter in WORD:
		temp_list.append(letter)
	temp_list.reverse()
	return temp_list

'''
this func uses string index
'''
def reverse_fun2():
	print('Method-2')
	return WORD[::-1]

'''
this func uses string index
'''

"""
calling the function here
"""
result = reverse_fun2() # call any one method of the above functions
print(result)

