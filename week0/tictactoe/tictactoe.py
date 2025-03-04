"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
        count_X += row.count(X)
        count_O += row.count(O)

    if count_X > count_O:
        return O
    else:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_moves = set()

    for row_index, row in enumerate(board):
        for column_index, item in enumerate(row):
            if item == None:
                possible_moves.add((row_index, column_index))

    return possible_moves

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    player_move = player(board)

    new_board = deepcopy(board)
    i,j = action

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_move

    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for player in (X,O):
        for row in board:
            if row == [player]*3:
                return player

        for i in range(3):
            column = [board[x][i] for x in range(3)]
            if column == [player]*3:
                return player

        if [board[i][i] for i in range(0,3)] == [player]*3:
            return player
        elif [board[i][~i] for i in range(0,3)] == [player]*3:
            return player

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winning_player = winner(board)

    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -10
            for action in actions(board):
                minvalue = min_value(result(board, action))[0]
                if minvalue > v:
                    v = minvalue
                    optimal_move = action

            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = +10
            for action in actions(board):
                maxvalue = max_value(result(board, action))[0]
                if maxvalue < v:
                    v = maxvalue
                    optimal_move = action

            return v, optimal_move

    current_player = player(board)

    if terminal(board):
        return None

    if current_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]

    raise NotImplementedError
