import itertools

class Game(object):
  def __init__(self,utils):
      self.utilities = utils
  def GetPlayerI(self,i):
      return self.utilities[i]

# I believe that this works. Further testing is a good idea though.
def ExpectedUtility(game, strategy_profiles,i):
    num_players = len(strategy_profiles)
    selector = [[i for i in range(len(strategy_profiles[q]))] for q in range(num_players)]
    options = list(itertools.product(*selector))
    util = 0
    utils_i = game.GetPlayerI(i)
    print(utils_i)
    for event in options:
        prob = 1
        for i in range(num_players):
            prob_t = strategy_profiles[i][event[i]]
            prob *= prob_t
        print(prob)
        bottom = utils_i
        for i in event:
            bottom = bottom[i]
        print(bottom)
        util += prob * bottom
    return util

# The input to this is a game, the matrix of strategy_profiles with the
# row for i with all 0s. i is the player who is best responsing.
def BestResponse(game,strategy_profiles,i):
    move = 0
    score = -100000000000
    for m in range(len(strategy_profiles[i])):
        cp = strategy_profiles.copy()
        cp[i][m] = 1
        print(cp)
        util = ExpectedUtility(game,cp,i)
        if util > score:
            score = util
            move = m
        # This is here cause of silly python things, need to fix.
        cp[i][m] = 0
    return (move,score)
