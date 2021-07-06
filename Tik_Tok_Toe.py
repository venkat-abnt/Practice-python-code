"""
This Explains Tik Tok Toe game
"""
import IPython.display
import random

#GAME_LIST = ['   ']*9


#To displays the list as board
def display_board():
   IPython.display.clear_output()
   print(GAME_LIST[6] + ' | ' + GAME_LIST[7] + ' | ' + GAME_LIST[8] + '\n')
   print(GAME_LIST[3] + ' | ' + GAME_LIST[4] + ' | ' + GAME_LIST[5] + '\n')
   print(GAME_LIST[0] + ' | ' + GAME_LIST[1] + ' | ' + GAME_LIST[2] + '\n')

#To select the player
def game_player():
   if random.randint(1,2) == 1:
      return 'PLAYER1'
   else:
      return 'PLAYER2'

#PLAYER = game_player()

#To select the marker
def player_marker():
   choice = input('choose your marker in [X,O] ').upper()
   if choice == 'X':
      return ('X','O')
   else:
      return ('O','X')

#PLAYER1_MARKER, PLAYER2_MARKER = player_marker()


#Checks for the space availability on the board and returns TRUE or FALSE boolean
def board_space_full():
   if '   ' in GAME_LIST:
      return True
   else:
      return False

#BOARD_SPACE = board_space_full()


#DECIDE THE POSITION AND PLACE THE MARKER
def player_position(marker):                                  #passing the respective player marker here
   if BOARD_SPACE == False:
      print('Board is full')
      #break
   else:
      while True:                                            #we can use BOARD_SPACE variable also here like we used it for IF just above
         position = int(input('Enter the  position to place the marker on the board b/w (0-8): '))
         if GAME_LIST[position].is_space():
            GAME_LIST[position] = marker
            break
         else:
            continue                                         #i dont think we need this else as the while loop will take care of the repitation loop. Any how just tet this


#To decide the winner of the game
def game_winner():
   pass



"""
GAME LOGIC PART AND FLOW
"""

GAME_LIST = ['   ']*9
GAME_ON = True

PLAYER = game_player() #player gets player1 or player2

PLAYER1_MARKER, PLAYER2_MARKER = player_marker() #these 2 will have 'X'/'O' as markers

while GAME_ON:
   if PLAYER == 'PLAYER1':
      display_board()
      BOARD_SPACE = board_space_full()
      player_position(PLAYER1_MARKER)
      PLAYER = 'PLAYER2'

   else:
      isplay_board()
      BOARD_SPACE = board_space_full()
      player_position(PLAYER1_MARKER)
      PLAYER = 'PLAYER1'











