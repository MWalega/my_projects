from dataclasses import dataclass
import random
from copy import deepcopy
import time
import readchar

# BOARD

# - list of lists with integers
# - 0: empty field
# - 1: shape
# - 2: border of board
# - 5 upper rows serve as place to input shape
# - game over if board contains 1 on row <= 5

board = [
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,0,0,0,0,0,0,0,0,2,2],
         [2,2,2,2,2,2,2,2,2,2,2,2],
         [2,2,2,2,2,2,2,2,2,2,2,2],
         ]

# SHAPES

# - size of list of list with shape is always 5x5
# - 0: empty field, 1: shape
# - allshapes are stored on list called 'shapes'
# - every shape is a list containing list of lists containing integers. Every
#   list of lists depict unique rotation of certain shape
# - list contain every possible shape's rotation
# - when rotating shape change rotation in order of list positions
# - when last rotation changes -> jump to the start of the list and shape is
#   in start rotation 

S = [
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,1,1,0],
      [0,1,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,1,0],
      [0,0,0,1,0],
      [0,0,0,0,0]]
     ]

Z = [
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,0,0],
      [0,0,1,1,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,1,1,0,0],
      [0,1,0,0,0],
      [0,0,0,0,0]]
     ]
 
I = [
     [[0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [1,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]
     ]
 
O = [
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,0,0],
      [0,1,1,0,0],
      [0,0,0,0,0]]
     ]
     
J = [
     [[0,0,0,0,0],
      [0,1,0,0,0],
      [0,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,1,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,0,0,1,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,1,1,0,0],
      [0,0,0,0,0]]
     ]
 
L = [
     [[0,0,0,0,0],
      [0,0,0,1,0],
      [0,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,1,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,1,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,1,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]
     ]
 
T = [
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,1,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,1,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]
     ]

shapes = [S, Z, I, O, J, L, T]

# CLASSES

@dataclass
class pos:
  row: int
  col: int

@dataclass
class LiveShape:
  shape_ind: int # in range(len(shapes))
  shape_rot: int # in range(len(shapes[shape_ind]))
  current_pos: pos

# FUNCTIONS

def pick_new_random_shape() -> LiveShape:
  shape_ind = random.randint(0, len(shapes) - 1)
  starting_pos = pos(0, 3) 
  ls = LiveShape(shape_ind, 0, starting_pos)
  return ls

def print_board(board, ls: LiveShape):
  board_to_print = deepcopy(board)
  
  # adding current shape to board_to_print
  for srow in range(5):
    for scol in range(5):
      if shapes[ls.shape_ind][ls.shape_rot][srow][scol] == 1:
        assert(board_to_print[ls.current_pos.row + srow][ls.current_pos.col + scol] == 0)
        # - current_pos is the position of shapes[shape_ind][current_rot][0][0] on board 
        #   (ie upper left corner)
        # - current_pos+delta is the position of shapes[shape_ind][current_rot][delta.row][delta.col]
        #   on board (ie upper left corner)
        board_to_print[ls.current_pos.row + srow][ls.current_pos.col + scol] = 1

  # printing board_to_print
  for row_ind in range(len(board_to_print)):
    print('\n')
    for c in board_to_print[row_ind]:
      if c == 0:
        print(' . ', end = '')
      if c == 1:
        print(' # ', end = '')
      if c == 2:
        if row_ind < len(board_to_print) - 2:
          print(' | ', end = '')
        else:
          print(' _ ', end = '') 

def move_shape(ls: LiveShape, move) -> LiveShape:
  new_ls = deepcopy(ls)
  delta_pos = {
   's' : pos(1, 0), 
   'a' : pos(0, -1),
   'd' : pos(0, 1),
   '' : pos(0, 0),
  }

  if move == 'w':
    rotate_shape(new_ls)
  else:
    change_pos(new_ls, delta_pos[move])

  return new_ls

def rotate_shape(ls: LiveShape) -> LiveShape:
  
  ls.shape_rot = (ls.shape_rot + 1) % len(shapes[ls.shape_ind])

def change_pos(ls: LiveShape, delta: pos):
  ls.current_pos.row += delta.row
  ls.current_pos.col += delta.col

def collision(ls: LiveShape, board) -> bool:
  for srow in range(5):
    for scol in range(5):
      if (
          shapes[ls.shape_ind][ls.shape_rot][srow][scol] == 1 and 
          (board[ls.current_pos.row + srow][ls.current_pos.col + scol] == 1 or
          board[ls.current_pos.row + srow][ls.current_pos.col + scol] == 2)
          ):
        return True
  return False

def add_shape_to_board(ls: LiveShape, board):
  for srow in range(5):
    for scol in range(5):
      if shapes[ls.shape_ind][ls.shape_rot][srow][scol] == 1:
        board[ls.current_pos.row + srow][ls.current_pos.col + scol] = 1

def remove_full_rows(board):
  len_row_no_border = len(board[0][2:-2])
  
  for row in range(5, len(board[:-2])):
    count = 0
    for col in range(2, len(board[row][:-2])):
      if board[row][col] == 1:
        count += 1
    if count == len_row_no_border:
      remove_row_and_adapt_board(board, row)

def remove_row_and_adapt_board(board, row: int):
  # cleaning full row
  for col in range(2, len(board[0][:-2])):
    board[row][col] = 0

  # pulling down all 1's above empty row by 1
  for srow in range(row, 4, -1):
    for scol in range(2, len(board[0][:-2])):
      if board[srow][scol] == 1:
        board[srow][scol] = 0
        board[srow+1][scol] = 1

def game_not_over(board) -> bool:
  for row in range(5):
    for col in range(len(board[row])):
      if board[row][col] == 1:
        return False
  return True

def input_move() -> str:
  # w - rotate
  # a - left
  # d - right
  move = readchar.readchar()
  while move not in ['w','a','d']:
    return ''
  return move

def try_moves(ls: LiveShape, board) -> LiveShape:
  start = time.time()
  while (time.time() - start) < 0.5:
    move = input_move()
    new_ls = move_shape(ls, move)
    if not collision(new_ls, board):
      ls = new_ls
    print_board(board, ls)
  return ls

def tetris(board, shapes):
  ls = pick_new_random_shape()

  while game_not_over(board):
    print_board(board, ls)
    ls = try_moves(ls, board)
    new_ls = move_shape(ls, 's')
    if not collision(new_ls, board):
      ls = new_ls
    else:
      add_shape_to_board(ls, board)
      remove_full_rows(board)
      ls = pick_new_random_shape()
  return 'Game over'

tetris(board, shapes)