'''
This is a rock , paper,scissors game where two players play and one wins
In this game, one of the below happens
Rock beats scissors
Scissors beat paper
Paper beats Rock
'''
import random
Game_list = ['Rock', 'scissors', 'paper']
Game_On = True

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

while Game_On:
	random.shuffle(Game_list)
	choice1 = int(input('Player1, please choose b/w (0,1,2): '))
	choice2 = int(input('Player2, please choose b/w (0,1,2): '))
	player1 = Game_list[choice1]
	print(f'player1 value is: {player1}')
	player2 = Game_list[choice2]
	print(f'player2 value is: {player2}')
	'''
	Call the game function defined above
	'''
	print('Executing the game function')
	result = game_func(player1, player2)
	print(result)

	ANSWER = input('do you want to play again: ')
	if ANSWER not in ['YES', 'Yes', 'yes', 'Y', 'y']:
		Game_On = False






	
