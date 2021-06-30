#divisor of a number

'''
This will give you a list of all divisors of a numbers 
'''

#new_list = []
NUM = int(input('Enter number of your choice: '))
#for i in range(2,101): #not considering 0 and 1 as we canot divide any number by 0 and every number is divisible by 1
#	if NUM % i ==0:
#		new_list.append(i)
#print(new_list)
new_list = [i for i in range(2,NUM+1) if NUM % i == 0]
print(new_list)

