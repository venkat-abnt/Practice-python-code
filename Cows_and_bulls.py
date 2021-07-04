'''
This Program randomly generates a desired length of number.
and then generates a randomd password which is a blend of alpha numeric and some special characters
'''
import random

def cows_and_bulls():
	(COWS,BULLS) = (0,0) #initialising cows & bulls to 0
	#CUS_NUM = input('Enter your guessing number: ')
	if CUS_NUM == GEN_NUM:
		print(f'****You won!! your guess is correct ****')
		return len(CUS_NUM),0
	else:
		for i in range(len(CUS_NUM)):
			if CUS_NUM[i] == GEN_NUM[i]:
				COWS +=1
			elif CUS_NUM[i] in GEN_NUM:
				BULLS +=1
			else:
				pass
		return COWS, BULLS

"""
This is where actuall game happens
"""
EMPTY_LIST = []
attempts = 0
cows = 0
bulls = 0
for x in range(4):
	EMPTY_LIST.append(str(random.randint(1,9)))#This will generate the 4 digit number, you canalways chnage it in the range so that length will varie accordingly
GEN_NUM = ''.join(EMPTY_LIST)
print(f'System generated number is: {GEN_NUM}')#commnet this out to hide the number 

while True:
	CUS_NUM = input('Enter your guessing number of %s digits: ' %len(GEN_NUM) )#using varibales inside the input function
	(COWS,BULLS) = cows_and_bulls()
	cows = cows + COWS
	bulls = bulls + BULLS 
	print(f'you have {COWS} cows & {BULLS} bulls in this attempt') #cows and bulls in this round of game
	attempts += 1
	if COWS == len(GEN_NUM):
		break
print(f'You took {attempts} attempts to make the correct guess')
print(f'By the end of the game you have {cows} cows & {bulls} bulls') #Total cows and bulls in the entire game
