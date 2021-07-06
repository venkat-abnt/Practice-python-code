"""
This is the Tik Tok Toe game.
In this game, we will have 2 players playing the game.
if any of the players gets his marker in three concesutoive positions either horizontally/vertically/diagonally, then he will win and game is over
otherwise the game will continue till the board gets filled completly
"""

#import IPython '''IPyhton module is not working in this machine though i have intalled it in command line using PIP Install'''
#from IPython import display
import random

#GAME_LIST = ['   ']*9


"""
To displays the list as board of Tick Tok Toe
"""
def display_board():
   #IPython.display.clear_output() '''If IPyhton module works, then output will be cleared out for each run.
   print(GAME_LIST[6] + ' | ' + GAME_LIST[7] + ' | ' + GAME_LIST[8] + '\n')
   print(GAME_LIST[3] + ' | ' + GAME_LIST[4] + ' | ' + GAME_LIST[5] + '\n')
   print(GAME_LIST[0] + ' | ' + GAME_LIST[1] + ' | ' + GAME_LIST[2] + '\n')


"""
To select the player and decides whicg player's turn first
"""
def game_player():
   if random.randint(1,2) == 1:
      return 'PLAYER1'
   else:
      return 'PLAYER2'

#PLAYER = game_player()


"""
To select the marker for the player1 & player2
"""
def player_marker():
   choice = input('choose your marker in [X,O] ').upper()
   if choice == 'X':
      return ('X','O')
   else:
      return ('O','X')

#PLAYER1_MARKER, PLAYER2_MARKER = player_marker()


"""
Checks for the space availability on the board and returns TRUE or FALSE boolean
"""
def board_space_full():
   if '   ' in GAME_LIST:
      return True
   else:
      return False

#BOARD_SPACE = board_space_full()


"""
This function Asks the user for the position untill a valid one is given
and decide the position and place the marker in that position.
"""
def player_position(marker, player):                                  #passing the respective player marker &  player as parameters here
   if BOARD_SPACE == False:
      print('Board is full')
      #break
   else:
      while True:                                            #we can use BOARD_SPACE variable also here like we used it for IF just above
         position = int(input('%s, Enter the  position to place the marker on the board b/w (0-8): ' %player))
         if GAME_LIST[position].isspace():
            GAME_LIST[position] = marker
            break
         #else:
          #  continue                                         #We dont need this else as the while loop will take care of the repitation loop.


"""
To decide the winner of the game based on 3 consecutive marks either vertically or horizontally  or diagonally
"""
def game_winner(marker):
   return ( (GAME_LIST[0] == GAME_LIST[1] == GAME_LIST[2] == marker) or #these 3 lines checks horizontally
            (GAME_LIST[3] == GAME_LIST[4] == GAME_LIST[5] == marker) or
            (GAME_LIST[6] == GAME_LIST[7] == GAME_LIST[8] == marker) or

            (GAME_LIST[0] == GAME_LIST[3] == GAME_LIST[6] == marker) or #these 3 lines checks vertically
            (GAME_LIST[1] == GAME_LIST[4] == GAME_LIST[7] == marker) or
            (GAME_LIST[2] == GAME_LIST[5] == GAME_LIST[8] == marker) or

            (GAME_LIST[0] == GAME_LIST[4] == GAME_LIST[8] == marker) or #these 2 lines checks diagonally
            (GAME_LIST[2] == GAME_LIST[4] == GAME_LIST[6] == marker) )


#WINNER = game_winner(marker) '''PLAYER1_MARKER or PLAYER2_MARKER'''


"""
GAME LOGIC PART AND FLOW of the Game step by step for both the players
We are keeping all the above defined functions in proper order as required for the game
and calling them with proper variables by passing as parameters to the functions.
"""
GAME_LIST = ['   ']*9
GAME_ON = True

PLAYER = game_player() #player gets player1 or player2

PLAYER1_MARKER, PLAYER2_MARKER = player_marker() #these 2 variables, will have 'X'/'O' as markers

'''
This while keeps going until any of th eplayer wins or till the board gets completly filled
'''
while GAME_ON:
   if PLAYER == 'PLAYER1':
      display_board()
      BOARD_SPACE = board_space_full()
      if BOARD_SPACE == False:
         GAME_ON = 'False'
         break
      player_position(PLAYER1_MARKER, PLAYER)
      WINNER = game_winner(PLAYER1_MARKER)
      if WINNER:
         print('Player-1 won')
         break
      PLAYER = 'PLAYER2'

   else:
      display_board()
      BOARD_SPACE = board_space_full()
      if BOARD_SPACE == False:
         GAME_ON = 'False'
         break
      player_position(PLAYER2_MARKER, PLAYER)
      WINNER = game_winner(PLAYER2_MARKER)
      if WINNER:
         print('Player-2 won')
         break
      PLAYER = 'PLAYER1'
