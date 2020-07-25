import random

class cube(object):
  def __init__(self, x_dir, y_dir):
    self.x = x_dir
    self.y = y_dir

class snake(object):
  def __init__(self, head_x, head_y):
    self.head = cube(head_x, head_y)
    self.body = [self.head]

def move_snake(snake_obj):
  head_last_x = snake_obj.head.x
  head_last_y = snake_obj.head.y
  prev_last_x = snake_obj.body[-1].x
  prev_last_y = snake_obj.body[-1].y
  key_pressed = input()

  if key_pressed == 'w':
    snake_obj.head.y -= 1
    if len(snake_obj.body) > 1:
      switch_last(head_last_x, head_last_y, snake_obj)
  elif key_pressed == 's':
    snake_obj.head.y += 1
    if len(snake_obj.body) > 1:
      switch_last(head_last_x, head_last_y, snake_obj)
  elif key_pressed == 'a':
    snake_obj.head.x -= 1
    if len(snake_obj.body) > 1:
      switch_last(head_last_x, head_last_y, snake_obj)
  elif key_pressed == 'd':
    snake_obj.head.x += 1
    if len(snake_obj.body) > 1:
      switch_last(head_last_x, head_last_y, snake_obj)
  elif key_pressed == 'q':
    global is_running
    is_running = False
  return prev_last_x, prev_last_y

def switch_last(head_last_x, head_last_y, snake_obj):
  last = snake_obj.body[-1]
  last.x = head_last_x
  last.y = head_last_y

def erase_snake(snake_obj, board):
  for element in snake_obj.body:
    board[element.y][snake_obj.head.x] = 0

def draw_snake_on_board(board, snake_obj):
  for cube in snake_obj.body:
    board[cube.y][cube.x] = 1

def draw_apple_on_board(board):
  y = random.randint(0, len(board)-1)
  x = random.randint(0, len(board[0])-1)
  board[y][x] = 2
  return y, x

def print_board(board):
  for row in board:
    print(row)

def main(board):
  global is_running
  
  width = len(board[0])
  height = len(board)
  snake_obj = snake(width//2, height//2)
  draw_snake_on_board(board, snake_obj)
  y_apple, x_apple = draw_apple_on_board(board)
  print_board(board)
  
  while is_running:
    erase_snake(snake_obj, board)
    prev_last_x, prev_last_y = move_snake(snake_obj)
    if snake_obj.head.x == x_apple and snake_obj.head.y == y_apple:
      snake_obj.body.append(cube(prev_last_x, prev_last_y))
      y_apple, x_apple = draw_apple_on_board(board)
    draw_snake_on_board(board, snake_obj)
    print_board(board)
  
  return 'Game over'


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

is_running = True
print(main(board))