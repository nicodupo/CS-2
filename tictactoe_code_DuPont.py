'''
Name: Nico DuPont
date: 12/2/24
description: tic tac toe game
log: 1.0
bugs: none
features: coin toss for who goes first
'''
import random

def print_box(box):
   for row in range(0,3):           
      for col in range(0,3):
            print(box[row][col], end=" ")
      print()

def make_move(choice, current_player, box):
   if choice == '1' and box[0][0] not in ["X", "O"]:
         box[0][0] = current_player
   elif choice == '2' and box[0][1] not in ["X", "O"]:
         box [0][1] = current_player
   elif choice == '3' and box [0][2] not in ["X", "O"]:
         box [0][2] = current_player
   elif choice == '4' and box [1][0] not in ["X", "O"]:
         box [1][0] = current_player
   elif choice == '5' and box [1][1] not in ["X", "O"]:
         box [1][1] = current_player
   elif choice == '6' and box [1][2] not in ["X", "O"]:
         box [1][2] = current_player 
   elif choice == '7' and box [2][0] not in ["X", "O"]:
         box [2][0] = current_player
   elif choice == '8' and box [2][1] not in ["X", "O"]:
         box [2][1] = current_player
   elif choice == '9' and box [2][2] not in ["X", "O"]:
         box [2][2] = current_player 
   '''
description: lets the user make their move on the board
args: takes the box that the user wants to put his X or O in and checks if it is taken
return: nothing
   '''
def check_winner(box, XO):
   if box[0][0] == XO and box[0][1] == XO and box[0][2] == XO:
      print(XO, " is winner")
      print("game over")
   elif box[0][0] == XO and box[1][0] == XO and box[2][0] == XO:
      print(XO, "is winner")
      print ("game over")
   elif box[0][2] == XO and box[1][2] == XO and box [2][2] == XO:
      print(XO, "is winner")
      print("game over")
   elif box[2][0] == XO and box[2][1] == XO and box [2][2] == XO:
      print(XO, "is winner")
      print ("game over")
   elif box[0][0] == XO and box [1][1] == XO and box [2][2] == XO:
      print(XO, "is winner")
      print ("game over")
   elif box[2][0] == XO and box [1][1] == XO and box [0][2] == XO:
      print(XO, "is winner")
      print ("game over")
   elif box[0][2] == XO and box[1][1] == XO and box [2][0] == XO:
      print(XO, "is winner")
      print ("game over")
   elif box[0][1] == XO and box [1][1] == XO and box [2][1] == XO:
      print(XO, "is winner")
      print ("game over")
   elif box[1][0] == XO and box [1][1] == XO and box [1][2] == XO:
      print(XO, "is winner")
      print ("game over")
   return ""
def main():
   box = [ 
   [1,2,3], 
   [4,5,6],
   [7,8,9] ]
   '''
   description: prints the playing box
   args: takes all the different possible spaces
   returns: fully printed box
   '''

   player1 = input("enter first player name:")
   player2 = input("enter second player name:") 
   
   turn = random.choice([True, False])
   
   if turn is True:
      print(player1 +" goes first, player1 is X")
   else: 
      print(player2 + " goes first player2 is O") 
   
   count = 0
   print_box(box)
   

         
   if turn is True:
      while count < 9:
         status = check_winner(box, "O")                    #check if the player has won
         choice = input("enter 1-9, 'X':")                 #add code to be able to enter 1-9   
         
         count += 1
         make_move(choice, "X", box)                    #check if the move is valid
         status = check_winner(box, "X")                    #check if the player has won  
         print_box(box)
         status = check_winner(box, "O")                    #check if the player has won
         count += 1
         choice = input("enter 1-9, 'O':")                 #add code to be able to enter 1-9   
         make_move(choice, "O", box)                    #check if the move is valid
         status = check_winner(box, "O")                    #check if the player has won
         print_box(box)

         
   if turn is False:                                      #player 2 is O
      while count < 9:
         status = check_winner(box, "O")                    #check if the player has won
         choice = input("enter 1-9, 'O':")                  #add code to be able to enter 1-9

         count += 1
         make_move(choice, "O", box)                    #check if the move is valid
         status = check_winner(box, "O")                    #check if the player has won
         print_box(box)
         status = check_winner(box, "O")                    #check if the player has won
         count += 1
         choice = input("enter 1-9, 'X':")
         make_move(choice, "X", box)                    #check if the move is valid
         status = check_winner(box, "X")                    #check if the player has won  
         print_box(box)

if __name__ == "__main__":
   main()