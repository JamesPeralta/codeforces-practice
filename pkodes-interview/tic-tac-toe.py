"""
Prompt: 
Unique Tic-Tac-Toe Finishes

We're working with a standard 3x3 Tic-Tac-Toe board.
- Two players: X goes first, then players alternate turns.
- A game ends immediately when:
   - One player wins (3 in a row), or
   - The board is full (draw)

We want to count how many different ways a game can finish.
- A "way" is defined as a sequence of moves, not just a final board.
"""

"""
Interview checklist:
- Clarify: sequence of moves (this code) vs distinct final boards (different count).
- State: board only; turn = X iff #X == #O (so state is hashable).
- Terminal: win *or* full — stop immediately (no moves after a win).
- Lines: all 8 winning lines; check both players for is_terminal.
"""
LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6),             # diags
)

def is_win(board: tuple[int, ...], mark: int) -> bool:
    return any(board[i] == board[j] == board[k] == mark for i, j, k in LINES)

def is_terminal(board: tuple[int, ...]) -> bool:
    if is_win(board, 1) or is_win(board, 2):
        return True
    return 0 not in board  # full

def ways_to_finish(board: tuple[int, ...], cache: dict[tuple[int, ...], int]) -> int:
    if board in cache:
        return cache[board]
    if is_terminal(board):
        cache[board] = 1
        return 1
    n_x = sum(1 for c in board if c == 1)
    n_o = sum(1 for c in board if c == 2)
    turn = 1 if n_x == n_o else 2  # X goes first
    total = 0
    for i in range(9):
        if board[i] != 0:
            continue
        new = list(board)
        new[i] = turn
        total += ways_to_finish(tuple(new), cache)
    cache[board] = total
    return total

def count_unique_finishes() -> int:
    return ways_to_finish((0,) * 9, {})

if __name__ == "__main__":
    print(count_unique_finishes())
