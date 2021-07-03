'''
This is a Guessing Game where user guess a number randomly
If the guess is correct means he won the game
'''
import random
#actual_num = random.randint(1,9)
#guess_num = int(input('enter your guessing number b/w(0-9): ') )
choice = ''
number_of_guesses = 0
'''
defing a function
'''
def guess_num_game():
	if actual_num == guess_num:
		print(f'Your guess is correct.\n actual number is: {actual_num} \n your guess is: {guess_num}')
	else:
		print(f'Your guess is wrong.\n actual number is: {actual_num} \n your guess  is: {guess_num}')
		if abs(actual_num - guess_num) < 2:
			print('your are alomost there')
		else:
			print('your guess is too far from actual number')

"""
Actual game logic is below.
Written in such a way that it keeps on asking for the guess untill correctly predicted
if the guess is correct then immedialtely game stops
and displays how many attempts you took to guess corectly.
"""
#while choice != 'exit':
while True:
    actual_num = random.randint(1,9)
    guess_num = int(input('enter your guessing number b/w(0-9): ') )
    '''
    Calling the Guess num game function
    '''
    guess_num_game()
    number_of_guesses += 1
    #choice = input('do you want to continuie the play?')
    if actual_num == guess_num:
    	break

print(f'you have taken {number_of_guesses} guesses for correct prediction')