from typing import Tuple, Callable



def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    root_player = state.player
    legal_moves = _ordered_moves(state)

    if not legal_moves:
        return (-1, -1)

    best_move = legal_moves[0]
    best_value = float("-inf")
    alpha = float("-inf")
    beta = float("inf")

    next_depth = _next_depth(max_depth)
    for move in legal_moves:
        value = _alphabeta(
            state.next_state(move),
            next_depth,
            alpha,
            beta,
            root_player,
            eval_func,
        )

        if value > best_value:
            best_value = value
            best_move = move

        alpha = max(alpha, best_value)

    return best_move


def _alphabeta(state, depth:int, alpha:float, beta:float, root_player:str, eval_func:Callable) -> float:
    if state.is_terminal() or depth == 0:
        return eval_func(state, root_player)

    legal_moves = _ordered_moves(state)
    if not legal_moves:
        return eval_func(state, root_player)

    next_depth = _next_depth(depth)

    if state.player == root_player:
        value = float("-inf")
        for move in legal_moves:
            value = max(
                value,
                _alphabeta(
                    state.next_state(move),
                    next_depth,
                    alpha,
                    beta,
                    root_player,
                    eval_func,
                ),
            )
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    value = float("inf")
    for move in legal_moves:
        value = min(
            value,
            _alphabeta(
                state.next_state(move),
                next_depth,
                alpha,
                beta,
                root_player,
                eval_func,
            ),
        )
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value


def _next_depth(depth:int) -> int:
    return depth if depth < 0 else depth - 1


def _ordered_moves(state) -> list:
    return sorted(state.legal_moves())
