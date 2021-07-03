'''
This Program asks user input for a number 
and decides whetehr it is prime or not
'''

user_num = int(input('Enter a number of your choice: '))

"""
In this method am using a list to decide
"""
def prime_fun(user_num):
    print('This is method 1')
    temp_list = []
    for i in range(2,user_num):
    	if user_num % i == 0:
    		temp_list.append(i)
    if len(temp_list) == 0:
	    print(f'{user_num} is Prime')
    else:
	    print(f'{user_num} is not a prime')

'''
In this am directly deciding based on the divisibility of the number
if the number id divisible by nay of the number in the range then not a prime
'''

def prime_func_method2(user_num):
	print('This is method 2')
	for i in range(2,user_num):
		if user_num % i == 0:
			return str(user_num) + ' is not a prime'
	return str(user_num) + ' is prime'

"""
Calling the actual function here
"""
#prime_fun(user_num)

result = prime_func_method2(user_num)
print(result)

	