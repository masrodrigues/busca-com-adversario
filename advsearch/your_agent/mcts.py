import random
import math
import time
from typing import Tuple

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    root_player = state.player
    legal_moves = list(state.legal_moves())
    if not legal_moves:
        return (-1, -1)

    for move in legal_moves:
        child_state = state.next_state(move)
        if child_state.is_terminal() and child_state.winner() == root_player:
            return move

    root = _Node(state)
    deadline = time.perf_counter() + 1.0
    min_iterations = 200
    iterations = 0

    while iterations < min_iterations or time.perf_counter() < deadline:
        node = _select(root)
        if not node.state.is_terminal():
            node = _expand(node)

        result = _simulate(node.state.copy(), root_player)
        _backpropagate(node, result)
        iterations += 1

    if not root.children:
        return random.choice(legal_moves)

    return max(root.children, key=lambda child: child.visits).move


class _Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.wins = 0.0
        self.visits = 0
        self.untried_moves = list(state.legal_moves())


def _select(node: _Node) -> _Node:
    while not node.state.is_terminal() and not node.untried_moves and node.children:
        node = max(node.children, key=_uct_score)
    return node


def _expand(node: _Node) -> _Node:
    move = node.untried_moves.pop()
    child = _Node(node.state.next_state(move), parent=node, move=move)
    node.children.append(child)
    return child


def _uct_score(node: _Node) -> float:
    if node.visits == 0:
        return float("inf")
    exploitation = node.wins / node.visits
    exploration = math.sqrt(math.log(node.parent.visits) / node.visits)
    return exploitation + math.sqrt(2) * exploration


def _simulate(state, root_player: str) -> float:
    while not state.is_terminal():
        legal_moves = list(state.legal_moves())
        if not legal_moves:
            break
        state = state.next_state(random.choice(legal_moves))

    winner = state.winner()
    if winner == root_player:
        return 1.0
    if winner is None:
        return 0.5
    return 0.0


def _backpropagate(node: _Node, result: float) -> None:
    while node is not None:
        node.visits += 1
        node.wins += result
        node = node.parent

