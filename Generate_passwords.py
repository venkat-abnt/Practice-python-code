'''
This Program asks user for desired length of their passwords
and then generates a randomd password which is a blend of alpha numeric and some special characters
'''
possible_values = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?'

capacity = input('How do you need your password(week,strong):  ')
import random

def pwd_gen():
    '''
    Random.choices generates some random values 
    from possible_values by length of k which is mentioned below.
    '''
    if capacity.lower() == 'week':
    	temp_pwd = random.choices(possible_values, k=random.randint(3,5))
    	main_pwd = ''.join(temp_pwd)
    	return main_pwd
    else:
    	length = int(input('What should be the length of your password?  '))
    	temp_pwd = random.choices(possible_values, k=length)
    	main_pwd = ''.join(temp_pwd)
    	return main_pwd
"""
Call the password generator generator fucntion defined above
for a new password which is a long of your choice
"""
password = pwd_gen()
print('Your new password is: {}'.format(password))
