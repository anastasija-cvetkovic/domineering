import string

def draw_table(m,n,matrix): 
    header = f"   {' '.join(string.ascii_uppercase[:n])}" 
    equals_line = f"   {' '.join('=' * n)}"  #= = =
    dash_line = f"   {' '.join('-' * n)}"    #- - -
    print(header)
    print(equals_line)
    for row_num in range(m, 0, -1): 
        matrix_row = m - row_num  
        cells = [str(cell) for cell in matrix[matrix_row]] 
        print(f" {row_num}ǁ{'|'.join(cells)}ǁ{row_num}")
        if row_num > 1:
            print(dash_line)
    print(equals_line)
    print(header)

def valid_move(player_move,column,player,matrix):
    column_position =  player_move[1]
    if(player == False):
        row_position = player_move[0] 
        if(row_position<1 or matrix[row_position][column_position] != " "):
            print("Invalid move")
            return False
        if(matrix[row_position-1][column_position] != " "):
            print("Invalid move")
            return False
        else:
            print("Valid move")
            return True
    elif(player==True):
        row_position = player_move[0]
        if(column_position+1 > column-1 or matrix[row_position][column_position] != " " ):
            print("Invalid move")
            return False
        if(matrix[row_position][column_position+1] != " "):
            print("Invalid move")
            return False
        else:
            print("Valid move")
            return True
        
def make_move(player_move,matrix,player,undo=False):
    move_column = player_move[1] 
    move_row = player_move[0]
    if(player == False):
        current_player = "X" if undo == False else " "
        matrix[move_row][move_column] = current_player
        matrix[move_row-1][move_column] = current_player
    elif(player == True):
        current_player = "O" if undo == False else " "
        matrix[move_row][move_column] = current_player
        matrix[move_row][move_column+1] = current_player

def take_move(row,column) -> list[int,int]:
    while(True):
        try:
            move_row = int(input("Insert the row of your move:"))
            real_row = row - move_row
            if real_row >= row or real_row < 0:
                print("Inserted number needs to be less than "+ str(row) + ".")
                continue
        except ValueError:
            print("Must be a number!")
            continue
        while(True):
            move_column = str(input("Insert the column of your move:"))
            column_position = ord(move_column) - 65
            if(column_position > 31 and column_position < 58): 
                column_position = column_position - 32
            if(column_position < 0 or column_position > 32 or len(move_column) > 1 or column_position > column):
                print("Must be one letter between A and " + string.ascii_uppercase[column - 1] + "!")
                continue
            else:
                break
        return [real_row,column_position]

def calculate_possible_moves(matrix,player,row,column):
    result=[]
    for i in range(row):
        for j in range(column):
            if(((i > 0  if player == False else j < column - 1)) and matrix[i][j] == " " and matrix[i if player == True else i - 1][j if player == False else j + 1] == " "):
                result.append([i,j])
    return result

def game_over(moves_left,player):
    if(not moves_left):
        if player:
            print("Player O won!")
            return True
        else:
            print("Player X won!")
            return True
    return False

def evaluate_moves(matrix,row,column):
    evaluated = len(calculate_possible_moves(matrix,False,row,column)) - len(calculate_possible_moves(matrix,True,row,column))
    return evaluated

def minimax_algorithm(matrix,row,column,player_moves,depth,maximizer,alpha,beta):
    positive_infinity=float('inf')
    negative_infinity=float('-inf')
    best_move=[]
    if depth == 0 or len(player_moves) == 0:
        return[best_move,evaluate_moves(matrix,row,column)]
    if maximizer:
        # player X is taking turn
        max_eval = negative_infinity
        for node in player_moves:
            children = calculate_possible_moves(matrix,True,row,column)  
            make_move(node,matrix,False)
            evaluation = minimax_algorithm(matrix,row,column,children,depth-1,False,alpha,beta)
            make_move(node,matrix,False,True)
            if(max_eval < evaluation[1]):
                max_eval = evaluation[1]
                best_move = node
            alpha = max(alpha, evaluation[1])
            if beta <= alpha:
                break
        return [best_move,max_eval]
    else:
        min_eval = positive_infinity
        for node in player_moves:
            children = calculate_possible_moves(matrix,False,row,column)
            make_move(node,matrix,True)
            evaluation = minimax_algorithm(matrix,row,column,children,depth-1,True,alpha,beta)
            make_move(node,matrix,True,True)
            if(min_eval > evaluation[1]):
                min_eval = evaluation[1]
                best_move = node
            beta = min(beta,evaluation[1])
            if beta <= alpha:
                break
        return [best_move,min_eval]      

def human_vs_computer(mode_computer,matrix,row,column,player):
    positive_infinity=float('inf')
    negative_infinity=float('-inf')
    if not mode_computer:
        # if computer is player X
        if player:
            player = human_move(row,column,player,matrix)
        else:
            player_moves = calculate_possible_moves(matrix,player,row,column)
            picked_move = minimax_algorithm(matrix,row,column,player_moves,4,True,negative_infinity,positive_infinity);
            print(picked_move)
            make_move(picked_move[0],matrix,player)
            player = not player
        draw_table(row,column,matrix)
    else:
        #ako je racunar igrac O
        if player:
            player_moves=calculate_possible_moves(matrix,player,row,column)
            picked_move=minimax_algorithm(matrix,row,column,player_moves,4,False,negative_infinity,positive_infinity);
            print(picked_move)
            make_move(picked_move[0],matrix,player)
            player = not player
        else:
            player = human_move(row,column,player,matrix)
        draw_table(row,column,matrix)
    return player      
    
def play(mode,mode_computer,player,matrix,row,column,winner):
    while(not winner): 
        possible_moves = calculate_possible_moves(matrix,player,row,column)
        if player:
            if(possible_moves):
                print("O player's turn:")
        else:
            if(possible_moves):
                print("X player's turn:") 
        winner =  game_over(possible_moves,not player) 
        if(winner):
            break
        else:
            if mode=="H":
                # human vs human
                player = human_move(row,column,player,matrix)
                draw_table(row,column,matrix)
            elif mode=="C":
                if mode_computer == "C":
                    #human vs computer, computer is player X
                    player = human_vs_computer(False,matrix,row,column,player)
                elif mode_computer == "H":
                    #human vs computer, computer is player O
                    player = human_vs_computer(True,matrix,row,column,player)

def human_move(row,column,player,matrix):
    player_move = take_move(row,column)
    valid = valid_move(player_move,column,player,matrix)
    while(not valid):
        player_move = take_move(row,column)
        valid = valid_move(player_move,column,player,matrix)
    make_move(player_move,matrix,player)
    player = not player
    return player          
     
def main():
    row = int(input("Number of rows:")) 
    column = int(input("Number of columns:"))
    matrix=[[" " for i in range(row)]for j in range(column)]
    draw_table(row,column,matrix)
    player = False # X plays first
    winner = False
    mode=input("Who are you playing against? C - Computer, H - Human ")
    if mode=="C":
        mode_computer = input("Who plays first: C - Computer, H - Human ")
        if mode_computer=="C":
            print("Computer is player X.")
        elif mode_computer=="H":
            print("Human is player X.")  
    elif mode=="H":
        mode_computer=None
        print("First player is X, second player is O.")

    play(mode,mode_computer,player,matrix,row,column,winner)
  
main()


