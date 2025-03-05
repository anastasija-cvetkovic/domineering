from minimax import *
from common import *

class Player:
  def __init__(self, marker):
    self.marker = marker # X or O
  # def take_move(self, board:Board) -> list[int,int]:
  #   pass # method to be implemented by subclasses

#isinstance(player,HumanPlayer)

class HumanPlayer(Player):
  from boardClass import Board

  def __init__(self,marker):
    super().__init__(self,marker) # super() <=> Player()

  def take_move(self,board:Board) -> list[int,int]:
    while True:
        try:
            move_row = int(input("Insert the row of your move:"))
            row_index = board.rows - move_row
            if not(0 <= row_index < board.rows):
                print(f"Inserted number needs to be less than {board.rows}.")
                continue
            break
        except ValueError:
            print("Must be a number!")
    while True:
      move_column = input("Insert the column of your move:").strip() # strip() for whitespace
      if len(move_column) != 1 or not move_column.isalpha():
        print("Please enter a single letter for the column.")
        continue
      column_index = ord(move_column.upper()) - ord('A')
      if not (0 <= column_index < board.cols):
        print(f"Must be one letter between A and {chr(ord('A') + board.cols - 1)}!")
        continue
      break 
    return [row_index,column_index]

  def play(self, board):
    player_move = self.take_move(board)
    valid = board.valid_move(player_move, self)
    while (not valid):
       player_move = self.take_move(board)
       valid = board.valid_move(player_move, self)
    board.make_move(player_move, self)

class ComputerPlayer(Player):
  def __init__(self, marker):
    super().__init__(self, marker)

  def play(self, board, alpha, beta, depth=4):
    if self.marker == "X":
      player_moves = board.calculate_possible_moves(self) 
      picked_move = minimax_algorithm(board, self,player_moves, depth, NEGATIVE_INFINITY, POSITIVE_INFINITY)
      print(picked_move)
      board.make_move(picked_move[0],self)

