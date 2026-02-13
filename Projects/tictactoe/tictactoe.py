"""
Tic Tac Toe Player
"""

import math
import copy

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

    count_X = 0
    count_O = 0

    for row in board:
        for pos in row:
            if (pos == X):
                count_X = count_X + 1
            elif (pos == O):
                count_O = count_O + 1

    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)

    current_player = player(board)

    i, j = action

    if i < 0 or i > 2 or j < 0 or j > 2 or board[i][j] is not None:
        raise Exception("Invalid Action")

    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != EMPTY:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    board_check = winner(board)
    if board_check is not None:
        return True

    for row in board:
        for cell in row:
            if cell == None:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    current_player = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board)

        v = -math.inf
        for action in actions(board):
            score = min_value(result(board, action))
            if score > v:
                v = score

        return v

    def min_value(board):
        if terminal(board):
            return utility(board)

        v = math.inf
        for action in actions(board):
            score = max_value(result(board, action))
            if score < v:
                v = score

        return v

    if current_player == X:
        best_score = -math.inf
        best_move = None

        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_move = action

        return best_move

    else:
        best_score = math.inf
        best_move = None

        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_move = action

        return best_move
