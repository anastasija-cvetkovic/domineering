from board import Board

def minimax_algorithm(board:Board,player_moves,depth,maximizer:str,alpha,beta):
    positive_infinity=float('inf')
    negative_infinity=float('-inf')
    best_move=[]
    if depth == 0 or len(player_moves) == 0:
        return[best_move,board.evaluate_moves(board.matrix,)]
    if maximizer == "X":
        # player X is taking turn
        max_eval = negative_infinity
        for node in player_moves:
            children = board.calculate_possible_moves(board.matrix,True)  
            board.make_move(node,board.matrix,False)
            evaluation = minimax_algorithm(board.matrix,board.rows,board.cols,children,depth-1,"X",alpha,beta)
            board.make_move(node,board.matrix,False,True)
            if(max_eval < evaluation[1]):
                max_eval = evaluation[1]
                best_move = node
            alpha = max(alpha, evaluation[1])
            if beta <= alpha:
                break
        return [best_move,max_eval]
    else:
        # player O is takin turn
        min_eval = positive_infinity
        for node in player_moves:
            children = board.calculate_possible_moves(board.matrix,False)
            board.make_move(node,board.matrix,True)
            evaluation = minimax_algorithm(board.matrix,board.rows,board.cols,children,depth-1,"O",alpha,beta)
            board.make_move(node,board.matrix,True,True)
            if(min_eval > evaluation[1]):
                min_eval = evaluation[1]
                best_move = node
            beta = min(beta,evaluation[1])
            if beta <= alpha:
                break
        return [best_move,min_eval]    