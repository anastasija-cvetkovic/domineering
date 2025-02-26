import string
from player import Player,HumanPlayer,ComputerPlayer 
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
  
  def valid_move(self,player_move,player:Player):
    column_position =  player_move[1]
    if(player.marker == "X"):
        row_position = player_move[0] 
        if(row_position < 1 or self.matrix[row_position][column_position] != " "):
            print("Invalid move")
            return False
        if(self.matrix[row_position - 1][column_position] != " "):
            print("Invalid move")
            return False
        else:
            print("Valid move")
            return True
    elif(player.marker == "O"):
        row_position = player_move[0]
        if(column_position + 1 > self.cols - 1 or self.matrix[row_position][column_position] != " " ):
            print("Invalid move")
            return False
        if(self.matrix[row_position][column_position + 1] != " "):
            print("Invalid move")
            return False
        else:
            print("Valid move")
            return True
     
  def make_move(self,player_move,player,undo=False):
    move_row = player_move[0]
    move_column = player_move[1] 
    if(player.marker == "X"):
        current_player = "X" if undo == False else " "
        self.matrix[move_row][move_column] = current_player
        self.matrix[move_row - 1][move_column] = current_player
    elif(player.marker == "O"):
        current_player = "O" if undo == False else " "
        self.matrix[move_row][move_column] = current_player
        self.matrix[move_row][move_column + 1] = current_player

  def calculate_possible_moves(self,player):
    result=[]
    for i in range(self.rows):
        for j in range(self.cols):
            if((i > 0  if player.marker == "X" else j < self.cols - 1) and self.matrix[i][j] == " " and self.matrix[i if player.marker == "O" else i - 1][j if player.marker == "X" else j + 1] == " "):
                result.append([i,j])
    return result
  
  def evaluate_moves(self,player):
    evaluated = len(self.calculate_possible_moves(self.matrix,player)) - len(self.calculate_possible_moves(self.matrix,player))
    return evaluated


  def game_over(moves_left,player):
    if(not moves_left):
        if player:
            print("Player O won!")
            return True
        else:
            print("Player X won!")
            return True
    return False