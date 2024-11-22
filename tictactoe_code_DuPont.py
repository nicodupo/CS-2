
import random
box = [ 
   [0,1,2],
   [3,4,5],
   [6,7,8] ]

def main():


   print(box[0][0])

   print("welcome")
   print_box(box)


player1 = input("Xs or Os? Type 'X' or 'O' ")

if player1 == 'X':
   player2 = 'O'                  #computer
else:
   player1 = '0' 
   player2 = 'X'

coins = ['Heads','Tails']

coin = random.choice(coins)

print(coin)
coin = random.randint(0,1)
if player1 == 0:
 
   player1 = "robot"
   player2 = "human"
else:
 
player1 = 'human'
player2 = 'robot'

turn = random.choice([True, False])
   count = 0

   while count <9:                           #player 1 is X

      if turn is True:
         print ("player1 turn")

         choice = input("enter 1-9")
         status = make_move(choice)
            if status == True:
               continue
            else: 
               turn = False
      else: 
         print("player2 turn")
         play_game("0")
         turn = True
      count +=1
def checkbox(player, choice):
   if player == "X":
      check_for = "O"
   if player == "O":
      check_for = "X"


   found = False
   if choice == 1 and player == "X":
      if box[0][0] == 'O':
         found = False

   return found
         
def print_box(box):

   for row in box:
      for col in row:
         print(col, end=" ")
      print("")


def make_move(choice):
   if box [0][0]=="0" and box[0][0]!='X' and box [0][0] =='X':
      found = checkbox('X')
      if found is True:
         print("illegal move")
         return "found"

   if box [0][1]=="1" and box [0][1]!='x' and box [0][1] =='x':
      checkbox('X')
   if box [0][2]=="2" and box [0][2]!='x' and box [0][2] == 'x':
      checkbox('x')
   if box [1][3]=="3" and box [1][3]!='x' and box [1][3] == 'x':
      checkbox('x')
   if box [1][4]=="4" and box [1][4]!='x'and box [1][4] == 'X':
      checkbox('x')
   if box [1][5]=="5" and box[1][5]!='X' and box [1][5] =='X':
      checkbox('X')
   if box [2][6]=="6" and box [2][6]!='x' and box [2][6] =='x':
      checkbox('X')
   if box [2][7]=="7" and box [2][7]!='x' and box [2][7] == 'x':
      checkbox('x')
   if box [2][8]=="8" and box [2][8]!='x' and box [2][8] == 'x':
      checkbox('x')
   if box [2][9]=="9" and box [2][9]!='x'and box [2][9] == 'x':
      checkbox('x')

#userchoice = random.randint(1,9)

#if userchoice ==1:
   #box[][]


def check_winner(XO):

   if box[0][0] == XO and box[0][1] == XO and box[0][2]:
      print(XO " is winner")
      print("game over")
   elif box[0][0] == XO and box[1][0] == XO and box[2][0]:
      print(XO "is winner")
      print("game over")
   elif box[0][2] == XO and box[1][2] == XO and box [2][2]:
      print(XO "is winner")
      print("game over")
   elif box[2][0] == XO and box[2][1] == XO and box [2][2]:
      print(XO "is winner")
      print ("game over")
   elif box[0][0] == XO and box [1][1] == XO and box [2][2]:
      print(XO "is winner")
      print ("game over")
   elif box[2][0] == XO and box [1][1] == XO and box [0][2]:
      print(XO "is winner")
      print ("game over")
   elif box[1][0] == XO and box [1][1] == XO and box [1][2]: 
      print (XO "is winner")
      print ("game over")
   elif box [0][1] == XO and box [1][1] == XO and box [2][1]:
      print (XO "winner")
      print ("game over")
  
main():