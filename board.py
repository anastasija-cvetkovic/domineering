import string
from base_player import Player
from common import PLAYER_X,PLAYER_O

class Board:

  def __init__(self, rows,cols):
    self.rows = rows
    self.cols = cols
    self.matrix = [[" " for _ in range(cols)] for _ in range(rows)]

  def draw_board(self): 
    header = f"   {' '.join(string.ascii_uppercase[:self.cols])}" 
    equals_line = f"   {' '.join('=' * self.cols)}"  #= = =
    dash_line = f"   {' '.join('-' * self.cols)}"    #- - -
    print(header)
    print(equals_line)
    for row_num in range(self.rows, 0, -1): 
        matrix_row = self.rows - row_num  
        cells = [str(cell) for cell in self.matrix[matrix_row]] 
        print(f" {row_num}ǁ{'|'.join(cells)}ǁ{row_num}")
        if row_num > 1:
            print(dash_line)
    print(equals_line)
    print(header)   
  
  def valid_move(self, player_move, player: Player):
    row_position = player_move[0]
    column_position = player_move[1]

    if not (0 <= row_position < self.rows) or not (0 <= column_position < self.cols):
        print("Invalid move: Position is out of bounds.")
        return False

    if player.marker == "X":
        if row_position < 1:
            print("Invalid move: Cannot place vertical domino in the first row.")
            return False
        if self.matrix[row_position][column_position] != " " or self.matrix[row_position - 1][column_position] != " ":
            print("Invalid move: Cells are not empty.")
            return False
        return True

    elif player.marker == "O":
        if column_position >= self.cols - 1:
            print("Invalid move: Cannot place horizontal domino in the last column.")
            return False
        if self.matrix[row_position][column_position] != " " or self.matrix[row_position][column_position + 1] != " ":
            print("Invalid move: Cells are not empty.")
            return False
        return True

    return False  # Invalid player 
     
  def make_move(self, player_move, player, undo=False):
    move_row = player_move[0]
    move_column = player_move[1] 

    if undo:
        marker = " "
    else:
        marker = str(player.marker)

    if player.marker == "X":
        # For PLAYER_X (vertical placement)
        self.matrix[move_row][move_column] = marker
        self.matrix[move_row - 1][move_column] = marker
    elif player.marker == "O":
        # For PLAYER_O (horizontal placement)
        self.matrix[move_row][move_column] = marker
        self.matrix[move_row][move_column + 1] = marker

  def calculate_possible_moves(self,player):
    result=[]
    for i in range(self.rows):
        for j in range(self.cols):
            if((i > 0  if player.marker == "X" else j < self.cols - 1) and self.matrix[i][j] == " " and self.matrix[i if player.marker == "O" else i - 1][j if player.marker == "X" else j + 1] == " "):
                result.append([i,j])
    return result
  
  def evaluate_moves(self):
    evaluated = len(self.calculate_possible_moves(PLAYER_X)) - len(self.calculate_possible_moves(PLAYER_O))
    return evaluated

  def game_over(self, moves_left,player):
    if(not moves_left):
        print(f"{player.marker} player won!")
        return True
    return False