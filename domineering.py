from board import *
from players import *
from common import *
from game import *       
     
def main():

  row = int(input("Number of rows:")) 
  column = int(input("Number of columns:"))

  board = Board(row,column)
  board.draw_board()

  while True:
    try:
      mode = input("Who are you playing against? C - Computer, H - Human ").upper()
      if mode not in ('C', 'H'):
        raise ValueError("Invalid mode choice!")
      
      if mode == "C":
        first_player = input("Who plays first: C - Computer, H - Human ").upper()
        if first_player not in ('C', 'H'):
          raise ValueError("Invalid choice for first player!")
        
        if first_player == "C":
          player1 = ComputerPlayer("X")
          player2 = HumanPlayer("O")
          print("Computer is player X.")
        else:
          player1 = HumanPlayer("X")
          player2 = ComputerPlayer("O")
          print("Human is player X.")

      else:
        player1=HumanPlayer("X")
        player2=HumanPlayer("O")
        print("First player is X, second player is O.")

      break
    except ValueError as e:
      print(e)
      print("Please insert correct values!")

  winner = False
  game_on(player1,player2,board,winner)
      
main()
    




