'''
This is a rock , paper,scissors game where two players play and one wins
In this game, one of the below happens
Rock beats scissors
Scissors beat paper
Paper beats Rock
'''
import random
Game_list = ['Rock', 'scissors', 'paper']
player1_score = 0
player2_score = 0
round_num = 1
#Game_On = True
MAX_POINTS = int(input('for how many points, you guys want to play the Game: '))

'''function to deide the winner'''
def game_func(player1, player2):
    if player1 == player2:
	    return "Tie Match"
    elif player1 == 'Rock' and player2 == 'scissors':
	    return 'Player1 wins'
    elif player1 == 'Rock' and player2 == 'paper':
        return 'Player2 wins'
    elif player1 == 'scissors' and player2 == 'Rock':
        return 'Player2 wins'
    elif player1 == 'scissors' and player2 == 'paper':
        return 'Player1 wins'
    elif player1 == 'paper' and player2 == 'Rock':
        return 'Player1 wins'
    elif player1 == 'paper' and player2 == 'scissors':
        return 'Player2 wins'

while player1_score < MAX_POINTS and player2_score < MAX_POINTS:
	random.shuffle(Game_list)
	print(f' Round Number {round_num} : ')
	choice1 = int(input('Player1, please choose b/w (0,1,2): '))
	choice2 = int(input('Player2, please choose b/w (0,1,2): '))
	player1 = Game_list[choice1]
	print(f'player1 value is: {player1}')
	player2 = Game_list[choice2]
	print(f'player2 value is: {player2}')
	'''
	Call the game function defined above
	'''
	#print('Executing the game function')
	
	result = game_func(player1, player2)
	print(result)
	if result == 'Player1 wins':
		player1_score += 1
	elif result == 'Player2 wins':
		player2_score += 1
	round_num += 1
	print(f'Player1 score is : {player1_score}')
	print(f'Player2 score is : {player2_score}')
	print('\n')

"""
Based on the final score deciding the winner of the Game
"""
if player1_score > player2_score:
	print('Final Winner is PLAYER-1')
else:
	print('Final Winner is PLAYER-2')

	

	#ANSWER = input('do you want to play again: ')
	#if ANSWER not in ['YES', 'Yes', 'yes', 'Y', 'y']:
	#	Game_On = False






	
