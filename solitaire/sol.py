class SolitaireMancala:

  def __init__(self):
    self.board = [0]

  def __str__(self):
    return '[' + ', '.join([str(elem) for elem in self.board[::-1]]) + ']'

  def set_board(self, configuration):
    self.board = configuration[:]

  def get_num_seeds(self, house_num):
    return self.board[house_num]

  def is_legal_move(self, house_num):
    if house_num == 0: return False
    return house_num == self.board[house_num]

  def apply_move(self, house_num):
    if not self.is_legal_move(house_num): return
    self.board[house_num] = 0
    for house in range(house_num-1, -1, -1):
      self.board[house] += 1

  def choose_move(self):
    for house in range(1, len(self.board)):
      if self.is_legal_move(house): return house
    return 0

  def is_game_won(self):
    return all([elem == 0 for elem in self.board[1:] ])

  def plan_moves(self):
    config = self.board[:]
    move_list = []

    while True:
      move = self.choose_move()
      if move == 0: break
      move_list.append(move)
      self.apply_move(move)

    self.set_board(config)
    return move_list



# if __name__ == '__main__':
#   import test
#   test.run_test(SolitaireMancala)