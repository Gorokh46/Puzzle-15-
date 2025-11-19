from random import choice

# =============== ИГРОВАЯ ЛОГИКА ===============
def create_solved_board():
    return [[(i * 4 + j + 1) % 16 for j in range(4)] for i in range(4)]

def is_solved(board):
    """Проверяет, решена ли головоломка"""
    solved = create_solved_board()
    return board == solved

def get_empty_pos(board):
    """Возвращает (row, col) пустой клетки"""
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j
    return None

def can_move(board, tile_row, tile_col):
    """Проверяет, можно ли переместить плитку в пустую клетку"""
    empty_row, empty_col = get_empty_pos(board)
    # Плитка должна быть рядом по горизонтали или вертикали
    return (
        (abs(tile_row - empty_row) == 1 and tile_col == empty_col) or
        (abs(tile_col - empty_col) == 1 and tile_row == empty_row)
    )

def move_tile(board, tile_row, tile_col):
    """Меняет местами плитку и пустую клетку"""
    if can_move(board, tile_row, tile_col):
        empty_row, empty_col = get_empty_pos(board)
        board[empty_row][empty_col], board[tile_row][tile_col] = \
            board[tile_row][tile_col], board[empty_row][empty_col]
        return True
    return False

