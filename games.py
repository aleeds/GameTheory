import itertools

class Game(object):
  # num_moves is how many moves each player has, as a list of numbers
  def __init__(self,util_f,num_moves):
      self.num_moves = num_moves
      self.utilities_function = util_f
  def GetUtility(self,i,actions):
      return self.utilities_function(i,actions)


def UtilFunc(player,matrix,actions):
    matrix = matrix[player]
    for i in actions:
        matrix = matrix[i]
    return matrix

def BuildMatrixGame(num_moves,matrix):
    f = lambda i, actions: UtilFunc(i,matrix,actions)
    return Game(f, num_moves)

# I believe that this works. Further testing is a good idea though.
def ExpectedUtility(game, strategy_profiles,i):
    num_players = len(strategy_profiles)
    selector = [[i for i in range(len(strategy_profiles[q]))] for q in range(num_players)]
    options = list(itertools.product(*selector))
    util = 0
    for event in options:
        prob = 1
        for i in range(num_players):
            prob_t = strategy_profiles[i][event[i]]
            prob *= prob_t
        util_action = game.GetUtility(i,event)
        util += prob * util_action
    return util

# The input to this is a game, the matrix of strategy_profiles with the
# row for i with all 0s. i is the player who is best responding
def BestResponse(game,strategy_profiles,i):
    move = 0
    score = -100000000000
    for m in range(len(strategy_profiles[i])):
        cp = strategy_profiles.copy()
        cp[i][m] = 1
        util = ExpectedUtility(game,cp,i)
        if util > score:
            score = util
            move = m
        # This is here cause of silly python things, need to fix.
        cp[i][m] = 0
    return (move,score)
