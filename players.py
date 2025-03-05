from minimax import *
from common import *
from base_player import *
from board import Board

class HumanPlayer(Player):

  def __init__(self,marker):
    super().__init__(marker) 

  def take_move(self, board: Board) -> list[int, int]:
      while True:
        try:
          move_row = int(input("Insert the row of your move: "))
          row_index = board.rows - move_row
          if not (0 <= row_index < board.rows):
            print(f"Row must be between 1 and {board.rows}.")
            continue  
        except ValueError:
          print("Invalid input. Enter a number for the row.")
          continue
        while True:
          move_column = input("Insert the column of your move: ").strip().upper()
          if len(move_column) != 1 or not move_column.isalpha():
            print("Please enter a single letter (A-Z).")
            continue
          column_index = ord(move_column) - ord('A')
          if not (0 <= column_index < board.cols):
            print(f"Column must be between A and {chr(ord('A') + board.cols - 1)}.")
            continue
          break 
        return [row_index, column_index]

  def play(self, board):
    while True:  
        player_move = self.take_move(board)
        valid = board.valid_move(player_move, self)
        if valid:
            board.make_move(player_move, self)
            board.draw_board()
            break
        else:
            print("Invalid move!")

class ComputerPlayer(Player):
  def __init__(self, marker):
    super().__init__(marker)

  def play(self, board, depth = 4):
    player_moves = board.calculate_possible_moves(self) 
    picked_move = minimax_algorithm(board, self, player_moves, depth, NEGATIVE_INFINITY, POSITIVE_INFINITY)
    board.make_move(picked_move[0], self)
    board.draw_board()