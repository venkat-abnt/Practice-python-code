#even or odd number

'''
Tells you whether a given number is even or odd
'''
NUM = int(input('Eneter a  number: '))
if NUM % 4 == 0:
	print(f' {NUM} is multiple of 4 and is even')
elif NUM % 2 == 0:
	print(f'given number {NUM} is Even')
else:
	print(f'given number {NUM} is Odd')
