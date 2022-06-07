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
    """
    Returns player who has the next turn on a board.
    """
    x_counter, o_counter = 0, 0
    for row in board:
        for element in row:
            if element == X:
                x_counter += 1
            if element == O:
                o_counter += 1
    if x_counter == o_counter:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    if board_copy[action[0]][action[1]] != EMPTY:
        raise Exception("This action is invalid!")
    board_copy[action[0]][action[1]] = player(board_copy)
    return board_copy


def winner(board):  
    """
    Returns the winner of the game, if there is one.
    """
    # win condition 1: horizontally
    for row in board:
        if row[0] == X and row[1] == X and row[2] == X:
            return X
        elif row[0] == O and row[1] == O and row[2] == O:
            return O

    # win condition 2: vertically
    if (board[0][0] == X and board[1][0] == X and board[2][0] == X) or (board[0][1] == X and board[1][1] == X and board[2][1] == X) or (board[0][2] == X and board[1][2] == X and board[2][2] == X):
        return X
    elif (board[0][0] == O and board[1][0] == O and board[2][0] == O) or (board[0][1] == O and board[1][1] == O and board[2][1] == O) or (board[0][2] == O and board[1][2] == O and board[2][2] == O):
        return O

    # win condition 3: diagonally
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    # if there is still a blank space
    for row in board:
        for element in row:
            if element == EMPTY:
                return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player_winner = winner(board)

    if player_winner == X:
        return 1
    elif player_winner == O:
        return -1
    else:
        return 0

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    opt_move = (None, None)
    if player(board) == X:
        best_value = -math.inf

        for action in actions(board):

            board[action[0]][action[1]] = X
            v_val = min_value(board)
            board[action[0]][action[1]] = EMPTY

            if best_value < v_val:
                best_value = v_val
                opt_move = action

        return opt_move

    elif player(board) == O:
        best_value = math.inf

        for action in actions(board):

            board[action[0]][action[1]] = O
            v_val = max_value(board)
            board[action[0]][action[1]] = EMPTY

            if best_value > v_val:
                best_value = v_val
                opt_move = action

        return opt_move




