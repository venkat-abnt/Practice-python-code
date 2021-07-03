'''
This Program asks user input for a number 
and generates fibonaci series till that number
'''

#user_num = int(input('Enter a number of your choice to generate Fibonacci series: '))

def fib_series(num):
	final_list = [0,1] # keeping 0 & 1 as part of logic to fibonacci sieries
	for i in range(num):
		count = final_list[-1] + final_list[-2]
		final_list.append(count)
	return final_list

"""
This is the main logic of the program
"""

user_num = int(input('Enter a number of your choice to generate Fibonacci series: '))
result = fib_series(user_num)
print(result)

