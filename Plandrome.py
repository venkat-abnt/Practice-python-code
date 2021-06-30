#Palandrome

'''
This will tell  you give string is a plandrome or not
'''

WORD = input('Enter a string of your choice: ')
NEW_WORD =  WORD[::-1]
if WORD == NEW_WORD:
	print(f'given word "{WORD}" is a palandrome')
else:
	print('given word "{}" is not palandrome'.format(WORD) )