from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move
from .othello_minimax_mask import EVAL_TEMPLATE

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    return minimax_move(state, 3, evaluate_custom)


def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    opponent = Board.opponent(player)

    if state.is_terminal():
        winner = state.winner()
        if winner == player:
            return 100000
        if winner == opponent:
            return -100000
        return 0

    player_pieces = state.board.num_pieces(player)
    opponent_pieces = state.board.num_pieces(opponent)
    occupied = player_pieces + opponent_pieces

    positional_score = _positional_score(state, player, opponent)
    mobility_score = _mobility_score(state, player, opponent)
    corner_score = _corner_score(state, player, opponent)
    danger_score = _corner_danger_score(state, player, opponent)
    piece_score = player_pieces - opponent_pieces

    piece_weight = 2 if occupied >= 52 else 0.5
    return (
        3 * positional_score
        + 10 * mobility_score
        + 35 * corner_score
        + 15 * danger_score
        + piece_weight * piece_score
    )


def _positional_score(state: GameState, player: str, opponent: str) -> float:
    score = 0
    for row in range(8):
        for col in range(8):
            piece = state.board.tiles[row][col]
            if piece == player:
                score += EVAL_TEMPLATE[row][col]
            elif piece == opponent:
                score -= EVAL_TEMPLATE[row][col]
    return score


def _mobility_score(state: GameState, player: str, opponent: str) -> float:
    return len(state.board.legal_moves(player)) - len(state.board.legal_moves(opponent))


def _corner_score(state: GameState, player: str, opponent: str) -> float:
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    return _piece_diff_on_squares(state, player, opponent, corners)


def _corner_danger_score(state: GameState, player: str, opponent: str) -> float:
    danger_groups = {
        (0, 0): [(0, 1), (1, 0), (1, 1)],
        (0, 7): [(0, 6), (1, 6), (1, 7)],
        (7, 0): [(6, 0), (6, 1), (7, 1)],
        (7, 7): [(6, 6), (6, 7), (7, 6)],
    }

    score = 0
    for corner, adjacent_squares in danger_groups.items():
        corner_row, corner_col = corner
        if state.board.tiles[corner_row][corner_col] != Board.EMPTY:
            continue
        score -= _piece_diff_on_squares(state, player, opponent, adjacent_squares)
    return score


def _piece_diff_on_squares(state: GameState, player: str, opponent: str, squares: list) -> int:
    score = 0
    for row, col in squares:
        piece = state.board.tiles[row][col]
        if piece == player:
            score += 1
        elif piece == opponent:
            score -= 1
    return score
