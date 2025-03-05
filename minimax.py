from board import *
from base_player import Player
from common import *

def minimax_algorithm(board:Board,current_player:Player,player_moves,depth,alpha,beta):
    
    if depth == 0 or board.game_over(player_moves,current_player):
        return [None,board.evaluate_moves()]

    best_move=[]
  
    opponent = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    if current_player == PLAYER_X:
        # maximizer(player X) is taking turn
        # opponent is player O
        max_eval = NEGATIVE_INFINITY
        for node in player_moves:
            children = board.calculate_possible_moves(opponent)  
            board.make_move(node, current_player)
            evaluation = minimax_algorithm(board, opponent, children, depth - 1, alpha, beta)
            board.make_move(node, current_player, True) # undo move
            if(max_eval < evaluation[1]):
                max_eval = evaluation[1]
                best_move = node
            alpha = max(alpha, evaluation[1])
            if beta <= alpha:
                break
        return [best_move,max_eval]
    else:
        # minimizer(player O) is taking turn
        # opponent is player X
        min_eval = POSITIVE_INFINITY
        for node in player_moves:
            children = board.calculate_possible_moves(opponent)
            board.make_move(node, current_player)
            evaluation = minimax_algorithm(board, opponent, children, depth - 1, alpha, beta)
            board.make_move(node, current_player, True) # undo move
            if(min_eval > evaluation[1]):
                min_eval = evaluation[1]
                best_move = node
            beta = min(beta,evaluation[1])
            if beta <= alpha:
                break
        return [best_move,min_eval]    