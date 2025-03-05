from board import *
from players import *
from common import *

def game_on(current_player,opponent, board:Board, winner):

  while (not winner):
    possible_moves = board.calculate_possible_moves(current_player)
    winner =  board.game_over(possible_moves,opponent)
    if(winner):
      break
    print(f"{current_player.marker} player's turn:")

    current_player.play(board)
  
    current_player, opponent = opponent, current_player

