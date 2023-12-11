"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    c=0
    for i in board:
        for y in i:
            if y==X:
                c+=1
            if y==O:
                c-=1
    if c==0:
        return X
    else:
        return O


def actions(board):
    L=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                L.add((i,j))
    return L


def result(board, action):
    if action not in actions(board):
        raise Exception("not a valid action")
    i,j=action
    board2 = copy.deepcopy(board)
    board2[i][j]=player(board)
    return board2

def winner(board):
    for i in range(3):
            if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]!=EMPTY:
                return board[i][0]
            if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]!=EMPTY:
                return board[0][i]
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!=EMPTY:
                return board[0][0]
    if board[2][0]==board[1][1] and board[0][2]==board[1][1] and board[2][0]!=EMPTY:
                return board[2][0]

def terminal(board):
    if winner(board) in [X,O]:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                return False
    return True


def utility(board):
    if winner(board)==X:
         return 1
    if winner(board)==O:
         return -1
    return 0
    
def maxvalue(board):
    v=-math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
         v=max(v, minvalue(result(board, action)))
    return v
    



def minvalue(board):
    v=math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
         v=min(v, maxvalue(result(board, action)))
    return v
     

     
def minimax(board):
    L=[]
    if terminal(board):
        return None
    
    elif player(board)==X:
        for a in actions(board):
            L.append([minvalue(result(board,a)),a])
        return sorted(L, key=lambda x: x[0], reverse=True)[0][1]
    else:
        for a in actions(board):
            L.append([maxvalue(result(board,a)),a])
        return sorted(L, key=lambda x: x[0])[0][1]


    
    
    
