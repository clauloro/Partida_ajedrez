board = [
['♜',	'♞',	'♝',	'♛',	'♚',	'♝',	'♞',	'♜'],
['♟',	'♟',	'♟',	'♟',	'♟',	'♟',	'♟',	'♟'],
[' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
[' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
[' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
[' ',	' ',	' ',	' ',	' ',	' ',	' ',	' '],
['♙',	'♙',	'♙',	'♙',	'♙',	'♙',	'♙',	'♙'],
['♖',	'♘',	'♗',	'♕',	'♔',	'♗',	'♘',	'♖'],
]#utilizo el tablero con figuras

def ilustracion_board (board):
    for t in board:
        print(t)

if __name__ == '__main__':
    ilustracion_board(board)
