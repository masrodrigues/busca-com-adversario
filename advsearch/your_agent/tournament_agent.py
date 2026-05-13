from typing import Tuple
from ..othello.gamestate import GameState
from .minimax import minimax_move
from .othello_minimax_custom import evaluate_custom

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    Consider that this will be called in the Othello tournament situation,
    so you should call the best implementation you got.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    if state.game_name == 'Othello':
        return minimax_move(state, 3, evaluate_custom)

    return (-1, -1)

