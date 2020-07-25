import readchar

def input_move() -> str:
  # w - rotate
  # a - left
  # d - right
  move = readchar.readchar()
  while move not in ['w','a','d']:
    move = readchar.readchar()
  return move

move = input_move()
print(move)
print(type(move))