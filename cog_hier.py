import math
import games
import numpy as np

def poisson(lmbda,i):
    return lmbda ** i * math.e ** (-lmbda) /  math.factorial(i)

def NormalizedPoisson(lmbda,i):
    poissons = [poisson(lmbda,k) for k in range(i)]
    norm = sum(poissons)
    return [v / norm for v in poissons]


# game is a game
# i is which player it is evaluating
# level is what level of the hierarchy they are at.
# the return value will be the expected utility of player i
# This is the initial recursive version, will likely switch to dynamic
# programming

def CogHierarchy(game,i,level,lmbda,re=False):
    if level == 0:
        strategy_profiles = [[1 / n for p in range(n)] for n in game.num_moves]
        util = games.ExpectedUtility(game,strategy_profiles,i)
        strs = strategy_profiles[i]
        return (util,strs)
    else:
        normed = NormalizedPoisson(lmbda,level)
        normed = np.array(normed,np.double)[np.newaxis]
        normed = normed.T
        strategy_profiles = []
        for player in range(len(game.num_moves)):
            if player != i:
                move_levels = np.zeros((game.num_moves[player],level))
                for lvl in range(level):
                    (util,strs) = CogHierarchy(game,player,lvl,lmbda)
                    move_levels[:,lvl] = strs
                strategy = move_levels.dot(normed)
                strategy_profiles.append(strategy)
            else:
                strategy_profiles.append([0 for mvs in range(game.num_moves[i])])
        (move,score) = games.BestResponse(game,strategy_profiles,i)
        strategy_profiles[i][move] = 1
        return (score[0],strategy_profiles[i])
